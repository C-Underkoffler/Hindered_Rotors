#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('VSQGJBCH_con', 'VSQGJBCHGBRHMO-UHFFFAOYSA-N_ArkSpecies_control.py')

statmech('VSQGJBCH_con')
thermo('VSQGJBCH_con', 'NASA')