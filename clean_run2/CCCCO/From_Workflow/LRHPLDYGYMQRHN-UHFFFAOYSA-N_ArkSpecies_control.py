#!/usr/bin/env python
# -*- coding: utf-8 -*-

atoms = {
    'H': 10,
    'C': 4,
    'O': 1,
}

bonds = {
    'C-O': 1,
    'O-H': 1,
    'C-C': 3,
    'C-H': 9,
}

linear = False

externalSymmetry = 3.0

spinMultiplicity = 1

opticalIsomers = 1

energy = {
    'M06-2X/cc-pVTZ': Log('LRHPLDYGYMQRHN-UHFFFAOYSA-N_GeoFreq_a2.log'),
}

geometry = Log('LRHPLDYGYMQRHN-UHFFFAOYSA-N_GeoFreq_a2.log')

frequencies = Log('LRHPLDYGYMQRHN-UHFFFAOYSA-N_GeoFreq_a2.log')

