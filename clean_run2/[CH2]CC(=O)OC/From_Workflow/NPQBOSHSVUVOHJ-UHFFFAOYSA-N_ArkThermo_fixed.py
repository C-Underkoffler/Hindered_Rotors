#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('NPQBOSHS_fix', 'NPQBOSHSVUVOHJ-UHFFFAOYSA-N_ArkSpecies_fixed.py')

statmech('NPQBOSHS_fix')
thermo('NPQBOSHS_fix', 'NASA')