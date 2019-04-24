#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('XOBKSJJD_fix', 'XOBKSJJDNFUZPF-UHFFFAOYSA-N_ArkSpecies_fixed.py')

statmech('XOBKSJJD_fix')
thermo('XOBKSJJD_fix', 'NASA')