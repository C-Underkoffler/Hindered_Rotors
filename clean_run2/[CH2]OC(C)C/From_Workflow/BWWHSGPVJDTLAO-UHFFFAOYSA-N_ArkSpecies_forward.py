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

externalSymmetry = 18.0

spinMultiplicity = 2

opticalIsomers = 1

energy = {
    'M06-2X/cc-pVTZ': Log('BWWHSGPVJDTLAO-UHFFFAOYSA-N_GeoFreq_a1.log'),
}

geometry = Log('BWWHSGPVJDTLAO-UHFFFAOYSA-N_GeoFreq_a1.log')

frequencies = Log('BWWHSGPVJDTLAO-UHFFFAOYSA-N_GeoFreq_a1.log')

rotors = [
     HinderedRotor(scanLog=Log('BWWHSGPVJDTLAO-UHFFFAOYSA-N_36by10.0_tor01_a1.log'), pivots=[1, 2], top=[2, 3, 4, 6, 7, 8, 9, 10, 11, 12], fit='fourier'),
     HinderedRotor(scanLog=Log('BWWHSGPVJDTLAO-UHFFFAOYSA-N_36by10.0_tor04_a1.log'), pivots=[1, 5], top=[5, 13, 14], fit='fourier'),
     HinderedRotor(scanLog=Log('BWWHSGPVJDTLAO-UHFFFAOYSA-N_36by10.0_tor13_a1.log'), pivots=[2, 4], top=[4, 10, 11, 12], fit='fourier'),
     HinderedRotor(scanLog=Log('BWWHSGPVJDTLAO-UHFFFAOYSA-N_36by10.0_tor12_a1.log'), pivots=[2, 3], top=[3, 7, 8, 9], fit='fourier'),
]

