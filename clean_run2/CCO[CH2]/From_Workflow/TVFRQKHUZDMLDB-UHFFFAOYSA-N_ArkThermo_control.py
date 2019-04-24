#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('TVFRQKHU_con', 'TVFRQKHUZDMLDB-UHFFFAOYSA-N_ArkSpecies_control.py')

statmech('TVFRQKHU_con')
thermo('TVFRQKHU_con', 'NASA')