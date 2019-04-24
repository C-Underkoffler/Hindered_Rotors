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
    'M06-2X/cc-pVTZ': Log('DHVSQGCGLGSLDF-UHFFFAOYSA-N_GeoFreq_a3.log'),
}

geometry = Log('DHVSQGCGLGSLDF-UHFFFAOYSA-N_GeoFreq_a3.log')

frequencies = Log('DHVSQGCGLGSLDF-UHFFFAOYSA-N_GeoFreq_a3.log')

rotors = [
     HinderedRotor(scanLog=Log('DHVSQGCGLGSLDF-UHFFFAOYSA-N_36by-10.0_tor04_a3.log'), pivots=[1, 5], top=[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], fit='fourier'),
     HinderedRotor(scanLog=Log('DHVSQGCGLGSLDF-UHFFFAOYSA-N_36by-10.0_tor12_a3.log'), pivots=[2, 3], top=[1, 3, 5, 8, 9, 13, 14], fit='fourier'),
     HinderedRotor(scanLog=Log('DHVSQGCGLGSLDF-UHFFFAOYSA-N_36by-10.0_tor13_a3.log'), pivots=[2, 4], top=[4, 10, 11, 12], fit='fourier'),
     HinderedRotor(scanLog=Log('DHVSQGCGLGSLDF-UHFFFAOYSA-N_36by-10.0_tor24_a3.log'), pivots=[3, 5], top=[1, 5, 13, 14], fit='fourier'),
]

