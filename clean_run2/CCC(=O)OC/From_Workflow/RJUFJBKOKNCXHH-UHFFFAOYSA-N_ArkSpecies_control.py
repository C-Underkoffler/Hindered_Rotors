#!/usr/bin/env python
# -*- coding: utf-8 -*-

atoms = {
    'H': 8,
    'C': 4,
    'O': 2,
}

bonds = {
    'C=O': 1,
    'C-O': 2,
    'C-C': 2,
    'C-H': 8,
}

linear = False

externalSymmetry = 9.0

spinMultiplicity = 1

opticalIsomers = 1

energy = {
    'M06-2X/cc-pVTZ': Log('RJUFJBKOKNCXHH-UHFFFAOYSA-N_GeoFreq_a1.log'),
}

geometry = Log('RJUFJBKOKNCXHH-UHFFFAOYSA-N_GeoFreq_a1.log')

frequencies = Log('RJUFJBKOKNCXHH-UHFFFAOYSA-N_GeoFreq_a1.log')

