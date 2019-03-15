#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('RMGHERXMTMUMMV-UHFFFAOYSA', 'RMGHERXMTMUMMV-UHFFFAOYSA.py')

statmech('RMGHERXMTMUMMV-UHFFFAOYSA')
thermo('RMGHERXMTMUMMV-UHFFFAOYSA', 'NASA')