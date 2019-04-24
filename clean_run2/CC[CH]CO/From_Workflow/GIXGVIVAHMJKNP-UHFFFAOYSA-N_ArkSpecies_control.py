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

