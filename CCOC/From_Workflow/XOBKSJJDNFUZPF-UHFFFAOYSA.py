#!/usr/bin/env python
# -*- coding: utf-8 -*-

atoms = {
    'H': 8,
    'C': 3,
    'O': 1,
}

bonds = {
    'C-O': 2,
    'C-C': 1,
    'C-H': 8,
}

linear = False

externalSymmetry = 9.0

spinMultiplicity = 1

opticalIsomers = 1

energy = {
    'M06-2X/cc-pVTZ': Log('XOBKSJJDNFUZPF-UHFFFAOYSA.log'),
}

geometry = Log('XOBKSJJDNFUZPF-UHFFFAOYSA.log')

frequencies = Log('XOBKSJJDNFUZPF-UHFFFAOYSA.log')

rotors = [
     HinderedRotor(scanLog=Log('/home/underkoffler.c/Code/Hindered_Rotors/CCOC/From_Workflow/XOBKSJJDNFUZPF-UHFFFAOYSA_tor01.log'), pivots=[1, 2], top=[2, 3, 5, 6, 7, 8, 9], fit='fourier'),
     HinderedRotor(scanLog=Log('/home/underkoffler.c/Code/Hindered_Rotors/CCOC/From_Workflow/XOBKSJJDNFUZPF-UHFFFAOYSA_tor03.log'), pivots=[1, 4], top=[4, 10, 11, 12], fit='fourier'),
     HinderedRotor(scanLog=Log('/home/underkoffler.c/Code/Hindered_Rotors/CCOC/From_Workflow/XOBKSJJDNFUZPF-UHFFFAOYSA_tor12.log'), pivots=[2, 3], top=[3, 7, 8, 9], fit='fourier'),
]
