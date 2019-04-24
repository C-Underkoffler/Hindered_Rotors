#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('XDJVAJLI_bac', 'XDJVAJLIXKTENM-UHFFFAOYSA-N_ArkSpecies_backward.py')

statmech('XDJVAJLI_bac')
thermo('XDJVAJLI_bac', 'NASA')