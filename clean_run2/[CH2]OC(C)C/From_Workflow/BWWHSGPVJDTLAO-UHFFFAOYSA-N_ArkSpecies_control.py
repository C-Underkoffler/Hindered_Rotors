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

externalSymmetry = 18.0

spinMultiplicity = 2

opticalIsomers = 1

energy = {
    'M06-2X/cc-pVTZ': Log('BWWHSGPVJDTLAO-UHFFFAOYSA-N_GeoFreq_a1.log'),
}

geometry = Log('BWWHSGPVJDTLAO-UHFFFAOYSA-N_GeoFreq_a1.log')

frequencies = Log('BWWHSGPVJDTLAO-UHFFFAOYSA-N_GeoFreq_a1.log')

