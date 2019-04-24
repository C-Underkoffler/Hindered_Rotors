#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('XOBKSJJD_con', 'XOBKSJJDNFUZPF-UHFFFAOYSA-N_ArkSpecies_control.py')

statmech('XOBKSJJD_con')
thermo('XOBKSJJD_con', 'NASA')