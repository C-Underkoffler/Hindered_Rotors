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
    'M06-2X/cc-pVTZ': Log('FBRHVBFWGRGMCF-UHFFFAOYSA-N_GeoFreq_a2.log'),
}

geometry = Log('FBRHVBFWGRGMCF-UHFFFAOYSA-N_GeoFreq_a2.log')

frequencies = Log('FBRHVBFWGRGMCF-UHFFFAOYSA-N_GeoFreq_a2.log')

rotors = [
     HinderedRotor(scanLog=Log('FBRHVBFWGRGMCF-UHFFFAOYSA-N_36by10.0_tor01_a2_F.log'), pivots=[1, 2], top=[2, 3, 5, 6, 7, 8, 9, 13, 14], fit='fourier'),
     HinderedRotor(scanLog=Log('FBRHVBFWGRGMCF-UHFFFAOYSA-N_36by10.0_tor03_a2_F.log'), pivots=[1, 4], top=[4, 10, 11, 12], fit='fourier'),
     HinderedRotor(scanLog=Log('FBRHVBFWGRGMCF-UHFFFAOYSA-N_36by10.0_tor14_a2_F.log'), pivots=[2, 5], top=[5, 13, 14], fit='fourier'),
     HinderedRotor(scanLog=Log('FBRHVBFWGRGMCF-UHFFFAOYSA-N_36by10.0_tor12_a2_F.log'), pivots=[2, 3], top=[3, 7, 8, 9], fit='fourier'),
]

