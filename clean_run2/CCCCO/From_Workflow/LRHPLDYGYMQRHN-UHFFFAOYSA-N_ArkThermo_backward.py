#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('LRHPLDYG_bac', 'LRHPLDYGYMQRHN-UHFFFAOYSA-N_ArkSpecies_backward.py')

statmech('LRHPLDYG_bac')
thermo('LRHPLDYG_bac', 'NASA')