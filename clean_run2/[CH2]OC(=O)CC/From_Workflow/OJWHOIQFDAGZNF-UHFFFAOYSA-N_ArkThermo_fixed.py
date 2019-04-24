#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('OJWHOIQF_fix', 'OJWHOIQFDAGZNF-UHFFFAOYSA-N_ArkSpecies_fixed.py')

statmech('OJWHOIQF_fix')
thermo('OJWHOIQF_fix', 'NASA')