#!/usr/bin/env python
# -*- coding: utf-8 -*-

atoms = {
    'H': 8,
    'C': 3,
    'O': 1,
}

bonds = {
    'C-O': 2,
    'C-C': 1,
    'C-H': 8,
}

linear = False

externalSymmetry = 9.0

spinMultiplicity = 1

opticalIsomers = 1

energy = {
    'M06-2X/cc-pVTZ': Log('XOBKSJJDNFUZPF-UHFFFAOYSA-N_GeoFreq_a1.log'),
}

geometry = Log('XOBKSJJDNFUZPF-UHFFFAOYSA-N_GeoFreq_a1.log')

frequencies = Log('XOBKSJJDNFUZPF-UHFFFAOYSA-N_GeoFreq_a1.log')

