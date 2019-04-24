#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('LRHPLDYG_fix', 'LRHPLDYGYMQRHN-UHFFFAOYSA-N_ArkSpecies_fixed.py')

statmech('LRHPLDYG_fix')
thermo('LRHPLDYG_fix', 'NASA')