#!/usr/bin/env python
# -*- coding: utf-8 -*-

atoms = {
    'H': 10,
    'C': 4,
    'O': 1,
}

bonds = {
    'C-O': 1,
    'O-H': 1,
    'C-C': 3,
    'C-H': 9,
}

linear = False

externalSymmetry = 3.0

spinMultiplicity = 1

opticalIsomers = 1

energy = {
    'M06-2X/cc-pVTZ': Log('LRHPLDYGYMQRHN-UHFFFAOYSA-N_GeoFreq_a2.log'),
}

geometry = Log('LRHPLDYGYMQRHN-UHFFFAOYSA-N_GeoFreq_a2.log')

frequencies = Log('LRHPLDYGYMQRHN-UHFFFAOYSA-N_GeoFreq_a2.log')

rotors = [
     HinderedRotor(scanLog=Log('LRHPLDYGYMQRHN-UHFFFAOYSA-N_36by10.0_tor03_a2_F.log'), pivots=[1, 4], top=[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], fit='fourier'),
     HinderedRotor(scanLog=Log('LRHPLDYGYMQRHN-UHFFFAOYSA-N_36by10.0_tor12_a2_F.log'), pivots=[2, 3], top=[3, 5, 6, 7, 12, 13, 14], fit='fourier'),
     HinderedRotor(scanLog=Log('LRHPLDYGYMQRHN-UHFFFAOYSA-N_36by10.0_tor13_a2_F.log'), pivots=[2, 4], top=[1, 4, 10, 11, 15], fit='fourier'),
     HinderedRotor(scanLog=Log('LRHPLDYGYMQRHN-UHFFFAOYSA-N_36by10.0_tor24_a2_F.log'), pivots=[3, 5], top=[5, 12, 13, 14], fit='fourier'),
]

