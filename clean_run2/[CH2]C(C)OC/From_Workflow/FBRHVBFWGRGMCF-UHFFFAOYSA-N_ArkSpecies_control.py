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

externalSymmetry = 9.0

spinMultiplicity = 2

opticalIsomers = 1

energy = {
    'M06-2X/cc-pVTZ': Log('FBRHVBFWGRGMCF-UHFFFAOYSA-N_GeoFreq_a2.log'),
}

geometry = Log('FBRHVBFWGRGMCF-UHFFFAOYSA-N_GeoFreq_a2.log')

frequencies = Log('FBRHVBFWGRGMCF-UHFFFAOYSA-N_GeoFreq_a2.log')

