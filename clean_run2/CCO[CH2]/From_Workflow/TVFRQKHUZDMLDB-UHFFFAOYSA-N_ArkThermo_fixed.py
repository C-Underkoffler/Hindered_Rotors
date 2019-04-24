#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('TVFRQKHU_fix', 'TVFRQKHUZDMLDB-UHFFFAOYSA-N_ArkSpecies_fixed.py')

statmech('TVFRQKHU_fix')
thermo('TVFRQKHU_fix', 'NASA')