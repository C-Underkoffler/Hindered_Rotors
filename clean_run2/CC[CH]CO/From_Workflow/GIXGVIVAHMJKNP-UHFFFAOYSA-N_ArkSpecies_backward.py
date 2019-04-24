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
    'M06-2X/cc-pVTZ': Log('GIXGVIVAHMJKNP-UHFFFAOYSA-N_GeoFreq_a2.log'),
}

geometry = Log('GIXGVIVAHMJKNP-UHFFFAOYSA-N_GeoFreq_a2.log')

frequencies = Log('GIXGVIVAHMJKNP-UHFFFAOYSA-N_GeoFreq_a2.log')

rotors = [
     HinderedRotor(scanLog=Log('GIXGVIVAHMJKNP-UHFFFAOYSA-N_36by-10.0_tor02_a2.log'), pivots=[1, 3], top=[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], fit='fourier'),
     HinderedRotor(scanLog=Log('GIXGVIVAHMJKNP-UHFFFAOYSA-N_36by-10.0_tor13_a2.log'), pivots=[2, 4], top=[4, 8, 9, 10], fit='fourier'),
     HinderedRotor(scanLog=Log('GIXGVIVAHMJKNP-UHFFFAOYSA-N_36by-10.0_tor14_a2.log'), pivots=[2, 5], top=[1, 3, 5, 11, 12, 13, 14], fit='fourier'),
     HinderedRotor(scanLog=Log('GIXGVIVAHMJKNP-UHFFFAOYSA-N_36by-10.0_tor24_a2.log'), pivots=[3, 5], top=[2, 4, 5, 6, 7, 8, 9, 10, 13], fit='fourier'),
]

