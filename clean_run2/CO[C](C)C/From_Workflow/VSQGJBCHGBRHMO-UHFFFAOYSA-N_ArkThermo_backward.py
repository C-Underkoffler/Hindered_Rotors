#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('VSQGJBCH_bac', 'VSQGJBCHGBRHMO-UHFFFAOYSA-N_ArkSpecies_backward.py')

statmech('VSQGJBCH_bac')
thermo('VSQGJBCH_bac', 'NASA')