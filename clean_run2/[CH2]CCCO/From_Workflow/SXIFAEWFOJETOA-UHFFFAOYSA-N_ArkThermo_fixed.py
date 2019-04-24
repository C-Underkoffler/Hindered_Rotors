#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('SXIFAEWF_fix', 'SXIFAEWFOJETOA-UHFFFAOYSA-N_ArkSpecies_fixed.py')

statmech('SXIFAEWF_fix')
thermo('SXIFAEWF_fix', 'NASA')