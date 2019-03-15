#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('PWGWQRXHVJJRD-UHFFFAOYSA', 'PWGWQRXHVJJRD-UHFFFAOYSA.py')

statmech('PWGWQRXHVJJRD-UHFFFAOYSA')
thermo('PWGWQRXHVJJRD-UHFFFAOYSA', 'NASA')