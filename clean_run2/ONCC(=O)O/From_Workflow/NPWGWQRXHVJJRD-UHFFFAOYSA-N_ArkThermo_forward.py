#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('NPWGWQRX_for', 'NPWGWQRXHVJJRD-UHFFFAOYSA-N_ArkSpecies_forward.py')

statmech('NPWGWQRX_for')
thermo('NPWGWQRX_for', 'NASA')