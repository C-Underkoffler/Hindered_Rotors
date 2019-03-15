#!/usr/bin/env python
# -*- coding: utf-8 -*-

atoms = {
    'H': 8,
    'C': 4,
    'O': 2,
}

bonds = {
    'C-O': 2,
    'C=O': 1,
    'C-C': 2,
    'C-H': 8,
}

linear = False

externalSymmetry = 9.0

spinMultiplicity = 1

opticalIsomers = 1

energy = {
    'M06-2X/cc-pVTZ': Log('RJUFJBKOKNCXHH-UHFFFAOYSA.log'),
}

geometry = Log('RJUFJBKOKNCXHH-UHFFFAOYSA.log')

frequencies = Log('RJUFJBKOKNCXHH-UHFFFAOYSA.log')

rotors = [
     HinderedRotor(scanLog=Log('/home/underkoffler.c/Code/Hindered_Rotors/clean_run2/CCC(=O)OC/From_Workflow/RJUFJBKOKNCXHH-UHFFFAOYSA_tor04.log'), pivots=[1, 5], top=[5, 12, 13, 14], fit='fourier'),
     HinderedRotor(scanLog=Log('/home/underkoffler.c/Code/Hindered_Rotors/clean_run2/CCC(=O)OC/From_Workflow/RJUFJBKOKNCXHH-UHFFFAOYSA_tor05.log'), pivots=[1, 6], top=[2, 3, 4, 6, 7, 8, 9, 10, 11], fit='fourier'),
     HinderedRotor(scanLog=Log('/home/underkoffler.c/Code/Hindered_Rotors/clean_run2/CCC(=O)OC/From_Workflow/RJUFJBKOKNCXHH-UHFFFAOYSA_tor23.log'), pivots=[3, 4], top=[4, 9, 10, 11], fit='fourier'),
     HinderedRotor(scanLog=Log('/home/underkoffler.c/Code/Hindered_Rotors/clean_run2/CCC(=O)OC/From_Workflow/RJUFJBKOKNCXHH-UHFFFAOYSA_tor25.log'), pivots=[3, 6], top=[1, 2, 5, 6, 12, 13, 14], fit='fourier'),
]
