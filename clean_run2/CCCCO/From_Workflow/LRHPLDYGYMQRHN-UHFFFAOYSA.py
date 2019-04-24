#!/usr/bin/env python
# -*- coding: utf-8 -*-

atoms = {
    'H': 10,
    'C': 4,
    'O': 1,
}

bonds = {
    'C-O': 1,
    'O-H': 1,
    'C-C': 3,
    'C-H': 9,
}

linear = False

externalSymmetry = 3.0

spinMultiplicity = 1

opticalIsomers = 1

energy = {
    'M06-2X/cc-pVTZ': Log('LRHPLDYGYMQRHN-UHFFFAOYSA.log'),
}

geometry = Log('LRHPLDYGYMQRHN-UHFFFAOYSA.log')

frequencies = Log('LRHPLDYGYMQRHN-UHFFFAOYSA.log')

rotors = [
     HinderedRotor(scanLog=Log('/home/underkoffler.c/Code/Hindered_Rotors/clean_run2/CCCCO/From_Workflow/LRHPLDYGYMQRHN-UHFFFAOYSA_tor03.log'), pivots=[1, 4], top=[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], fit='fourier'),
     HinderedRotor(scanLog=Log('/home/underkoffler.c/Code/Hindered_Rotors/clean_run2/CCCCO/From_Workflow/LRHPLDYGYMQRHN-UHFFFAOYSA_tor12.log'), pivots=[2, 3], top=[3, 5, 6, 7, 12, 13, 14], fit='fourier'),
     HinderedRotor(scanLog=Log('/home/underkoffler.c/Code/Hindered_Rotors/clean_run2/CCCCO/From_Workflow/LRHPLDYGYMQRHN-UHFFFAOYSA_tor13.log'), pivots=[2, 4], top=[1, 4, 10, 11, 15], fit='fourier'),
     HinderedRotor(scanLog=Log('/home/underkoffler.c/Code/Hindered_Rotors/clean_run2/CCCCO/From_Workflow/LRHPLDYGYMQRHN-UHFFFAOYSA_tor24.log'), pivots=[3, 5], top=[5, 12, 13, 14], fit='fourier'),
]
