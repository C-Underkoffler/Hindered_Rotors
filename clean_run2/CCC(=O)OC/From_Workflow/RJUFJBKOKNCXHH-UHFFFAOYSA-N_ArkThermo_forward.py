#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('RJUFJBKO_for', 'RJUFJBKOKNCXHH-UHFFFAOYSA-N_ArkSpecies_forward.py')

statmech('RJUFJBKO_for')
thermo('RJUFJBKO_for', 'NASA')