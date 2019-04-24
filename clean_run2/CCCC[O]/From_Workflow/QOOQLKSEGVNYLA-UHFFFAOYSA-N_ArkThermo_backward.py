#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('QOOQLKSE_bac', 'QOOQLKSEGVNYLA-UHFFFAOYSA-N_ArkSpecies_backward.py')

statmech('QOOQLKSE_bac')
thermo('QOOQLKSE_bac', 'NASA')