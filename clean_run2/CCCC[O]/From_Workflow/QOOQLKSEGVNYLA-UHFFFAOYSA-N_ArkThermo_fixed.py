#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('QOOQLKSE_fix', 'QOOQLKSEGVNYLA-UHFFFAOYSA-N_ArkSpecies_fixed.py')

statmech('QOOQLKSE_fix')
thermo('QOOQLKSE_fix', 'NASA')