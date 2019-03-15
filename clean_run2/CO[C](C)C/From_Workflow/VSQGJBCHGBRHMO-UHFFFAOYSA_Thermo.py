#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('VSQGJBCHGBRHMO-UHFFFAOYSA', 'VSQGJBCHGBRHMO-UHFFFAOYSA.py')

statmech('VSQGJBCHGBRHMO-UHFFFAOYSA')
thermo('VSQGJBCHGBRHMO-UHFFFAOYSA', 'NASA')