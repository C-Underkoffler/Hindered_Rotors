#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('SXIFAEWF_bac', 'SXIFAEWFOJETOA-UHFFFAOYSA-N_ArkSpecies_backward.py')

statmech('SXIFAEWF_bac')
thermo('SXIFAEWF_bac', 'NASA')