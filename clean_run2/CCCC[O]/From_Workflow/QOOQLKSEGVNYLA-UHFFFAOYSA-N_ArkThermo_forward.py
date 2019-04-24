#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('QOOQLKSE_for', 'QOOQLKSEGVNYLA-UHFFFAOYSA-N_ArkSpecies_forward.py')

statmech('QOOQLKSE_for')
thermo('QOOQLKSE_for', 'NASA')