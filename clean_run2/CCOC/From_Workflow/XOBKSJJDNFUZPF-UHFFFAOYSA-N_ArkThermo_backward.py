#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('XOBKSJJD_bac', 'XOBKSJJDNFUZPF-UHFFFAOYSA-N_ArkSpecies_backward.py')

statmech('XOBKSJJD_bac')
thermo('XOBKSJJD_bac', 'NASA')