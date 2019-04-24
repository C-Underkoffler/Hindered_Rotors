#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('DHVSQGCG_fix', 'DHVSQGCGLGSLDF-UHFFFAOYSA-N_ArkSpecies_fixed.py')

statmech('DHVSQGCG_fix')
thermo('DHVSQGCG_fix', 'NASA')