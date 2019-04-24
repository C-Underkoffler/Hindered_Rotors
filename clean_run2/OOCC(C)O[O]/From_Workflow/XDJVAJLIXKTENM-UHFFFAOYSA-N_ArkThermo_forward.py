#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('XDJVAJLI_for', 'XDJVAJLIXKTENM-UHFFFAOYSA-N_ArkSpecies_forward.py')

statmech('XDJVAJLI_for')
thermo('XDJVAJLI_for', 'NASA')