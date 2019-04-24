#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('BWWHSGPV_bac', 'BWWHSGPVJDTLAO-UHFFFAOYSA-N_ArkSpecies_backward.py')

statmech('BWWHSGPV_bac')
thermo('BWWHSGPV_bac', 'NASA')