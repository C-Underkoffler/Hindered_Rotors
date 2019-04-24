#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('FBRHVBFW_con', 'FBRHVBFWGRGMCF-UHFFFAOYSA-N_ArkSpecies_control.py')

statmech('FBRHVBFW_con')
thermo('FBRHVBFW_con', 'NASA')