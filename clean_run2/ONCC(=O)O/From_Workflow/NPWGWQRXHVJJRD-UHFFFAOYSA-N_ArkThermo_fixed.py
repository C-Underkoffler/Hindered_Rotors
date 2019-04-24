#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('NPWGWQRX_fix', 'NPWGWQRXHVJJRD-UHFFFAOYSA-N_ArkSpecies_fixed.py')

statmech('NPWGWQRX_fix')
thermo('NPWGWQRX_fix', 'NASA')