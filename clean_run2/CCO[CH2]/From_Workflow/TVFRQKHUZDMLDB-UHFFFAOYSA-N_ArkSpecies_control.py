#!/usr/bin/env python
# -*- coding: utf-8 -*-

atoms = {
    'H': 7,
    'C': 3,
    'O': 1,
}

bonds = {
    'C-O': 2,
    'C-C': 1,
    'C-H': 7,
}

linear = False

externalSymmetry = 6.0

spinMultiplicity = 2

opticalIsomers = 1

energy = {
    'M06-2X/cc-pVTZ': Log('TVFRQKHUZDMLDB-UHFFFAOYSA-N_GeoFreq_a2.log'),
}

geometry = Log('TVFRQKHUZDMLDB-UHFFFAOYSA-N_GeoFreq_a2.log')

frequencies = Log('TVFRQKHUZDMLDB-UHFFFAOYSA-N_GeoFreq_a2.log')

