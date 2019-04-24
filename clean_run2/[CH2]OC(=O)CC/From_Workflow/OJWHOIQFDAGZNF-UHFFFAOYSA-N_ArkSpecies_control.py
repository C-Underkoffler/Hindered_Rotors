#!/usr/bin/env python
# -*- coding: utf-8 -*-

atoms = {
    'H': 7,
    'C': 4,
    'O': 2,
}

bonds = {
    'C-O': 2,
    'C=O': 1,
    'C-C': 2,
    'C-H': 7,
}

linear = False

externalSymmetry = 6.0

spinMultiplicity = 2

opticalIsomers = 1

energy = {
    'M06-2X/cc-pVTZ': Log('OJWHOIQFDAGZNF-UHFFFAOYSA-N_GeoFreq_a1.log'),
}

geometry = Log('OJWHOIQFDAGZNF-UHFFFAOYSA-N_GeoFreq_a1.log')

frequencies = Log('OJWHOIQFDAGZNF-UHFFFAOYSA-N_GeoFreq_a1.log')

