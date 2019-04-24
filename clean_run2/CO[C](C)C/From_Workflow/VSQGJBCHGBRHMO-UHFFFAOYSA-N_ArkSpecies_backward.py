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

externalSymmetry = 54.0

spinMultiplicity = 2

opticalIsomers = 1

energy = {
    'M06-2X/cc-pVTZ': Log('VSQGJBCHGBRHMO-UHFFFAOYSA-N_GeoFreq_a1.log'),
}

geometry = Log('VSQGJBCHGBRHMO-UHFFFAOYSA-N_GeoFreq_a1.log')

frequencies = Log('VSQGJBCHGBRHMO-UHFFFAOYSA-N_GeoFreq_a1.log')

rotors = [
     HinderedRotor(scanLog=Log('VSQGJBCHGBRHMO-UHFFFAOYSA-N_36by-10.0_tor04_a1.log'), pivots=[1, 5], top=[2, 3, 5, 6, 7, 8, 9, 10, 11], fit='fourier'),
     HinderedRotor(scanLog=Log('VSQGJBCHGBRHMO-UHFFFAOYSA-N_36by-10.0_tor03_a1.log'), pivots=[1, 4], top=[4, 12, 13, 14], fit='fourier'),
     HinderedRotor(scanLog=Log('VSQGJBCHGBRHMO-UHFFFAOYSA-N_36by-10.0_tor14_a1.log'), pivots=[2, 5], top=[1, 3, 4, 5, 9, 10, 11, 12, 13, 14], fit='fourier'),
     HinderedRotor(scanLog=Log('VSQGJBCHGBRHMO-UHFFFAOYSA-N_36by-10.0_tor24_a1.log'), pivots=[3, 5], top=[1, 2, 4, 5, 6, 7, 8, 12, 13, 14], fit='fourier'),
]

