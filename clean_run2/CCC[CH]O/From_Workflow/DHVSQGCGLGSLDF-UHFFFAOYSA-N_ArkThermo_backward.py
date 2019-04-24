#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('DHVSQGCG_bac', 'DHVSQGCGLGSLDF-UHFFFAOYSA-N_ArkSpecies_backward.py')

statmech('DHVSQGCG_bac')
thermo('DHVSQGCG_bac', 'NASA')