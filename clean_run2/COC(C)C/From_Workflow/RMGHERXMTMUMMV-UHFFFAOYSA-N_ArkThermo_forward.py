#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('RMGHERXM_for', 'RMGHERXMTMUMMV-UHFFFAOYSA-N_ArkSpecies_forward.py')

statmech('RMGHERXM_for')
thermo('RMGHERXM_for', 'NASA')