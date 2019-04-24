#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('RJUFJBKO_fix', 'RJUFJBKOKNCXHH-UHFFFAOYSA-N_ArkSpecies_fixed.py')

statmech('RJUFJBKO_fix')
thermo('RJUFJBKO_fix', 'NASA')