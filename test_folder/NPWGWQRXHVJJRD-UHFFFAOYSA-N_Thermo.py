#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('NPWGWQRXHVJJRD-UHFFFAOYSA-N', 'NPWGWQRXHVJJRD-UHFFFAOYSA-N.py')

statmech('NPWGWQRXHVJJRD-UHFFFAOYSA-N')
thermo('NPWGWQRXHVJJRD-UHFFFAOYSA-N', 'NASA')