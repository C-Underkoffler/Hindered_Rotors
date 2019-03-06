#!/usr/bin/env python
# -*- coding: utf-8 -*-

atoms = {
    'H': 12,
    'C': 5,
    'O': 2,
}

bonds = {
    'C-O': 3,
    'O-H': 1,
    'C-C': 3,
    'C-H': 11,
}

linear = False

externalSymmetry = 27.0

spinMultiplicity = 1

opticalIsomers = 1

energy = {
    'M06-2X/cc-pVTZ': Log('VMPUAIZSESMILD-UHFFFAOYSA-N_Freq.log'),
}

geometry = Log('VMPUAIZSESMILD-UHFFFAOYSA-N_Freq.log')

frequencies = Log('VMPUAIZSESMILD-UHFFFAOYSA-N_Freq.log')

rotors = [
     HinderedRotor(scanLog=Log('VMPUAIZSESMILD-UHFFFAOYSA-N_tor34.log'), pivots=[3, 4], top=[19, 2, 4, 8, 9], fit='fourier'),
]