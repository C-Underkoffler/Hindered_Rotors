#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('DUEVIJNW_fix', 'DUEVIJNWLJUFDM-UHFFFAOYSA-N_ArkSpecies_fixed.py')

statmech('DUEVIJNW_fix')
thermo('DUEVIJNW_fix', 'NASA')