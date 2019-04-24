#!/usr/bin/env python
# -*- coding: utf-8 -*-

atoms = {
    'H': 8,
    'C': 4,
    'O': 2,
}

bonds = {
    'C=O': 1,
    'C-O': 2,
    'C-C': 2,
    'C-H': 8,
}

linear = False

externalSymmetry = 9.0

spinMultiplicity = 1

opticalIsomers = 1

energy = {
    'M06-2X/cc-pVTZ': Log('RJUFJBKOKNCXHH-UHFFFAOYSA-N_GeoFreq_a1.log'),
}

geometry = Log('RJUFJBKOKNCXHH-UHFFFAOYSA-N_GeoFreq_a1.log')

frequencies = Log('RJUFJBKOKNCXHH-UHFFFAOYSA-N_GeoFreq_a1.log')

rotors = [
     HinderedRotor(scanLog=Log('RJUFJBKOKNCXHH-UHFFFAOYSA-N_36by10.0_tor04_a1.log'), pivots=[1, 5], top=[5, 12, 13, 14], fit='fourier'),
     HinderedRotor(scanLog=Log('RJUFJBKOKNCXHH-UHFFFAOYSA-N_36by10.0_tor05_a1.log'), pivots=[1, 6], top=[2, 3, 4, 6, 7, 8, 9, 10, 11], fit='fourier'),
     HinderedRotor(scanLog=Log('RJUFJBKOKNCXHH-UHFFFAOYSA-N_36by10.0_tor23_a1.log'), pivots=[3, 4], top=[4, 9, 10, 11], fit='fourier'),
     HinderedRotor(scanLog=Log('RJUFJBKOKNCXHH-UHFFFAOYSA-N_36by10.0_tor25_a1.log'), pivots=[3, 6], top=[1, 2, 5, 6, 12, 13, 14], fit='fourier'),
]

