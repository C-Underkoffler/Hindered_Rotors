#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('RJUFJBKOKNCXHH-UHFFFAOYSA', 'RJUFJBKOKNCXHH-UHFFFAOYSA.py')

statmech('RJUFJBKOKNCXHH-UHFFFAOYSA')
thermo('RJUFJBKOKNCXHH-UHFFFAOYSA', 'NASA')