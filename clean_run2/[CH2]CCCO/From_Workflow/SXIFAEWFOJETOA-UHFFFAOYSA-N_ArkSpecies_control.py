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

externalSymmetry = 2.0

spinMultiplicity = 2

opticalIsomers = 1

energy = {
    'M06-2X/cc-pVTZ': Log('SXIFAEWFOJETOA-UHFFFAOYSA-N_GeoFreq_a1.log'),
}

geometry = Log('SXIFAEWFOJETOA-UHFFFAOYSA-N_GeoFreq_a1.log')

frequencies = Log('SXIFAEWFOJETOA-UHFFFAOYSA-N_GeoFreq_a1.log')

