#!/usr/bin/env python
# -*- coding: utf-8 -*-

atoms = {
    'H': 9,
    'C': 4,
    'O': 1,
}

bonds = {
    'C-O': 1,
    'O-H': 1,
    'C-C': 3,
    'C-H': 8,
}

linear = False

externalSymmetry = 2.0

spinMultiplicity = 2

opticalIsomers = 1

energy = {
    'M06-2X/cc-pVTZ': Log('SXIFAEWFOJETOA-UHFFFAOYSA-N_GeoFreq_a1.log'),
}

geometry = Log('SXIFAEWFOJETOA-UHFFFAOYSA-N_GeoFreq_a1.log')

frequencies = Log('SXIFAEWFOJETOA-UHFFFAOYSA-N_GeoFreq_a1.log')

rotors = [
     HinderedRotor(scanLog=Log('SXIFAEWFOJETOA-UHFFFAOYSA-N_36by10.0_tor03_a1.log'), pivots=[1, 4], top=[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], fit='fourier'),
     HinderedRotor(scanLog=Log('SXIFAEWFOJETOA-UHFFFAOYSA-N_36by10.0_tor12_a1.log'), pivots=[2, 3], top=[3, 5, 8, 9, 12, 13], fit='fourier'),
     HinderedRotor(scanLog=Log('SXIFAEWFOJETOA-UHFFFAOYSA-N_36by10.0_tor13_a1.log'), pivots=[2, 4], top=[1, 4, 10, 11, 14], fit='fourier'),
     HinderedRotor(scanLog=Log('SXIFAEWFOJETOA-UHFFFAOYSA-N_36by10.0_tor24_a1.log'), pivots=[3, 5], top=[5, 12, 13], fit='fourier'),
]

