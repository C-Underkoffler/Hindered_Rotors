#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('TVFRQKHU_bac', 'TVFRQKHUZDMLDB-UHFFFAOYSA-N_ArkSpecies_backward.py')

statmech('TVFRQKHU_bac')
thermo('TVFRQKHU_bac', 'NASA')