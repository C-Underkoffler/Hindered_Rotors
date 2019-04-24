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

rotors = [
     HinderedRotor(scanLog=Log('XOBKSJJDNFUZPF-UHFFFAOYSA-N_36by-10.0_tor01_a1.log'), pivots=[1, 2], top=[2, 3, 5, 6, 7, 8, 9], fit='fourier'),
     HinderedRotor(scanLog=Log('XOBKSJJDNFUZPF-UHFFFAOYSA-N_36by-10.0_tor03_a1.log'), pivots=[1, 4], top=[4, 10, 11, 12], fit='fourier'),
     HinderedRotor(scanLog=Log('XOBKSJJDNFUZPF-UHFFFAOYSA-N_36by-10.0_tor12_a1.log'), pivots=[2, 3], top=[3, 7, 8, 9], fit='fourier'),
]

