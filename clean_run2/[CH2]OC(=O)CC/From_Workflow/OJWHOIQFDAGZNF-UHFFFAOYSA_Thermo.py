#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('OJWHOIQFDAGZNF-UHFFFAOYSA', 'OJWHOIQFDAGZNF-UHFFFAOYSA.py')

statmech('OJWHOIQFDAGZNF-UHFFFAOYSA')
thermo('OJWHOIQFDAGZNF-UHFFFAOYSA', 'NASA')