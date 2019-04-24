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

externalSymmetry = 3.0

spinMultiplicity = 2

opticalIsomers = 1

energy = {
    'M06-2X/cc-pVTZ': Log('DBQZVPSKYUCKNT-UHFFFAOYSA-N_GeoFreq_a1.log'),
}

geometry = Log('DBQZVPSKYUCKNT-UHFFFAOYSA-N_GeoFreq_a1.log')

frequencies = Log('DBQZVPSKYUCKNT-UHFFFAOYSA-N_GeoFreq_a1.log')

rotors = [
     HinderedRotor(scanLog=Log('DBQZVPSKYUCKNT-UHFFFAOYSA-N_36by10.0_tor02_a1.log'), pivots=[1, 3], top=[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], fit='fourier'),
     HinderedRotor(scanLog=Log('DBQZVPSKYUCKNT-UHFFFAOYSA-N_36by10.0_tor14_a1.log'), pivots=[2, 5], top=[4, 5, 10, 11, 12, 13], fit='fourier'),
     HinderedRotor(scanLog=Log('DBQZVPSKYUCKNT-UHFFFAOYSA-N_36by10.0_tor12_a1.log'), pivots=[2, 3], top=[1, 3, 8, 9, 14], fit='fourier'),
     HinderedRotor(scanLog=Log('DBQZVPSKYUCKNT-UHFFFAOYSA-N_36by10.0_tor34_a1.log'), pivots=[4, 5], top=[1, 2, 3, 5, 6, 7, 8, 9, 13, 14], fit='fourier'),
]

