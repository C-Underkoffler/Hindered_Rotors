#!/usr/bin/env python
# -*- coding: utf-8 -*-

atoms = {
    'H': 7,
    'C': 4,
    'O': 2,
}

bonds = {
    'C=O': 1,
    'C-O': 2,
    'C-C': 2,
    'C-H': 7,
}

linear = False

externalSymmetry = 6.0

spinMultiplicity = 2

opticalIsomers = 1

energy = {
    'M06-2X/cc-pVTZ': Log('NPQBOSHSVUVOHJ-UHFFFAOYSA-N_GeoFreq_a2.log'),
}

geometry = Log('NPQBOSHSVUVOHJ-UHFFFAOYSA-N_GeoFreq_a2.log')

frequencies = Log('NPQBOSHSVUVOHJ-UHFFFAOYSA-N_GeoFreq_a2.log')

rotors = [
     HinderedRotor(scanLog=Log('NPQBOSHSVUVOHJ-UHFFFAOYSA-N_36by-10.0_tor04_a2.log'), pivots=[1, 5], top=[2, 3, 5, 6, 7, 8, 12, 13], fit='fourier'),
     HinderedRotor(scanLog=Log('NPQBOSHSVUVOHJ-UHFFFAOYSA-N_36by-10.0_tor03_a2.log'), pivots=[1, 4], top=[4, 9, 10, 11], fit='fourier'),
     HinderedRotor(scanLog=Log('NPQBOSHSVUVOHJ-UHFFFAOYSA-N_36by-10.0_tor25_a2.log'), pivots=[3, 6], top=[6, 12, 13], fit='fourier'),
     HinderedRotor(scanLog=Log('NPQBOSHSVUVOHJ-UHFFFAOYSA-N_36by-10.0_tor24_a2.log'), pivots=[3, 5], top=[1, 2, 4, 5, 9, 10, 11], fit='fourier'),
]

