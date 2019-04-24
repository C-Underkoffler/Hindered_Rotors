#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('GIXGVIVA_con', 'GIXGVIVAHMJKNP-UHFFFAOYSA-N_ArkSpecies_control.py')

statmech('GIXGVIVA_con')
thermo('GIXGVIVA_con', 'NASA')