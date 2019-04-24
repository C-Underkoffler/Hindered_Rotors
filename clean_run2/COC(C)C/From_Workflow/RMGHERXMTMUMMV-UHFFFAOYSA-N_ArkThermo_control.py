#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('RMGHERXM_con', 'RMGHERXMTMUMMV-UHFFFAOYSA-N_ArkSpecies_control.py')

statmech('RMGHERXM_con')
thermo('RMGHERXM_con', 'NASA')