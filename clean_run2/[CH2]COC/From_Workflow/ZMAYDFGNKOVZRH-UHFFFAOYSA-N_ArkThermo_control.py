#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('ZMAYDFGN_con', 'ZMAYDFGNKOVZRH-UHFFFAOYSA-N_ArkSpecies_control.py')

statmech('ZMAYDFGN_con')
thermo('ZMAYDFGN_con', 'NASA')