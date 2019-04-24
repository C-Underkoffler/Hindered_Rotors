#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('RJUFJBKO_bac', 'RJUFJBKOKNCXHH-UHFFFAOYSA-N_ArkSpecies_backward.py')

statmech('RJUFJBKO_bac')
thermo('RJUFJBKO_bac', 'NASA')