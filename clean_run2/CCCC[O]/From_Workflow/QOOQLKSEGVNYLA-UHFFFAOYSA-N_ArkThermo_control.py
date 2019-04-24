#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('QOOQLKSE_con', 'QOOQLKSEGVNYLA-UHFFFAOYSA-N_ArkSpecies_control.py')

statmech('QOOQLKSE_con')
thermo('QOOQLKSE_con', 'NASA')