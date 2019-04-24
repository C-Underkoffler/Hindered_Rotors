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

externalSymmetry = 6.0

spinMultiplicity = 2

opticalIsomers = 1

energy = {
    'M06-2X/cc-pVTZ': Log('OJWHOIQFDAGZNF-UHFFFAOYSA-N_GeoFreq_a1.log'),
}

geometry = Log('OJWHOIQFDAGZNF-UHFFFAOYSA-N_GeoFreq_a1.log')

frequencies = Log('OJWHOIQFDAGZNF-UHFFFAOYSA-N_GeoFreq_a1.log')

rotors = [
     HinderedRotor(scanLog=Log('OJWHOIQFDAGZNF-UHFFFAOYSA-N_36by10.0_tor05_a1.log'), pivots=[1, 6], top=[6, 12, 13], fit='fourier'),
     HinderedRotor(scanLog=Log('OJWHOIQFDAGZNF-UHFFFAOYSA-N_36by10.0_tor04_a1.log'), pivots=[1, 5], top=[2, 3, 4, 5, 7, 8, 9, 10, 11], fit='fourier'),
     HinderedRotor(scanLog=Log('OJWHOIQFDAGZNF-UHFFFAOYSA-N_36by10.0_tor24_a1.log'), pivots=[3, 5], top=[1, 2, 5, 6, 12, 13], fit='fourier'),
     HinderedRotor(scanLog=Log('OJWHOIQFDAGZNF-UHFFFAOYSA-N_36by10.0_tor23_a1.log'), pivots=[3, 4], top=[4, 9, 10, 11], fit='fourier'),
]

