#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('BWWHSGPVJDTLAO-UHFFFAOYSA', 'BWWHSGPVJDTLAO-UHFFFAOYSA.py')

statmech('BWWHSGPVJDTLAO-UHFFFAOYSA')
thermo('BWWHSGPVJDTLAO-UHFFFAOYSA', 'NASA')