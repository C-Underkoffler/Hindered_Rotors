#!/usr/bin/env python
# -*- coding: utf-8 -*-

atoms = {
    'H': 5,
    'C': 2,
    'O': 3,
    'N': 1,
}

bonds = {
    'C-O': 1,
    'C-H': 2,
    'O-H': 2,
    'C-C': 1,
    'C=O': 1,
    'N-C': 1,
    'N-O': 1,
    'N-H': 1,
}

linear = False

externalSymmetry = 1.0

spinMultiplicity = 1

opticalIsomers = 1

energy = {
    'M06-2X/cc-pVTZ': Log('NPWGWQRXHVJJRD-UHFFFAOYSA-N_GeoFreq_a1.log'),
}

geometry = Log('NPWGWQRXHVJJRD-UHFFFAOYSA-N_GeoFreq_a1.log')

frequencies = Log('NPWGWQRXHVJJRD-UHFFFAOYSA-N_GeoFreq_a1.log')

