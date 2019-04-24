#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('ZMAYDFGN_fix', 'ZMAYDFGNKOVZRH-UHFFFAOYSA-N_ArkSpecies_fixed.py')

statmech('ZMAYDFGN_fix')
thermo('ZMAYDFGN_fix', 'NASA')