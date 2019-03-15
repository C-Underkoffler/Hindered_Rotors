#!/usr/bin/env python
# -*- coding: utf-8 -*-

atoms = {
    'H': 5,
    'C': 2,
    'O': 4,
}

bonds = {
    'C-O': 1,
    'C-H': 2,
    'O-H': 2,
    'C-C': 1,
    'C=O': 1,
    'N-C': 1,
    'N-O': 1,
    'N-H': 1,
}

linear = False

externalSymmetry = 1.0

spinMultiplicity = 1

opticalIsomers = 1

energy = {
    'M06-2X/cc-pVTZ': Log('PWGWQRXHVJJRD-UHFFFAOYSA.log'),
}

geometry = Log('PWGWQRXHVJJRD-UHFFFAOYSA.log')

frequencies = Log('PWGWQRXHVJJRD-UHFFFAOYSA.log')

rotors = [
     HinderedRotor(scanLog=Log('/home/underkoffler.c/Code/Hindered_Rotors/clean_run2/ONCC(=O)O/From_Workflow/PWGWQRXHVJJRD-UHFFFAOYSA_tor03.log'), pivots=[1, 4], top=[2, 3, 4, 5, 6, 7, 8, 9, 11], fit='fourier'),
     HinderedRotor(scanLog=Log('/home/underkoffler.c/Code/Hindered_Rotors/clean_run2/ONCC(=O)O/From_Workflow/PWGWQRXHVJJRD-UHFFFAOYSA_tor15.log'), pivots=[2, 6], top=[1, 3, 4, 5, 6, 7, 8, 9, 10], fit='fourier'),
     HinderedRotor(scanLog=Log('/home/underkoffler.c/Code/Hindered_Rotors/clean_run2/ONCC(=O)O/From_Workflow/PWGWQRXHVJJRD-UHFFFAOYSA_tor34.log'), pivots=[4, 5], top=[2, 3, 5, 6, 7, 8, 11], fit='fourier'),
     HinderedRotor(scanLog=Log('/home/underkoffler.c/Code/Hindered_Rotors/clean_run2/ONCC(=O)O/From_Workflow/PWGWQRXHVJJRD-UHFFFAOYSA_tor45.log'), pivots=[5, 6], top=[2, 3, 6, 11], fit='fourier'),
]
