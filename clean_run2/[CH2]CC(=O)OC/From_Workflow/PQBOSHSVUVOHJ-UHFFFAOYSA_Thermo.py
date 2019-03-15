#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('PQBOSHSVUVOHJ-UHFFFAOYSA', 'PQBOSHSVUVOHJ-UHFFFAOYSA.py')

statmech('PQBOSHSVUVOHJ-UHFFFAOYSA')
thermo('PQBOSHSVUVOHJ-UHFFFAOYSA', 'NASA')