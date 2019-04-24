#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('JQCSUVJD_bac', 'JQCSUVJDBHJKNG-UHFFFAOYSA-N_ArkSpecies_backward.py')

statmech('JQCSUVJD_bac')
thermo('JQCSUVJD_bac', 'NASA')