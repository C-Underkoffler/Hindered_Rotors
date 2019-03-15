#!/usr/bin/env python
# -*- coding: utf-8 -*-

atoms = {
    'H': 7,
    'C': 4,
    'O': 2,
}

bonds = {
    'C-O': 2,
    'C=O': 1,
    'C-C': 2,
    'C-H': 7,
}

linear = False

externalSymmetry = 6.0

spinMultiplicity = 2

opticalIsomers = 1

energy = {
    'M06-2X/cc-pVTZ': Log('OJWHOIQFDAGZNF-UHFFFAOYSA.log'),
}

geometry = Log('OJWHOIQFDAGZNF-UHFFFAOYSA.log')

frequencies = Log('OJWHOIQFDAGZNF-UHFFFAOYSA.log')

rotors = [
     HinderedRotor(scanLog=Log('/home/underkoffler.c/Code/Hindered_Rotors/clean_run2/[CH2]OC(=O)CC/From_Workflow/OJWHOIQFDAGZNF-UHFFFAOYSA_tor05.log'), pivots=[1, 6], top=[6, 12, 13], fit='fourier'),
     HinderedRotor(scanLog=Log('/home/underkoffler.c/Code/Hindered_Rotors/clean_run2/[CH2]OC(=O)CC/From_Workflow/OJWHOIQFDAGZNF-UHFFFAOYSA_tor04.log'), pivots=[1, 5], top=[2, 3, 4, 5, 7, 8, 9, 10, 11], fit='fourier'),
     HinderedRotor(scanLog=Log('/home/underkoffler.c/Code/Hindered_Rotors/clean_run2/[CH2]OC(=O)CC/From_Workflow/OJWHOIQFDAGZNF-UHFFFAOYSA_tor23.log'), pivots=[3, 4], top=[4, 9, 10, 11], fit='fourier'),
     HinderedRotor(scanLog=Log('/home/underkoffler.c/Code/Hindered_Rotors/clean_run2/[CH2]OC(=O)CC/From_Workflow/OJWHOIQFDAGZNF-UHFFFAOYSA_tor24.log'), pivots=[3, 5], top=[1, 2, 5, 6, 12, 13], fit='fourier'),
]
