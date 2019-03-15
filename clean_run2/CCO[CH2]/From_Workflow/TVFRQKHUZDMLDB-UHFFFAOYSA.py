#!/usr/bin/env python
# -*- coding: utf-8 -*-

atoms = {
    'H': 7,
    'C': 3,
    'O': 1,
}

bonds = {
    'C-O': 2,
    'C-C': 1,
    'C-H': 7,
}

linear = False

externalSymmetry = 6.0

spinMultiplicity = 2

opticalIsomers = 1

energy = {
    'M06-2X/cc-pVTZ': Log('TVFRQKHUZDMLDB-UHFFFAOYSA.log'),
}

geometry = Log('TVFRQKHUZDMLDB-UHFFFAOYSA.log')

frequencies = Log('TVFRQKHUZDMLDB-UHFFFAOYSA.log')

rotors = [
     HinderedRotor(scanLog=Log('/home/underkoffler.c/Code/Hindered_Rotors/clean_run2/CCO[CH2]/From_Workflow/TVFRQKHUZDMLDB-UHFFFAOYSA_tor01.log'), pivots=[1, 2], top=[2, 3, 5, 6, 7, 8, 9], fit='fourier'),
     HinderedRotor(scanLog=Log('/home/underkoffler.c/Code/Hindered_Rotors/clean_run2/CCO[CH2]/From_Workflow/TVFRQKHUZDMLDB-UHFFFAOYSA_tor03.log'), pivots=[1, 4], top=[4, 10, 11], fit='fourier'),
     HinderedRotor(scanLog=Log('/home/underkoffler.c/Code/Hindered_Rotors/clean_run2/CCO[CH2]/From_Workflow/TVFRQKHUZDMLDB-UHFFFAOYSA_tor12.log'), pivots=[2, 3], top=[3, 7, 8, 9], fit='fourier'),
]
