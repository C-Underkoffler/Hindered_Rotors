#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('TVFRQKHU_for', 'TVFRQKHUZDMLDB-UHFFFAOYSA-N_ArkSpecies_forward.py')

statmech('TVFRQKHU_for')
thermo('TVFRQKHU_for', 'NASA')