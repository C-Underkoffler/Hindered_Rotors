#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('NPQBOSHS_con', 'NPQBOSHSVUVOHJ-UHFFFAOYSA-N_ArkSpecies_control.py')

statmech('NPQBOSHS_con')
thermo('NPQBOSHS_con', 'NASA')