#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('ZMAYDFGNKOVZRH-UHFFFAOYSA', 'ZMAYDFGNKOVZRH-UHFFFAOYSA.py')

statmech('ZMAYDFGNKOVZRH-UHFFFAOYSA')
thermo('ZMAYDFGNKOVZRH-UHFFFAOYSA', 'NASA')