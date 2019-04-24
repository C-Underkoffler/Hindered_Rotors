# Coordinates for XDJVAJLI_con in Input Orientation (angstroms):
#   O    1.4398   -0.3304   -3.4436
#   O   -1.2876   -0.8456   -1.0572
#   O    1.5138    1.0827   -3.3014
#   O   -1.5072   -2.1115   -1.2298
#   C    0.0528   -0.4620   -1.4603
#   C    0.1826   -0.7343   -2.9550
#   C    1.0953   -1.1711   -0.6287
#   H    0.0618    0.6113   -1.2795
#   H   -0.6240   -0.2421   -3.5038
#   H    0.1479   -1.8082   -3.1399
#   H    1.0285   -2.2474   -0.7789
#   H    2.0828   -0.8324   -0.9368
#   H    0.9583   -0.9488    0.4278
#   H    1.5686    1.3648   -4.2214
conformer(
    label = 'XDJVAJLI_con',
    E0 = (-124.892, 'kJ/mol'),
    modes = [
        IdealGasTranslation(mass=(107.034, 'amu')),
        NonlinearRotor(
            inertia = ([95.9627, 325.694, 354.689], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([31.8938, 118.01, 137.91, 153.834, 208.906, 234.647, 295.494, 354.15, 412.814, 508.05, 622.861, 804.407, 880.925, 907.748, 935.706, 1029.69, 1070.69, 1106.85, 1148.24, 1202.9, 1236.14, 1295.72, 1325.9, 1339.5, 1349.94, 1367.08, 1417.62, 1425.06, 1438.45, 2926.39, 2941.26, 2984.44, 2999.44, 3018.2, 3021.59, 3676.35], 'cm^-1'),
        ),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
)

# Thermodynamics for XDJVAJLI_con:
#   Enthalpy of formation (298 K)   =   -23.835 kcal/mol
#   Entropy of formation (298 K)    =    92.867 cal/(mol*K)
#    =========== =========== =========== =========== ===========
#    Temperature Heat cap.   Enthalpy    Entropy     Free energy
#    (K)         (cal/mol*K) (kcal/mol)  (cal/mol*K) (kcal/mol)
#    =========== =========== =========== =========== ===========
#            300      31.646     -23.771      93.078     -51.695
#            400      37.873     -20.288     103.055     -61.510
#            500      43.304     -16.223     112.104     -72.275
#            600      48.014     -11.652     120.425     -83.907
#            800      55.561      -1.256     135.327    -109.517
#           1000      61.060      10.436     148.349    -137.913
#           1500      68.888      43.194     174.807    -219.016
#           2000      72.686      78.675     195.195    -311.715
#           2400      74.515     108.143     208.622    -392.549
#    =========== =========== =========== =========== ===========
thermo(
    label = 'XDJVAJLI_con',
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.70033, 0.0486786, -2.87127e-05, 7.8172e-09, -7.56964e-13, -15019.9, 12.3525],
                Tmin = (10, 'K'),
                Tmax = (1699.5, 'K'),
            ),
            NASAPolynomial(
                coeffs = [21.8992, 0.0125247, -2.69829e-06, -7.4922e-11, 6.3795e-14, -22170.3, -87.9361],
                Tmin = (1699.5, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (-124.923, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (332.579, 'J/(mol*K)'),
    ),
)
