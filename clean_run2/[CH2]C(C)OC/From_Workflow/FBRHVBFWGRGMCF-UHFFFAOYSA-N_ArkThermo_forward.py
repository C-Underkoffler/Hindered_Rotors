#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('FBRHVBFW_for', 'FBRHVBFWGRGMCF-UHFFFAOYSA-N_ArkSpecies_forward.py')

statmech('FBRHVBFW_for')
thermo('FBRHVBFW_for', 'NASA')