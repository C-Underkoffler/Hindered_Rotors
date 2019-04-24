#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('FBRHVBFW_bac', 'FBRHVBFWGRGMCF-UHFFFAOYSA-N_ArkSpecies_backward.py')

statmech('FBRHVBFW_bac')
thermo('FBRHVBFW_bac', 'NASA')