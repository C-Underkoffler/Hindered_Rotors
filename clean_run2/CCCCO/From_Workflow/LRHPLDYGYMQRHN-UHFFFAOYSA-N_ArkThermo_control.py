#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('LRHPLDYG_con', 'LRHPLDYGYMQRHN-UHFFFAOYSA-N_ArkSpecies_control.py')

statmech('LRHPLDYG_con')
thermo('LRHPLDYG_con', 'NASA')