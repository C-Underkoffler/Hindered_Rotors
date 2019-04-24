#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('GIXGVIVA_fix', 'GIXGVIVAHMJKNP-UHFFFAOYSA-N_ArkSpecies_fixed.py')

statmech('GIXGVIVA_fix')
thermo('GIXGVIVA_fix', 'NASA')