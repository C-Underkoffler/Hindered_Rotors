#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('VSQGJBCH_for', 'VSQGJBCHGBRHMO-UHFFFAOYSA-N_ArkSpecies_forward.py')

statmech('VSQGJBCH_for')
thermo('VSQGJBCH_for', 'NASA')