#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('DBQZVPSK_for', 'DBQZVPSKYUCKNT-UHFFFAOYSA-N_ArkSpecies_forward.py')

statmech('DBQZVPSK_for')
thermo('DBQZVPSK_for', 'NASA')