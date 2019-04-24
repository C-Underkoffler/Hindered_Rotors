#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('GIXGVIVA_bac', 'GIXGVIVAHMJKNP-UHFFFAOYSA-N_ArkSpecies_backward.py')

statmech('GIXGVIVA_bac')
thermo('GIXGVIVA_bac', 'NASA')