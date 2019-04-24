#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('RJUFJBKO_con', 'RJUFJBKOKNCXHH-UHFFFAOYSA-N_ArkSpecies_control.py')

statmech('RJUFJBKO_con')
thermo('RJUFJBKO_con', 'NASA')