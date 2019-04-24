#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('BWWHSGPV_fix', 'BWWHSGPVJDTLAO-UHFFFAOYSA-N_ArkSpecies_fixed.py')

statmech('BWWHSGPV_fix')
thermo('BWWHSGPV_fix', 'NASA')