#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('DUEVIJNW_con', 'DUEVIJNWLJUFDM-UHFFFAOYSA-N_ArkSpecies_control.py')

statmech('DUEVIJNW_con')
thermo('DUEVIJNW_con', 'NASA')