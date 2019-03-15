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

externalSymmetry = 54.0

spinMultiplicity = 2

opticalIsomers = 1

energy = {
    'M06-2X/cc-pVTZ': Log('VSQGJBCHGBRHMO-UHFFFAOYSA.log'),
}

geometry = Log('VSQGJBCHGBRHMO-UHFFFAOYSA.log')

frequencies = Log('VSQGJBCHGBRHMO-UHFFFAOYSA.log')

rotors = [
     HinderedRotor(scanLog=Log('/home/underkoffler.c/Code/Hindered_Rotors/clean_run2/CO[C](C)C/From_Workflow/VSQGJBCHGBRHMO-UHFFFAOYSA_tor03.log'), pivots=[1, 4], top=[4, 12, 13, 14], fit='fourier'),
     HinderedRotor(scanLog=Log('/home/underkoffler.c/Code/Hindered_Rotors/clean_run2/CO[C](C)C/From_Workflow/VSQGJBCHGBRHMO-UHFFFAOYSA_tor04.log'), pivots=[1, 5], top=[2, 3, 5, 6, 7, 8, 9, 10, 11], fit='fourier'),
     HinderedRotor(scanLog=Log('/home/underkoffler.c/Code/Hindered_Rotors/clean_run2/CO[C](C)C/From_Workflow/VSQGJBCHGBRHMO-UHFFFAOYSA_tor14.log'), pivots=[2, 5], top=[1, 3, 4, 5, 9, 10, 11, 12, 13, 14], fit='fourier'),
     HinderedRotor(scanLog=Log('/home/underkoffler.c/Code/Hindered_Rotors/clean_run2/CO[C](C)C/From_Workflow/VSQGJBCHGBRHMO-UHFFFAOYSA_tor24.log'), pivots=[3, 5], top=[1, 2, 4, 5, 6, 7, 8, 12, 13, 14], fit='fourier'),
]
