#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('XDJVAJLI_con', 'XDJVAJLIXKTENM-UHFFFAOYSA-N_ArkSpecies_control.py')

statmech('XDJVAJLI_con')
thermo('XDJVAJLI_con', 'NASA')