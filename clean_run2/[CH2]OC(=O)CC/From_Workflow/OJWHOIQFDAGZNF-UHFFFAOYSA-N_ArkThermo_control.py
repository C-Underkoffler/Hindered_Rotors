#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('OJWHOIQF_con', 'OJWHOIQFDAGZNF-UHFFFAOYSA-N_ArkSpecies_control.py')

statmech('OJWHOIQF_con')
thermo('OJWHOIQF_con', 'NASA')