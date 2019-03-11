import numpy as np

import subprocess
import shlex

import cclib

import os

from autotst.species import Conformer, Species

from hotbit import Hotbit

from ase.calculators.gaussian import Gaussian as ASE_Gaussian

from rdkit import Chem

import datetime


SMILES_list = [
    'CCCCO',
    'CCCC[O]',
    'CCC[CH]O',
    'CC[CH]CO',
    'C[CH]CCO',
    '[CH2]CCCO',
    'CCOC',
    'C[CH]OC',
    'CCO[CH2]',
    '[CH2]COC',
    'COC(C)C',
    'CO[C](C)C',
    '[CH2]OC(C)C',
    '[CH2]C(C)OC',
    'CCC(=O)OC',
    'C[CH]C(=O)OC',
    '[CH2]CC(=O)OC',
    '[CH2]OC(=O)CC',
    'ONCC(=O)O',
]

base_paths = [
    '/home/underkoffler.c/Code/Hindered_Rotors',
    '/home/underkoffler.c/Code/Hindered_Rotors/clean_run1'
]





def GeoFreqCom_from_Conf(conf, file_name=None):
    
    gaus_job = ASE_Gaussian()
    
    if file_name is None:
        gaus_job.label = conf.rmg_molecule.toAugmentedInChIKey() + '_GeoFreq'
    else:
        gaus_job.label = file_name
        
    gaus_job.parameters['mem'] = '5GB'
    gaus_job.parameters['nprocshared'] = '20'
    gaus_job.parameters['method'] = 'm062x'
    gaus_job.parameters['basis'] = '6-311+g(2df,2p)'
    conf.rmg_molecule.updateMultiplicity()
    gaus_job.parameters['multiplicity'] = conf.rmg_molecule.multiplicity
    gaus_job.extra = 'opt=(calcfc,verytight,gdiis,maxcycles=900) freq iop(7/33=1,2/16=3)'

    
    del gaus_job.parameters['force']
    
    gaus_job.write_input(conf.ase_molecule)
    
    return




def generate_rotors_run_script(path=None):
    
    if path is None:
        path = os.getcwd()
    
    lst_template = ["#!/bin/bash",
                    "",
                    "#SBATCH --job-name=AutoScript",
                    "#SBATCH --output=$1.log",
                    "",
                    "## number of nodes",
                    "#SBATCH -N 1",
                    "#SBATCH --exclusive",
                    "#SBATCH --partition=general",
                    "#SBATCH --mem=120000",
                    "",
                    "## export GAUSS_SCRDIR=/scratch/$USER/gaussian_scratch",
                    "## make the directory if it doesn't exist already",
                    "## mkdir -p $GAUSS_SCRDIR",
                    "",
                    "## run gaussian, with the desired input file",
                    "g16 $1.com",
                    "",
                    ""]


    template ='\n'.join(lst_template)
    with open('{}/rotors_run_template.sh'.format(path), 'w') as f:
        f.write(template)
        
    return




def geos_of_interest(parser=None, file_name=None):
    if parser is None:
        assert file_name is not None, "Need either parser or file_name"
        parser = cclib.io.ccread(file_name)

    min_energy = None
    min_coords = None

    atomnos = parser.atomnos

    opt_indices = [idx for idx, status in enumerate(parser.optstatus) if status==2]
    opt_SCFenergies = [parser.scfenergies[idx] for idx in opt_indices]

    init_atomcoords = parser.atomcoords[0]
    init_energy = parser.scfenergies[0]

    first_atomcoords = parser.atomcoords[opt_indices[0]]
    first_energy = parser.scfenergies[opt_indices[0]]

    last_atomcoords = parser.atomcoords[opt_indices[-1]]
    last_energy = parser.scfenergies[opt_indices[-1]]

    lowest_atomcoords = None
    lowest_energy = None
    for opt_idx in opt_indices:
        energy = parser.scfenergies[opt_idx]
        if (energy < lowest_energy) or (lowest_energy is None):
            lowest_energy = energy
            lowest_atomcoords = parser.atomcoords[opt_idx]
    
    geometries = {}
    geometries['scan_init'] = [init_atomcoords, init_energy]
    geometries['sacn_first'] = [first_atomcoords, first_energy]
    geometries['scan_lowest'] = [lowest_atomcoords, lowest_energy]
    geometries['scan_last'] = [last_atomcoords, last_energy]
    
    return geometries




def hotbit_lowest_conf(SMILES):
    SMILES_list = [SMILES]
    spec = Species(SMILES_list)
    spec.generate_conformers(calculator=Hotbit())

    lowest_conf = None
    lowest_energy = None
    for smiles, confs in spec.conformers.items():
        for conf in confs:
            conf.ase_molecule.set_calculator(Hotbit())
            conf.energy = conf.ase_molecule.get_potential_energy()

            if (conf.energy < lowest_energy) or (lowest_energy is None):
                lowest_energy = conf.energy
                lowest_conf = conf

    return lowest_conf













# Begin Search
now = datetime.datetime.now()

master_output = '\n\nMaster conf search log at:\t{}\n\n'.format(now)


for SMILES in SMILES_list:
    output = '\n\n' + SMILES + '\n'
    output += 'Energy of conformer using hotbit: Log conformer came from\n\n'
    output += 'If log is scan, conformer chosen by lowest SCF energy\n\n'
    
    
    
    
    gen_conf = Conformer(SMILES)
    gen_conf.ase_molecule.set_calculator(Hotbit())
    gen_conf.energy = gen_conf.ase_molecule.get_potential_energy()

    conf_dict = {}
    conf_dict['default'] = gen_conf
    
    base_path_output = '/home/underkoffler.c/Code/Hindered_Rotors/clean_run2'
    path_output = '{}/{}/From_Workflow'.format(base_path_output, SMILES)
    if not os.path.isdir(path_output):
        os.makedirs(path_output)
    
    
    output += '{}\t:\t{}\n'.format('default', conf_dict['default'].energy)
    
    for base_path in base_paths:
        path = '{}/{}/From_Workflow'.format(base_path, SMILES)
        if not os.path.isdir(path):
            os.makedirs(path)

        os.chdir(path)

        for log in os.listdir(path):
            if log.endswith('.log'):
                parser = None
                
                new_key = path + '/' + log
                new_conf = Conformer(SMILES)
                
                try:
                    parser = cclib.io.ccread(log)
                    assert parser is not None
                    geos = geos_of_interest(parser=parser)
                except:
                    continue

                    
                output += new_key + '\n'
                with open(os.path.join(path_output, 'Lowest_Conf_Search.txt'), 'w') as f:
                    f.write(output)
        
                master_output += output
                with open(os.path.join(base_path_output, 'Mast_Conf_Search.txt'), 'w') as f:
                    f.write(master_output)
                

                atomcoords, scfenergy = geos['scan_lowest']

                new_conf.ase_molecule.set_positions(atomcoords)
                new_conf.update_coords_from(mol_type='ase')

                new_conf.ase_molecule.set_calculator(Hotbit())
                new_conf.energy = new_conf.ase_molecule.get_potential_energy()
                
                output += '\t{}\n'.format(new_conf.energy)
                
                
                conf_dict[new_key] = new_conf
                
                
                with open('Lowest_Conf_Search.txt', 'w') as f:
                    f.write(output)
        
                master_output += output
                with open(os.path.join(base_path_output, 'Mast_Conf_Search.txt'), 'w') as f:
                    f.write(master_output)

    
    output += '\nDone Searching through Logs\n'
    
    with open('Lowest_Conf_Search.txt', 'w') as f:
        f.write(output)
        
    master_output += output
    with open(os.path.join(base_path_output, 'Mast_Conf_Search.txt'), 'w') as f:
        f.write(master_output)
    
    
    
    
    already_hotbit_gened = False
    for key in conf_dict.keys():
        if '/home/underkoffler.c/Code/Hindered_Rotors/clean_run1' in key:
            already_hotbit_gened = True
    
    if not already_hotbit_gened:
        #hotbit_conf = Conformer(SMILES)
        #hotbit_conf.energy = -100
        hotbit_conf = hotbit_lowest_conf(SMILES)
        assert hotbit_conf.energy is not None

        conf_dict['hotbit_gen'] = hotbit_conf
        output += '{}\t:\t{}\n'.format('hotbit_gen', conf_dict['hotbit_gen'].energy)
    
    
    min_conf = None
    min_energy = None
    min_key = None
    
    for key, conf in conf_dict.items():
        assert conf.energy is not None
        if (min_energy is None) or (conf.energy < min_energy):
            min_conf = conf
            min_energy = conf.energy
            min_key = key
    
    
    output += '\nLOWEST FOUND:\n{}\t:\t{}\n'.format(min_energy, min_key)
                    
    base_path_output = '/home/underkoffler.c/Code/Hindered_Rotors/clean_run2'
    path_output = '{}/{}/From_Workflow'.format(base_path_output, SMILES)
    
    if not os.path.isdir(path_output):
        os.makedirs(path_output)
    os.chdir(path_output)
    
    generate_rotors_run_script(path=path_output)
    
    augInChIKey = Chem.rdinchi.InchiToInchiKey(Chem.MolToInchi(
            Chem.MolFromSmiles(SMILES)))
    
    geo_Freq_Base = augInChIKey + '_GeoFreq_a1'

    output += 'Creating geo-freq input for min_conf.\n\tConf sourced from {0}\n\tNew Geo-Freq Input: {1}\n'.format(min_key, geo_Freq_Base+'.com')
    GeoFreqCom_from_Conf(min_conf, file_name=geo_Freq_Base)
    
    subprocess.call(shlex.split('sbatch rotors_run_template.sh {0}'.format(geo_Freq_Base)))
    output += '\nEXECUTED {}.com\n\n\n'.format(geo_Freq_Base+'.com')
    
    
    
    
    
    with open('Lowest_Conf_Search.txt', 'w') as f:
        f.write(output)
        
    master_output += output
    with open(os.path.join(base_path_output, 'Mast_Conf_Search.txt'), 'w') as f:
        f.write(master_output)

