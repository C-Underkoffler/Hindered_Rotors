#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('RMGHERXM_fix', 'RMGHERXMTMUMMV-UHFFFAOYSA-N_ArkSpecies_fixed.py')

statmech('RMGHERXM_fix')
thermo('RMGHERXM_fix', 'NASA')