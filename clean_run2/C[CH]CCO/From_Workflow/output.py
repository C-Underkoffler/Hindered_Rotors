# Coordinates for DBQZVPSK_con in Input Orientation (angstroms):
#   O   -1.8116   -0.8753    0.2106
#   C   -0.0482    0.8064    0.2427
#   C   -1.4707    0.4423   -0.1661
#   C    2.2956   -0.3044    0.1486
#   C    0.9683   -0.0265   -0.4600
#   H    0.0535    0.6883    1.3249
#   H    0.1107    1.8733    0.0282
#   H   -2.1888    1.0946    0.3284
#   H   -1.5864    0.5774   -1.2482
#   H    2.8363   -1.0818   -0.3887
#   H    2.9333    0.5897    0.1512
#   H    2.1920   -0.6124    1.1912
#   H    0.8458   -0.1687   -1.5282
#   H   -1.1173   -1.4634   -0.0997
conformer(
    label = 'DBQZVPSK_con',
    E0 = (-87.0196, 'kJ/mol'),
    modes = [
        IdealGasTranslation(mass=(73.0653, 'amu')),
        NonlinearRotor(
            inertia = ([44.975, 195.763, 216.97], 'amu*angstrom^2'),
            symmetry = 3,
        ),
        HarmonicOscillator(
            frequencies = ([59.9377, 120.765, 175.32, 245.937, 338.784, 361.724, 458.414, 487.48, 806.073, 815.445, 924.913, 933.787, 981.645, 1066.98, 1084.91, 1105.77, 1158.6, 1181.44, 1262.97, 1313.64, 1342.58, 1363.31, 1365.68, 1400.94, 1416.56, 1423.95, 1453.55, 2847.98, 2863.8, 2881.96, 2935.39, 2937.59, 2979.1, 2990.39, 3021.61, 3688.88], 'cm^-1'),
        ),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
)

# Thermodynamics for DBQZVPSK_con:
#   Enthalpy of formation (298 K)   =   -15.736 kcal/mol
#   Entropy of formation (298 K)    =    80.636 cal/(mol*K)
#    =========== =========== =========== =========== ===========
#    Temperature Heat cap.   Enthalpy    Entropy     Free energy
#    (K)         (cal/mol*K) (kcal/mol)  (cal/mol*K) (kcal/mol)
#    =========== =========== =========== =========== ===========
#            300      26.812     -15.683      80.814     -39.927
#            400      32.962     -12.691      89.379     -48.442
#            500      38.661      -9.105      97.356     -57.783
#            600      43.797      -4.977     104.868     -67.898
#            800      52.164       4.662     118.675     -90.278
#           1000      58.107      15.725     130.994    -115.269
#           1500      66.957      47.239     156.429    -187.404
#           2000      71.496      81.973     176.382    -270.791
#           2400      73.640     111.028     189.620    -344.059
#    =========== =========== =========== =========== ===========
thermo(
    label = 'DBQZVPSK_con',
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.7633, 0.0311085, 1.16601e-05, -2.71502e-08, 9.8587e-12, -10475.4, 9.56943],
                Tmin = (10, 'K'),
                Tmax = (1081.96, 'K'),
            ),
            NASAPolynomial(
                coeffs = [5.75101, 0.0386652, -1.94804e-05, 4.77012e-09, -4.58897e-13, -11778, -4.20839],
                Tmin = (1081.96, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (-87.0726, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (332.579, 'J/(mol*K)'),
    ),
)

