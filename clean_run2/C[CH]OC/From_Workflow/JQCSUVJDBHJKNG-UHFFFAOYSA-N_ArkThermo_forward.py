#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('JQCSUVJD_for', 'JQCSUVJDBHJKNG-UHFFFAOYSA-N_ArkSpecies_forward.py')

statmech('JQCSUVJD_for')
thermo('JQCSUVJD_for', 'NASA')