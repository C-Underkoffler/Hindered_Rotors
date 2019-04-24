#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('DUEVIJNW_for', 'DUEVIJNWLJUFDM-UHFFFAOYSA-N_ArkSpecies_forward.py')

statmech('DUEVIJNW_for')
thermo('DUEVIJNW_for', 'NASA')