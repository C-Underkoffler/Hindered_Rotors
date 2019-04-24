#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('ZMAYDFGN_bac', 'ZMAYDFGNKOVZRH-UHFFFAOYSA-N_ArkSpecies_backward.py')

statmech('ZMAYDFGN_bac')
thermo('ZMAYDFGN_bac', 'NASA')