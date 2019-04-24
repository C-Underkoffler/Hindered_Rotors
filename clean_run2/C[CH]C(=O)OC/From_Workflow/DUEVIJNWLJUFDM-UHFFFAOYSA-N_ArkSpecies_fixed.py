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

externalSymmetry = 9.0

spinMultiplicity = 2

opticalIsomers = 1

energy = {
    'M06-2X/cc-pVTZ': Log('DUEVIJNWLJUFDM-UHFFFAOYSA-N_GeoFreq_a1.log'),
}

geometry = Log('DUEVIJNWLJUFDM-UHFFFAOYSA-N_GeoFreq_a1.log')

frequencies = Log('DUEVIJNWLJUFDM-UHFFFAOYSA-N_GeoFreq_a1.log')

rotors = [
     HinderedRotor(scanLog=Log('DUEVIJNWLJUFDM-UHFFFAOYSA-N_36by10.0_tor03_a1_F.log'), pivots=[1, 4], top=[4, 10, 11, 12], fit='fourier'),
     HinderedRotor(scanLog=Log('DUEVIJNWLJUFDM-UHFFFAOYSA-N_36by10.0_tor05_a1_F.log'), pivots=[1, 6], top=[2, 3, 5, 6, 7, 8, 9, 13], fit='fourier'),
     HinderedRotor(scanLog=Log('DUEVIJNWLJUFDM-UHFFFAOYSA-N_36by10.0_tor24_a1_F.log'), pivots=[3, 5], top=[1, 2, 4, 5, 6, 10, 11, 12, 13], fit='fourier'),
     HinderedRotor(scanLog=Log('DUEVIJNWLJUFDM-UHFFFAOYSA-N_36by10.0_tor45_a1_F.log'), pivots=[5, 6], top=[1, 2, 4, 6, 10, 11, 12], fit='fourier'),
]

