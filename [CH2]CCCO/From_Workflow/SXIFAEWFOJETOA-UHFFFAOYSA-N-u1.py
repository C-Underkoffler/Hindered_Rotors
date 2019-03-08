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
    'M06-2X/cc-pVTZ': Log('SXIFAEWFOJETOA-UHFFFAOYSA-N-u1_GeoFreq.log'),
}

geometry = Log('SXIFAEWFOJETOA-UHFFFAOYSA-N-u1_GeoFreq.log')

frequencies = Log('SXIFAEWFOJETOA-UHFFFAOYSA-N-u1_GeoFreq.log')

rotors = [
     HinderedRotor(scanLog=Log('SXIFAEWFOJETOA-UHFFFAOYSA-N_tor03.log'), pivots=[1, 4], top=[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], fit='fourier'),
     HinderedRotor(scanLog=Log('SXIFAEWFOJETOA-UHFFFAOYSA-N_tor12.log'), pivots=[2, 3], top=[3, 5, 8, 9, 12, 13], fit='fourier'),
     HinderedRotor(scanLog=Log('SXIFAEWFOJETOA-UHFFFAOYSA-N_tor13.log'), pivots=[2, 4], top=[1, 4, 10, 11, 14], fit='fourier'),
     HinderedRotor(scanLog=Log('SXIFAEWFOJETOA-UHFFFAOYSA-N_tor24.log'), pivots=[3, 5], top=[5, 12, 13], fit='fourier'),
]