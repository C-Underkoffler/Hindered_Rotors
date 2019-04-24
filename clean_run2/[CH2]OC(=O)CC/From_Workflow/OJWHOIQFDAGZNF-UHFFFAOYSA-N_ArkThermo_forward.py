#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('OJWHOIQF_for', 'OJWHOIQFDAGZNF-UHFFFAOYSA-N_ArkSpecies_forward.py')

statmech('OJWHOIQF_for')
thermo('OJWHOIQF_for', 'NASA')