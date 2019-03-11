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


# Inputs:

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
    '[CH2]OC(=O)CC'
]


Conf_list = []
Rxn_list = None
modelChemistry = 'M06-2X/cc-pVTZ'
base_path = '/home/underkoffler.c/Code/Hindered_Rotors/clean_run1'
given_steps = 36
given_stepsize = 10.0
log_name = None
master_log_name = None
ark_dict_file = None
ThermoJob = False
attempt = 1








# Helper Functions


def rote_Rotor_Input(conformer, 
                     torsion, 
                     file_name, 
                     path=None, 
                     method='m062x', 
                     basis='6-311+g(2df,2p)', 
                     job='Opt=(CalcFC,ModRedun)', 
                     steps=72, 
                     stepsize_deg=10.0):
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
        F.close

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


























# Workflow


"""
General premise:


Iterate list of smiles, conf, or conf in reactions:
If GeoFreq log does not exist or is incomplete:

    Writes GeoFreq Input if none found

    Executes GeoFreq Input
    Continues to next smiles in iteration

Else:

    Updates geometry from GeoFreq log
    Generates scan object for every torsion

    Iterates through each scan object:

        If scan log does not exist or is incomplete:

            Writes scan input if none found

            Executes scan
            Continues to next scan in iteration

        Else:
            Updates scan with scan log

    If all scans have been updated from scan log:

        Writes species.py for SMILESif not found

        If specified as thermo calc:

            Writes thermo input for Arkane if none found
            Executes thermo input

            Adds arkane class instance to dictionary by smile


"""



ark_dict = {}

if ark_dict_file is None:
    ark_dict_file = 'ark_dict.pickle'


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
    log_name = 'Rotors_{0}by{1}_a{2}_Log'.format(given_steps, given_stepsize, attempt)

if master_log_name is None:
    master_log_name = 'Master_{0}by{1}_a{2}_Log'.format(given_steps, given_stepsize, attempt)
    
master_log = []
    
assert attempt > 0

for conf in Conf_list:
    SMILES = conf.smiles
    
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
    
    temp_mast = master_log + log
    temp_output = '\n\n'.join(temp_mast)
    with open(os.path.join(base_path, master_log_name), 'w') as mastf:
        mastf.write(temp_output)
    
    augInChIKey = Chem.rdinchi.InchiToInchiKey(Chem.MolToInchi(
            Chem.MolFromSmiles(SMILES)))
    
    geo_Freq_Base = augInChIKey + '_GeoFreq_a{}'.format(attempt)
    geo_Freq_Com = geo_Freq_Base + '.com'
    geo_Freq_Log = geo_Freq_Base + '.log'

    if not exists_and_complete(geo_Freq_Log):
        log += ['Geometry & Frequency log file NOT FOUND or NOT COMPLETE\n\t{0} for {1} NOT FOUND or NOT COMPLETE.\n\tLooking for {0}'.format(geo_Freq_Log, SMILES)]
        
        if not os.path.isfile(geo_Freq_Com):
            lowest_conf = None
            
            #log += ['Lowest Conformer Pickle NOT FOUND\n\t{}_lowest_conf.pickle NOT FOUND\n\tGenerating one using Hotbit...'.format(SMILES)]

            try:
                lowest_conf = hotbit_lowest_conf(SMILES)
            except:
                log += ['PROBLEMS WITH LOWEST CONFORMER SEARCH!! Consult Grad Dad']

                output = '\n\n'.join(log)
                with open(os.path.join(path, log_name), 'w') as f:
                    f.write(output)

                master_log += log
                master_output = '\n\n'.join(master_log)
                with open(os.path.join(base_path, master_log_name), 'w') as mastf:
                    mastf.write(master_output)
                continue
                
            assert lowest_conf is not None, 'Hotbit Solution not working'
            
            conf = lowest_conf
            
            log += ['Geometry & Frequencey input file NOT FOUND\n\t{0} for {1} NOT FOUND.\n\tGenerating one now...'.format(geo_Freq_Com, SMILES)]
            GeoFreqCom_from_Conf(lowest_conf, geo_Freq_Base, path=path)

        else:
            log += ['Using previous geometry & frequency input file']

        assert os.path.isfile(geo_Freq_Com)
        log += ['EXECUTING {0}'.format(geo_Freq_Com)]
        subprocess.call(shlex.split('sbatch rotors_run_template.sh {0}'.format(geo_Freq_Base)))
        

    else:
        log += ['Geometry & Frequency log file is complete!\n\t{0} for {1} is complete!'.format(geo_Freq_Log, SMILES)]
        geo_conf = update_Conformer(conf, geo_Freq_Log, path=path)
        
        all_Scans_Updated = True
        for torsion in geo_conf.get_torsions():
            (i, j, k, l) = (-1, -1, -1, -1)
            (i, j, k, l) = torsion.atom_indices

            scan_geo_log = geo_Freq_Log
            
            scan_rotor_base = augInChIKey + '_{0}by{1}_tor{2}{3}_a{4}'.format(given_steps, given_stepsize, j, k, attempt)
            scan_input_com = scan_rotor_base + '.com'
            scan_output_log = scan_rotor_base + '.log'

            log += ['\nLooking at {} torsion in {}'.format((i,j,k,l), SMILES)]
            
            temp_mast = master_log + log
            temp_output = '\n\n'.join(temp_mast)
            with open(os.path.join(base_path, master_log_name), 'w') as mastf:
                mastf.write(temp_output)

            verify_info = {}
            if exists_and_complete(os.path.join(path, scan_output_log)):
                log += ['\tTorsion log file is complete!\n\t\t{0} for {1} exists and is complete!'.format(scan_output_log, SMILES)]
                
                #I'm just trying to match naming convention in autotst.statmech without rewriting the convention there
                reduced_scan_log = augInChIKey.strip('-N') + '_tor{}{}.log'.format(j, k)
                
                subprocess.call(shlex.split('cp {} {}'.format(scan_output_log, reduced_scan_log)))
                
                auto_job = AutoTST_Job()
                print '\t', scan_output_log
                
                try:
                    scan_info = auto_job.verify_rotor(given_steps, given_stepsize, file_name=reduced_scan_log)
                except:
                    log += ['\tBROKE verify_rotor() method\n\t{}'.format(scan_output_log)]
                    
                    
                    log += ['\tCopying broken log to "..._BVM.log" for Broke verify_rotor() Method'] 
                    failed_name = scan_output_log
                    failed_rename = failed_name.strip('.log') + '_BVM.log'
                    subprocess.call(shlex.split('mv {} {}'.format(failed_name, failed_rename)))
                    
                             
                    log += ['\tRe-running with previous input file']

                    log += ['\tEXECUTING {0}'.format(scan_input_com)]
                    
                    subprocess.call(shlex.split('sbatch rotors_run_template.sh {0}'.format(scan_rotor_base)))
                    
                    output = '\n\n'.join(log)
                    with open(os.path.join(path, log_name), 'w') as f:
                        f.write(output)
     
                    master_log += log
                    master_output = '\n\n'.join(master_log)
                    with open(os.path.join(base_path, master_log_name), 'w') as mastf:
                        mastf.write(master_output)
                    continue

                    
                    
                    
                [verified, energy, atomnos, atomcoords] = scan_info
                
                if not verified:
                    all_Scans_Updated = False
                    log += ['{} NOT Verified. Suggest running with different initial geometry'.format((i, j, k, l))]
                else:
                    log += ['{} Verified!'.format((i, j, k, l))]
            else:
                all_Scans_Updated = False
                log += ['\tTorsion log file NOT FOUND or NOT COMPLETE.\n\t\t{0} for {1} NOT FOUND or NOT COMPLETE.\n\t\tLooking for existing {2}'.format(scan_output_log, SMILES, scan_input_com)]
                if not os.path.isfile(os.path.join(path, scan_input_com)):
                    log += ['\tTorsion input file NOT FOUND.\n\t\t{0} for {1} NOT FOUND.\n\t\tGenerating one now..'.format(scan_input_com, SMILES)]
                    
                    rote_Rotor_Input(geo_conf, torsion, scan_input_com, path=path, steps=given_steps, stepsize_deg=given_stepsize)
                else:
                    log += ['\tUsing previous torsion input file.\n\t\t{0} for {1} exists!'.format(scan_input_com, SMILES)]


                log += ['\tEXECUTING {0}'.format(scan_input_com)]
                subprocess.call(shlex.split('sbatch rotors_run_template.sh {0}'.format(scan_rotor_base)))


        if all_Scans_Updated:

            log += ['All scans for {0} have data!'.format(SMILES)]

            species_file = augInChIKey.strip('-N') + '.py'
            
            if not os.path.isfile(species_file):
                log += ['Arkane Species.py file NOT FOUND\n\t{0} NOT FOUND for {1}\n\tGenerating one now...'.format(species_file, SMILES)]

                torsions = conf.get_torsions()
                
                statmech_job = AutoTST_StatMech('Needs_Rxn_Str_This_Will_Do')
                statmech_job.model_chemistry = modelChemistry
                statmech_job.scratch = path
                statmech_job.write_arkane_for_reacts_and_prods(conf)
                
            else:
                log += ['Species.py for {0} exists!\n\t{1}'.format(SMILES, species_file)]

            assert os.path.isfile(species_file)

            if ThermoJob:
                log += ['Beginning Thermo Calculations']
                thermo_filename = augInChIKey + '_Thermo.py'
                
                out_path = path
                species_name = augInChI.strip('-N')
                
                if not os.path.isfile(thermo_filename):
                    log += ['Thermo input file NOT FOUND\n\t{0} NOT FOUND for {1}\t\nGenerating one now...'.format(thermo_filename, SMILES)]

                    write_ArkaneThermoInput(thermo_filename, modelChemistry, species_name, species_file)

                log += ['Executing Arkane Thermo Job for {0}\n\tAKA {1}'.format(species_file, SMILES)]
                log += ['Arkane log named "arkane.log"\n\tat {0}'.format(path)]

                ark = arkane.Arkane(inputFile=thermo_filename, outputDirectory=out_path)
                ark.plot = False
                ark.execute()
                ark_dict[SMILES] = ark
                
                """try:
                    with open(ark_dict_file, 'wb') as ark_f:
                        pickle.dump(ark_dict, ark_f)
                except:
                    pass"""
                    
    log += ['\n\n===========================================================================================']

    output = '\n\n'.join(log)
    with open(os.path.join(path, log_name), 'w') as f:
        f.write(output)
    
    master_log += log
    master_output = '\n\n'.join(master_log)
    with open(os.path.join(base_path, master_log_name), 'w') as mastf:
        mastf.write(master_output)
