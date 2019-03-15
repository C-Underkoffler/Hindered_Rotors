#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('DUEVIJNWLJUFDM-UHFFFAOYSA', 'DUEVIJNWLJUFDM-UHFFFAOYSA.py')

statmech('DUEVIJNWLJUFDM-UHFFFAOYSA')
thermo('DUEVIJNWLJUFDM-UHFFFAOYSA', 'NASA')