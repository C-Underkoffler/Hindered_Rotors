#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('DBQZVPSK_bac', 'DBQZVPSKYUCKNT-UHFFFAOYSA-N_ArkSpecies_backward.py')

statmech('DBQZVPSK_bac')
thermo('DBQZVPSK_bac', 'NASA')