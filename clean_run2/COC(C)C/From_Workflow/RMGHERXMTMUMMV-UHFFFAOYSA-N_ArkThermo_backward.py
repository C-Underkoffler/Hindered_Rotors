#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('RMGHERXM_bac', 'RMGHERXMTMUMMV-UHFFFAOYSA-N_ArkSpecies_backward.py')

statmech('RMGHERXM_bac')
thermo('RMGHERXM_bac', 'NASA')