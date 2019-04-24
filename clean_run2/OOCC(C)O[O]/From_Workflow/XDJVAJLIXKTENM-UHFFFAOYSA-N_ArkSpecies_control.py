#!/usr/bin/env python
# -*- coding: utf-8 -*-

atoms = {
    'H': 7,
    'C': 3,
    'O': 4,
}

bonds = {
    'C-O': 2,
    'O-O': 2,
    'O-H': 1,
    'C-C': 2,
    'C-H': 6,
}

linear = False

externalSymmetry = 1.5

spinMultiplicity = 2

opticalIsomers = 1

energy = {
    'M06-2X/cc-pVTZ': Log('XDJVAJLIXKTENM-UHFFFAOYSA-N_GeoFreq_a1.log'),
}

geometry = Log('XDJVAJLIXKTENM-UHFFFAOYSA-N_GeoFreq_a1.log')

frequencies = Log('XDJVAJLIXKTENM-UHFFFAOYSA-N_GeoFreq_a1.log')

