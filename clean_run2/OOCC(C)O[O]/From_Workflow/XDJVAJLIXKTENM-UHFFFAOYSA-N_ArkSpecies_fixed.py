#!/usr/bin/env python
# -*- coding: utf-8 -*-

atoms = {
    'H': 7,
    'C': 3,
    'O': 4,
}

bonds = {
    'C-O': 2,
    'O-O': 2,
    'O-H': 1,
    'C-C': 2,
    'C-H': 6,
}

linear = False

externalSymmetry = 1.5

spinMultiplicity = 2

opticalIsomers = 1

energy = {
    'M06-2X/cc-pVTZ': Log('XDJVAJLIXKTENM-UHFFFAOYSA-N_GeoFreq_a1.log'),
}

geometry = Log('XDJVAJLIXKTENM-UHFFFAOYSA-N_GeoFreq_a1.log')

frequencies = Log('XDJVAJLIXKTENM-UHFFFAOYSA-N_GeoFreq_a1.log')

rotors = [
     HinderedRotor(scanLog=Log('XDJVAJLIXKTENM-UHFFFAOYSA-N_36by10.0_tor05_a1_F.log'), pivots=[1, 6], top=[2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], fit='fourier'),
     HinderedRotor(scanLog=Log('XDJVAJLIXKTENM-UHFFFAOYSA-N_36by10.0_tor02_a1_F.log'), pivots=[1, 3], top=[3, 14], fit='fourier'),
     HinderedRotor(scanLog=Log('XDJVAJLIXKTENM-UHFFFAOYSA-N_36by10.0_tor14_a1_F.log'), pivots=[2, 5], top=[1, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], fit='fourier'),
     HinderedRotor(scanLog=Log('XDJVAJLIXKTENM-UHFFFAOYSA-N_36by10.0_tor45_a1_F.log'), pivots=[5, 6], top=[1, 3, 6, 9, 10, 14], fit='fourier'),
     HinderedRotor(scanLog=Log('XDJVAJLIXKTENM-UHFFFAOYSA-N_36by10.0_tor46_a1_F.log'), pivots=[5, 7], top=[7, 11, 12, 13], fit='fourier'),
]

