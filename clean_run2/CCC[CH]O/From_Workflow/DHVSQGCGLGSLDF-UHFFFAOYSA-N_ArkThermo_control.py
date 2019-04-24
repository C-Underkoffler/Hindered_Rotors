#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('DHVSQGCG_con', 'DHVSQGCGLGSLDF-UHFFFAOYSA-N_ArkSpecies_control.py')

statmech('DHVSQGCG_con')
thermo('DHVSQGCG_con', 'NASA')