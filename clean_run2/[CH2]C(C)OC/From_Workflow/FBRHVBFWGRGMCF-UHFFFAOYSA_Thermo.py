#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('FBRHVBFWGRGMCF-UHFFFAOYSA', 'FBRHVBFWGRGMCF-UHFFFAOYSA.py')

statmech('FBRHVBFWGRGMCF-UHFFFAOYSA')
thermo('FBRHVBFWGRGMCF-UHFFFAOYSA', 'NASA')