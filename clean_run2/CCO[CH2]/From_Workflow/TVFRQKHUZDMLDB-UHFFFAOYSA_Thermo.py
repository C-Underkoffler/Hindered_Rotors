#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('TVFRQKHUZDMLDB-UHFFFAOYSA', 'TVFRQKHUZDMLDB-UHFFFAOYSA.py')

statmech('TVFRQKHUZDMLDB-UHFFFAOYSA')
thermo('TVFRQKHUZDMLDB-UHFFFAOYSA', 'NASA')