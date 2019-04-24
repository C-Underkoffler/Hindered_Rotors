#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('SXIFAEWF_con', 'SXIFAEWFOJETOA-UHFFFAOYSA-N_ArkSpecies_control.py')

statmech('SXIFAEWF_con')
thermo('SXIFAEWF_con', 'NASA')