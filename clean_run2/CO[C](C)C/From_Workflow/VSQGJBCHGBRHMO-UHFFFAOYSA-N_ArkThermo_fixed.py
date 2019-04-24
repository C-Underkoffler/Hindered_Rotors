#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('VSQGJBCH_fix', 'VSQGJBCHGBRHMO-UHFFFAOYSA-N_ArkSpecies_fixed.py')

statmech('VSQGJBCH_fix')
thermo('VSQGJBCH_fix', 'NASA')