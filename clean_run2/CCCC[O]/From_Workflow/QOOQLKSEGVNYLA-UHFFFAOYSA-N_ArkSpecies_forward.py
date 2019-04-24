#!/usr/bin/env python
# -*- coding: utf-8 -*-

atoms = {
    'H': 9,
    'C': 4,
    'O': 1,
}

bonds = {
    'C-O': 1,
    'C-C': 3,
    'C-H': 9,
}

linear = False

externalSymmetry = 3.0

spinMultiplicity = 2

opticalIsomers = 1

energy = {
    'M06-2X/cc-pVTZ': Log('QOOQLKSEGVNYLA-UHFFFAOYSA-N_GeoFreq_a1.log'),
}

geometry = Log('QOOQLKSEGVNYLA-UHFFFAOYSA-N_GeoFreq_a1.log')

frequencies = Log('QOOQLKSEGVNYLA-UHFFFAOYSA-N_GeoFreq_a1.log')

rotors = [
     HinderedRotor(scanLog=Log('QOOQLKSEGVNYLA-UHFFFAOYSA-N_36by10.0_tor12_a1.log'), pivots=[2, 3], top=[1, 3, 5, 8, 9, 13, 14], fit='fourier'),
     HinderedRotor(scanLog=Log('QOOQLKSEGVNYLA-UHFFFAOYSA-N_36by10.0_tor24_a1.log'), pivots=[3, 5], top=[1, 5, 13, 14], fit='fourier'),
]

