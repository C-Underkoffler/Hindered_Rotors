#!/usr/bin/env python
# -*- coding: utf-8 -*-

atoms = {
    'H': 9,
    'C': 4,
    'O': 1,
}

bonds = {
    'C-O': 2,
    'C-C': 2,
    'C-H': 9,
}

linear = False

externalSymmetry = 9.0

spinMultiplicity = 2

opticalIsomers = 1

energy = {
    'M06-2X/cc-pVTZ': Log('FBRHVBFWGRGMCF-UHFFFAOYSA.log'),
}

geometry = Log('FBRHVBFWGRGMCF-UHFFFAOYSA.log')

frequencies = Log('FBRHVBFWGRGMCF-UHFFFAOYSA.log')

rotors = [
     HinderedRotor(scanLog=Log('/home/underkoffler.c/Code/Hindered_Rotors/clean_run1/[CH2]C(C)OC/From_Workflow/FBRHVBFWGRGMCF-UHFFFAOYSA-N-u1_tor01.log'), pivots=[1, 2], top=[2, 3, 5, 6, 7, 8, 9, 13, 14], fit='fourier'),
     HinderedRotor(scanLog=Log('/home/underkoffler.c/Code/Hindered_Rotors/clean_run1/[CH2]C(C)OC/From_Workflow/FBRHVBFWGRGMCF-UHFFFAOYSA-N-u1_tor03.log'), pivots=[1, 4], top=[4, 10, 11, 12], fit='fourier'),
     HinderedRotor(scanLog=Log('/home/underkoffler.c/Code/Hindered_Rotors/clean_run1/[CH2]C(C)OC/From_Workflow/FBRHVBFWGRGMCF-UHFFFAOYSA-N-u1_tor12.log'), pivots=[2, 3], top=[3, 7, 8, 9], fit='fourier'),
     HinderedRotor(scanLog=Log('/home/underkoffler.c/Code/Hindered_Rotors/clean_run1/[CH2]C(C)OC/From_Workflow/FBRHVBFWGRGMCF-UHFFFAOYSA-N-u1_tor14.log'), pivots=[2, 5], top=[5, 13, 14], fit='fourier'),
]
