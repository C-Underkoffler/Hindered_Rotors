#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('NPQBOSHS_bac', 'NPQBOSHSVUVOHJ-UHFFFAOYSA-N_ArkSpecies_backward.py')

statmech('NPQBOSHS_bac')
thermo('NPQBOSHS_bac', 'NASA')