#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('FBRHVBFW_fix', 'FBRHVBFWGRGMCF-UHFFFAOYSA-N_ArkSpecies_fixed.py')

statmech('FBRHVBFW_fix')
thermo('FBRHVBFW_fix', 'NASA')