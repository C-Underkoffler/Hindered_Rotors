#!/usr/bin/env python
# -*- coding: utf-8 -*-

modelChemistry = "M06-2X/cc-pVTZ"
useHinderedRotors = True
useBondCorrections = True

species('XOBKSJJDNFUZPF-UHFFFAOYSA-N', 'XOBKSJJDNFUZPF-UHFFFAOYSA-N.py')

statmech('XOBKSJJDNFUZPF-UHFFFAOYSA-N')
thermo('XOBKSJJDNFUZPF-UHFFFAOYSA-N', 'NASA')