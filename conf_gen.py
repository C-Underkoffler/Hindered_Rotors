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



base_path = '/home/underkoffler.c/Code/Hindered_Rotors'

master_log_name = 'Conf_Gen_Log.txt'

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


for SMILES in SMILES_list:
    path = '{0}/{1}/From_Workflow'.format(base_path, SMILES)
    os.chdir(path)
    
    lowest_conf = hotbit_lowest_conf(SMILES)
    
    pickle.dump(lowest_conf, '{}_lowest_conf.pickle'.format(SMILES))
    
    lowest_conf = pickle.load('{}_lowest_conf.pickle'.format(SMILES))
    