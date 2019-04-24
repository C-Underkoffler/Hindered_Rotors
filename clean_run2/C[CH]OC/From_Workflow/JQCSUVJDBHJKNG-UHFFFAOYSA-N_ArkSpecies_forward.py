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

externalSymmetry = 9.0

spinMultiplicity = 2

opticalIsomers = 1

energy = {
    'M06-2X/cc-pVTZ': Log('JQCSUVJDBHJKNG-UHFFFAOYSA-N_GeoFreq_a2.log'),
}

geometry = Log('JQCSUVJDBHJKNG-UHFFFAOYSA-N_GeoFreq_a2.log')

frequencies = Log('JQCSUVJDBHJKNG-UHFFFAOYSA-N_GeoFreq_a2.log')

rotors = [
     HinderedRotor(scanLog=Log('JQCSUVJDBHJKNG-UHFFFAOYSA-N_36by10.0_tor03_a2.log'), pivots=[1, 4], top=[2, 4, 5, 6, 7, 11], fit='fourier'),
     HinderedRotor(scanLog=Log('JQCSUVJDBHJKNG-UHFFFAOYSA-N_36by10.0_tor02_a2.log'), pivots=[1, 3], top=[3, 8, 9, 10], fit='fourier'),
     HinderedRotor(scanLog=Log('JQCSUVJDBHJKNG-UHFFFAOYSA-N_36by10.0_tor13_a2.log'), pivots=[2, 4], top=[1, 3, 4, 8, 9, 10, 11], fit='fourier'),
]

