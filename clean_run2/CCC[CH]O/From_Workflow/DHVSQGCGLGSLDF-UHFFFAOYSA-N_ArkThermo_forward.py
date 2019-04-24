#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('DHVSQGCG_for', 'DHVSQGCGLGSLDF-UHFFFAOYSA-N_ArkSpecies_forward.py')

statmech('DHVSQGCG_for')
thermo('DHVSQGCG_for', 'NASA')