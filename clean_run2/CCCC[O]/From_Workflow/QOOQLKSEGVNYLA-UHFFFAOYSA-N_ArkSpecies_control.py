#!/usr/bin/env python
# -*- coding: utf-8 -*-

atoms = {
    'H': 9,
    'C': 4,
    'O': 1,
}

bonds = {
    'C-O': 1,
    'C-C': 3,
    'C-H': 9,
}

linear = False

externalSymmetry = 3.0

spinMultiplicity = 2

opticalIsomers = 1

energy = {
    'M06-2X/cc-pVTZ': Log('QOOQLKSEGVNYLA-UHFFFAOYSA-N_GeoFreq_a1.log'),
}

geometry = Log('QOOQLKSEGVNYLA-UHFFFAOYSA-N_GeoFreq_a1.log')

frequencies = Log('QOOQLKSEGVNYLA-UHFFFAOYSA-N_GeoFreq_a1.log')

