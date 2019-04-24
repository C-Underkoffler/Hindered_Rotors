#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('DUEVIJNW_bac', 'DUEVIJNWLJUFDM-UHFFFAOYSA-N_ArkSpecies_backward.py')

statmech('DUEVIJNW_bac')
thermo('DUEVIJNW_bac', 'NASA')