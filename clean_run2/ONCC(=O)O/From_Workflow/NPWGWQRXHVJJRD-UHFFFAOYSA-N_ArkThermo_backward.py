#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('NPWGWQRX_bac', 'NPWGWQRXHVJJRD-UHFFFAOYSA-N_ArkSpecies_backward.py')

statmech('NPWGWQRX_bac')
thermo('NPWGWQRX_bac', 'NASA')