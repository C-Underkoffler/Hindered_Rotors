#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('JQCSUVJD_fix', 'JQCSUVJDBHJKNG-UHFFFAOYSA-N_ArkSpecies_fixed.py')

statmech('JQCSUVJD_fix')
thermo('JQCSUVJD_fix', 'NASA')