#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('NPWGWQRX_con', 'NPWGWQRXHVJJRD-UHFFFAOYSA-N_ArkSpecies_control.py')

statmech('NPWGWQRX_con')
thermo('NPWGWQRX_con', 'NASA')