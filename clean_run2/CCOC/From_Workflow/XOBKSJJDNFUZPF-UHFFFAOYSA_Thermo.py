#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('XOBKSJJDNFUZPF-UHFFFAOYSA', 'XOBKSJJDNFUZPF-UHFFFAOYSA.py')

statmech('XOBKSJJDNFUZPF-UHFFFAOYSA')
thermo('XOBKSJJDNFUZPF-UHFFFAOYSA', 'NASA')