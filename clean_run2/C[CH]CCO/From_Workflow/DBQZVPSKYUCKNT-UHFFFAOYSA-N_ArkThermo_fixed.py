#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('DBQZVPSK_fix', 'DBQZVPSKYUCKNT-UHFFFAOYSA-N_ArkSpecies_fixed.py')

statmech('DBQZVPSK_fix')
thermo('DBQZVPSK_fix', 'NASA')