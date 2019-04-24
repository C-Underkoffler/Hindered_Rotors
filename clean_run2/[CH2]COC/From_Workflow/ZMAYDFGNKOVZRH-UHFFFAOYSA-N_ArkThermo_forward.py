#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('ZMAYDFGN_for', 'ZMAYDFGNKOVZRH-UHFFFAOYSA-N_ArkSpecies_forward.py')

statmech('ZMAYDFGN_for')
thermo('ZMAYDFGN_for', 'NASA')