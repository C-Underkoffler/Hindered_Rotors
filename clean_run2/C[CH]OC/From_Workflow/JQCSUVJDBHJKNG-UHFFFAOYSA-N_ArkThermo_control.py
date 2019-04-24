#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('JQCSUVJD_con', 'JQCSUVJDBHJKNG-UHFFFAOYSA-N_ArkSpecies_control.py')

statmech('JQCSUVJD_con')
thermo('JQCSUVJD_con', 'NASA')