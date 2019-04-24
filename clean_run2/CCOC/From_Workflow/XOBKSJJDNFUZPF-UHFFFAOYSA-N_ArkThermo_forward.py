#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('XOBKSJJD_for', 'XOBKSJJDNFUZPF-UHFFFAOYSA-N_ArkSpecies_forward.py')

statmech('XOBKSJJD_for')
thermo('XOBKSJJD_for', 'NASA')