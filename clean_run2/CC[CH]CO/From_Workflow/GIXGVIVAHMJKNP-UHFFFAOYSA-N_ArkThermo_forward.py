#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('GIXGVIVA_for', 'GIXGVIVAHMJKNP-UHFFFAOYSA-N_ArkSpecies_forward.py')

statmech('GIXGVIVA_for')
thermo('GIXGVIVA_for', 'NASA')