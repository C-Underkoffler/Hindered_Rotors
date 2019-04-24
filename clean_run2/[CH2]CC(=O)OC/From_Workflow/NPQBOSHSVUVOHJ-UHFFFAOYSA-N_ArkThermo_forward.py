#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('NPQBOSHS_for', 'NPQBOSHSVUVOHJ-UHFFFAOYSA-N_ArkSpecies_forward.py')

statmech('NPQBOSHS_for')
thermo('NPQBOSHS_for', 'NASA')