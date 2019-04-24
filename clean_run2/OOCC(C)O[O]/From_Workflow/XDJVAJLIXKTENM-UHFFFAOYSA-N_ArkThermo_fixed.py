#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('XDJVAJLI_fix', 'XDJVAJLIXKTENM-UHFFFAOYSA-N_ArkSpecies_fixed.py')

statmech('XDJVAJLI_fix')
thermo('XDJVAJLI_fix', 'NASA')