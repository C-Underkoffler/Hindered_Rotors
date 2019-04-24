#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('OJWHOIQF_bac', 'OJWHOIQFDAGZNF-UHFFFAOYSA-N_ArkSpecies_backward.py')

statmech('OJWHOIQF_bac')
thermo('OJWHOIQF_bac', 'NASA')