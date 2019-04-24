#!/usr/bin/env python
# -*- coding: utf-8 -*-

atoms = {
    'H': 5,
    'C': 2,
    'O': 3,
    'N': 1,
}

bonds = {
    'C-O': 1,
    'C-H': 2,
    'O-H': 2,
    'C-C': 1,
    'C=O': 1,
    'N-C': 1,
    'N-O': 1,
    'N-H': 1,
}

linear = False

externalSymmetry = 1.0

spinMultiplicity = 1

opticalIsomers = 1

energy = {
    'M06-2X/cc-pVTZ': Log('NPWGWQRXHVJJRD-UHFFFAOYSA-N_GeoFreq_a1.log'),
}

geometry = Log('NPWGWQRXHVJJRD-UHFFFAOYSA-N_GeoFreq_a1.log')

frequencies = Log('NPWGWQRXHVJJRD-UHFFFAOYSA-N_GeoFreq_a1.log')

rotors = [
     HinderedRotor(scanLog=Log('NPWGWQRXHVJJRD-UHFFFAOYSA-N_36by-10.0_tor03_a1.log'), pivots=[1, 4], top=[2, 3, 4, 5, 6, 7, 8, 9, 11], fit='fourier'),
     HinderedRotor(scanLog=Log('NPWGWQRXHVJJRD-UHFFFAOYSA-N_36by-10.0_tor15_a1.log'), pivots=[2, 6], top=[1, 3, 4, 5, 6, 7, 8, 9, 10], fit='fourier'),
     HinderedRotor(scanLog=Log('NPWGWQRXHVJJRD-UHFFFAOYSA-N_36by-10.0_tor34_a1.log'), pivots=[4, 5], top=[2, 3, 5, 6, 7, 8, 11], fit='fourier'),
     HinderedRotor(scanLog=Log('NPWGWQRXHVJJRD-UHFFFAOYSA-N_36by-10.0_tor45_a1.log'), pivots=[5, 6], top=[2, 3, 6, 11], fit='fourier'),
]

