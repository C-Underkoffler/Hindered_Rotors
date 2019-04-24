#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('SXIFAEWF_for', 'SXIFAEWFOJETOA-UHFFFAOYSA-N_ArkSpecies_forward.py')

statmech('SXIFAEWF_for')
thermo('SXIFAEWF_for', 'NASA')