#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('DBQZVPSK_con', 'DBQZVPSKYUCKNT-UHFFFAOYSA-N_ArkSpecies_control.py')

statmech('DBQZVPSK_con')
thermo('DBQZVPSK_con', 'NASA')