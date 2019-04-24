from ase.calculators.gaussian import Gaussian as ASE_Gaussian
from autotst.calculators.gaussian import read_gaussian_out


from autotst.calculators.gaussian import Gaussian as AutoTST_Gaussian
from autotst.calculators.statmech import StatMech as AutoTST_StatMech
from autotst.species import Conformer, Species
from autotst.job import Job as AutoTST_Job

from hotbit import Hotbit

import os
import subprocess
import shlex

import datetime

import pickle

from rdkit import Chem

import cclib

import arkane

# Inputs:

SMILES_list = [
    'OOCC(C)O[O]'
]


Conf_list = []
Rxn_list = None
modelChemistry = 'M06-2X/cc-pVTZ'
base_path = '/home/underkoffler.c/Code/Hindered_Rotors/clean_run2'
given_steps = 36
given_stepsize = 10.0
log_name = None
master_log_name = None
ark_dict_file = None
ThermoJob = True
max_attempt = 20








# Helper Functions


def rote_Rotor_Input(conformer, 
                     torsion, 
                     file_name, 
                     path=None, 
                     method='m062x', 
                     basis='6-311+g(2df,2p)', 
                     job='Opt=(CalcFC,ModRedun)', 
                     steps=72, 
                     stepsize_deg=10.0,
                     locked_torsions=None):
    """
    Write Gaussian input file for torsion scan

    conformer :: Conformer Object
    torsion   :: Torsion Object
    file_name :: desired file name to be written to
    
    path     :: path of file to write
    method   :: Gaussian method
    basis    :: Gaussian basis
    job      :: Gaussian job key word

    steps        :: Number of steps in scan
    stepsize_deg :: change in DEGREES between steps
    """
    
    if path is None:
        path = os.getcwd()
        

    assert isinstance(stepsize_deg, float)
    
    (i, j, k, l) = (-1, -1, -1, -1)
    (i, j, k, l) = torsion.atom_indices
    
    found_matching_torsion = False
    for c_torsion in conformer.get_torsions():
        [a, b, c, d] = c_torsion.atom_indices
        if [a, b, c, d] == [i, j, k, l]:
            found_matching_torsion = True
            
    assert found_matching_torsion, "Did not find matching torsion within conformer"
    
    mol = conformer.rmg_molecule
    mol.updateMultiplicity()

    output = '%nprocshared=20\n'
    output += '%mem=5GB\n'
    output += '#p {0}/{1} {2}\n'.format(method, basis, job)
    output += '\nGaussian Input Prepared from Scan Object\n'
    output += '\n0 {}\n'.format(mol.multiplicity)

    for atom in mol.atoms:
        output += "{}     {}     {}     {}\n".format(atom.element, atom.coords[0], atom.coords[1], atom.coords[2])

    output += '\n'

    # For atom IDs, need to be careful to adjust mol's IDs by +1 so that they start at 1 instead of zero
    for bond in mol.getAllEdges():
        output += 'B {0} {1}\n'.format(bond.atom1.sortingLabel+1, bond.atom2.sortingLabel+1)

    adj_i = i+1
    adj_j = j+1
    adj_k = k+1
    adj_l = l+1
    
    output = output + 'D {0} {1} {2} {3} S {4} {5}'.format(adj_i, adj_j, adj_k, adj_l, steps, stepsize_deg)
    output += '\n\n\n'

    with open(os.path.join(path, file_name), 'w') as F:
        F.write(output)
        

    return



def update_Conformer(conformer, file_name, path=None):
    """
    Updates conformer geometry from Gaussian geometry optimization output. If no filename specified tries by naming convention within path

    ACHTUNG!!! No Checks for whether conformer in file matches given conformer

    filename :: Geometry optimization log from Gaussian
    path :: path of file, default to cwd
    """

    
    if path is None:
        path = os.getcwd()

    os.chdir(path)
    conformer.ase_molecule = read_gaussian_out(file_name)
    
    conformer.update_coords()
    
    return conformer

def GeoFreqCom_from_Conf(conf, file_name=None, path=None):
    
    gaus_job = ASE_Gaussian()
    
    SMILES = conf.smiles
    
    augInChIKey = Chem.rdinchi.InchiToInchiKey(Chem.MolToInchi(
        Chem.MolFromSmiles(SMILES)))
                
    
    if file_name is None:
        gaus_job.label = augInChIKey + '_GeoFreq'
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



def hotbit_lowest_conf(SMILES):
    path = os.path.join('{}_Confs'.format(SMILES))
    
    
    if not os.path.isdir(path):
        os.makedirs(path)
    
    SMILES_list = [SMILES]
    spec = Species(SMILES_list)
    spec.generate_conformers(calculator=Hotbit())
    print SMILES
    print
    print 'Generated conformer for {}'.format(SMILES)
    lowest_conf = None
    lowest_energy = None
    
    conf_count = 0
    for smiles, confs in spec.conformers.items():
        print smiles
        if smiles == SMILES:
            
            print '{} conf for {}'.format(len(confs), smiles)
            
            for conf in confs:
                conf_count += 1
                conf.ase_molecule.set_calculator(Hotbit())

                conf.energy = conf.ase_molecule.get_potential_energy()
                print 'Found Conf {} energy of {}'.format(conf_count, conf.energy)

                if (conf.energy < lowest_energy) or (lowest_energy is None):
                    lowest_energy = conf.energy
                    lowest_conf = conf
    
                with open(os.path.join(path, '{}_conf{}'.format(SMILES, conf_count)), 'wb') as F:
                    atomcoords = conf.ase_molecule.get_positions()
                    atomnos = conf.ase_molecule.get_atomic_numbers()
                    energy = conf.energy
                    pickle.dump([SMILES, atomcoords, atomnos, energy], F)
            
    return lowest_conf


def exists_and_complete(path):
    exists_and_complete = False
    auto_g = AutoTST_Gaussian()
    
    if os.path.isfile(path):
        if False not in auto_g.verify_output_file(path):
            exists_and_complete = True
    
    return exists_and_complete


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


def write_ArkaneThermoInput(filename, modelChemistry, spec_name, spec_file, path=None):
    """
    Writes thermo input file for Arkane
    
    filename :: name of file that will be written to
    modelChemistry :: ModelChemistry used when finding opt geometry and frequencies
    spec_name :: label for species
    spec_file :: name of species file (needs to be in the same directory)
    """
    
    
    output = ['#!/usr/bin/env python',
              '# -*- coding: utf-8 -*-',
              '',
              'modelChemistry = "{0}"'.format(modelChemistry),
              'useHinderedRotors = True',
              'useBondCorrections = True',
              '',
              "species('{0}', '{1}')\n\nstatmech('{0}')".format(spec_name, spec_file),
              "thermo('{0}', '{1}')".format(spec_name, 'NASA')]

    output = '\n'.join(output)

    if path is None:
        path = os.getcwd()
    
    with open(os.path.join(path,filename), 'w') as f:
        f.write(output)
    
    return















# Workflow


"""
General premise:


Iterate list of smiles, conf, or conf in reactions:

If GeoFreq log does not exist or is incomplete:

    Writes GeoFreq Input if none found

    Executes GeoFreq Input
    Continues to next smiles in iteration

Else GeoFreq log is complete

    Updates geometry from GeoFreq log









    If all torsions have been deamed valid:

        Writes species.py for SMILESif not found

        If specified as thermo calc:

            Writes thermo input for Arkane if none found
            Executes thermo input

            Adds arkane class instance to dictionary by smile


"""



ark_dict = {}


assert (SMILES_list is not None) or (Rxn_list is not None) or (len(Conf_list)!=0)

if (SMILES_list is not None):
    Conf_list += [Conformer(SMILES) for SMILES in SMILES_list]

if (Rxn_list is not None):
    for rxn in Rxn_list:
        for species in rxn.reactants:
            for reac_list in species.conformers.values():
                Conf_list += reac_list

        for species in rxn.products:
            for prod_list in species.conformers.values():
                Conf_list += prod_list

if log_name is None:
    log_name = 'Rotors_{0}by{1}_maxa{2}_Log'.format(given_steps, given_stepsize, max_attempt)

if master_log_name is None:
    master_log_name = 'Master_{0}by{1}_maxa{2}_Log'.format(given_steps, given_stepsize, max_attempt)
    
master_log = []
log = None
    

for conf in Conf_list:
    SMILES = conf.smiles
    
    if log is not None:
        output = '\n\n'.join(log)
        with open(os.path.join(path, log_name), 'w') as f:
            f.write(output)
            
        master_log += log
        master_output = '\n\n'.join(master_log)
        with open(os.path.join(base_path, master_log_name), 'w') as mastf:
            mastf.write(master_output)

    log = []
    path = '{0}/{1}/From_Workflow'.format(base_path, SMILES)

    if not os.path.isdir(path):
        os.makedirs(path)

    os.chdir(path)
    print os.getcwd()

    if not os.path.isfile('rotors_run_script'):
        generate_rotors_run_script(path=path)

    log += ['\n\n===========================================================================================']
    now = datetime.datetime.now()
    log += ['{}'.format(now)]

    log += ['Beginning workflow for {0} at:\n\t{1}'.format(SMILES, path)]

    augInChIKey = Chem.rdinchi.InchiToInchiKey(Chem.MolToInchi(
        Chem.MolFromSmiles(SMILES)))

    attempt_loop = True
    attempt = max_attempt + 1 #Defined as ...+1 because I wanted the attempt -= 1 visible at the beginning of the while loop
    while attempt > 0 and attempt_loop:
        # Iterating through each possible attempt
        
        attempt -= 1
            
        temp_mast = master_log + log
        temp_output = '\n\n'.join(temp_mast)
        with open(os.path.join(base_path, master_log_name), 'w') as mastf:
            mastf.write(temp_output)
    
    
        geo_Freq_Base = augInChIKey + '_GeoFreq_a{}'.format(attempt)
        geo_Freq_Com = geo_Freq_Base + '.com'
        geo_Freq_Log = geo_Freq_Base + '.log'

        if not exists_and_complete(geo_Freq_Log):
            if attempt>1:
                log += ['No Completed GeoFreq found for attempt {}'.format(attempt)]

                #print '\tSkipping Conformer since no Geo Freq at attempt {}'.format(attempt)
                continue #to next attempt

            else:
                #First attempt, OK to generate initial geometry
                log += ['Geometry & Frequency log file NOT FOUND or NOT COMPLETE\n\t{0} for {1} NOT FOUND or NOT COMPLETE.\n\tLooking for {2}'.format(geo_Freq_Log, SMILES, geo_Freq_Com)]

                if not os.path.isfile(geo_Freq_Com):
                    #assert False, "Protecting my mems. Comment out for a complete disregard of your mems"
                    log += ['Geometry & Frequencey input file NOT FOUND\n\t{0} for {1} NOT FOUND.\n\tGenerating one now...'.format(geo_Freq_Com, SMILES)]
		    
                    lowest_conf = None

                   
                    lowest_conf = hotbit_lowest_conf(SMILES)
                        
                    assert lowest_conf is not None, 'Hotbit Solution not working'
		    log += ['Lowest conformer generated using AutoTST conformer generation and hotbit calculator']

                    conf = lowest_conf

                    GeoFreqCom_from_Conf(lowest_conf, geo_Freq_Base, path=path)

                else:
                    log += ['Using previous geometry & frequency input file']

            assert os.path.isfile(geo_Freq_Com)
            log += ['EXECUTING {0}'.format(geo_Freq_Com)]
            subprocess.call(shlex.split('sbatch rotors_run_template.sh {0}'.format(geo_Freq_Base)))

        print
        log += ['\n\n===========================================================================================']


master_log += log
master_output = '\n\n'.join(master_log)
master_output += '\n\n!!!!!!!!!!!!!!!!!!\n!! ALL FINISHED !!\n!!!!!!!!!!!!!!!!!!'
with open(os.path.join(base_path, master_log_name), 'w') as mastf:
    mastf.write(master_output)

print '\n\n!!!!!!!!!!!!!!!!!!\n!! ALL FINISHED !!\n!!!!!!!!!!!!!!!!!!'

