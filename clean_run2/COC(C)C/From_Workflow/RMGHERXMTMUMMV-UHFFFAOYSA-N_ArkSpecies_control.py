#!/usr/bin/env python
# -*- coding: utf-8 -*-

atoms = {
    'H': 10,
    'C': 4,
    'O': 1,
}

bonds = {
    'C-O': 2,
    'C-C': 2,
    'C-H': 10,
}

linear = False

externalSymmetry = 27.0

spinMultiplicity = 1

opticalIsomers = 1

energy = {
    'M06-2X/cc-pVTZ': Log('RMGHERXMTMUMMV-UHFFFAOYSA-N_GeoFreq_a1.log'),
}

geometry = Log('RMGHERXMTMUMMV-UHFFFAOYSA-N_GeoFreq_a1.log')

frequencies = Log('RMGHERXMTMUMMV-UHFFFAOYSA-N_GeoFreq_a1.log')

