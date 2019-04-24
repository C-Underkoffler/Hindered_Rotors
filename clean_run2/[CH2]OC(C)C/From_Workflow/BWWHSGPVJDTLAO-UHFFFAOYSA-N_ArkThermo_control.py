#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('BWWHSGPV_con', 'BWWHSGPVJDTLAO-UHFFFAOYSA-N_ArkSpecies_control.py')

statmech('BWWHSGPV_con')
thermo('BWWHSGPV_con', 'NASA')