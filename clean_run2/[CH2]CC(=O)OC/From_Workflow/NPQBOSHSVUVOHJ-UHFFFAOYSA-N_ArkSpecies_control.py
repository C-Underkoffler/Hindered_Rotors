#!/usr/bin/env python
# -*- coding: utf-8 -*-

atoms = {
    'H': 7,
    'C': 4,
    'O': 2,
}

bonds = {
    'C=O': 1,
    'C-O': 2,
    'C-C': 2,
    'C-H': 7,
}

linear = False

externalSymmetry = 6.0

spinMultiplicity = 2

opticalIsomers = 1

energy = {
    'M06-2X/cc-pVTZ': Log('NPQBOSHSVUVOHJ-UHFFFAOYSA-N_GeoFreq_a2.log'),
}

geometry = Log('NPQBOSHSVUVOHJ-UHFFFAOYSA-N_GeoFreq_a2.log')

frequencies = Log('NPQBOSHSVUVOHJ-UHFFFAOYSA-N_GeoFreq_a2.log')

