#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('BWWHSGPV_for', 'BWWHSGPVJDTLAO-UHFFFAOYSA-N_ArkSpecies_forward.py')

statmech('BWWHSGPV_for')
thermo('BWWHSGPV_for', 'NASA')