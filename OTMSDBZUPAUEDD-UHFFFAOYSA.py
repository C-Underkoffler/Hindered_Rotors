#!/usr/bin/env python
# -*- coding: utf-8 -*-

atoms = {
    'H': 6,
    'C': 2,
}

bonds = {
    'C-C': 1,
    'C-H': 6,
}

linear = False

externalSymmetry = 18.0

spinMultiplicity = 1

opticalIsomers = 1

energy = {
    'M06-2X/cc-pVTZ': Log('OTMSDBZUPAUEDD-UHFFFAOYSA.log'),
}

geometry = Log('OTMSDBZUPAUEDD-UHFFFAOYSA.log')

frequencies = Log('OTMSDBZUPAUEDD-UHFFFAOYSA.log')

rotors = []
