#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('LRHPLDYG_for', 'LRHPLDYGYMQRHN-UHFFFAOYSA-N_ArkSpecies_forward.py')

statmech('LRHPLDYG_for')
thermo('LRHPLDYG_for', 'NASA')