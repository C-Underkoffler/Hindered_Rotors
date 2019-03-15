# Coordinates for PQBOSHSVUVOHJ-UHFFFAOYSA in Input Orientation (angstroms):
#   O    1.0727   -0.7025   -0.0048
#   O    0.0659    1.2934    0.0106
#   C   -1.2765   -0.7147   -0.0045
#   C    2.3307   -0.0316    0.0001
#   C   -0.0032    0.0968    0.0015
#   C   -2.4995    0.1196    0.0021
#   H   -1.2317   -1.3793   -0.8752
#   H   -1.2315   -1.3925    0.8560
#   H    2.4257    0.5871    0.8902
#   H    2.4254    0.6006   -0.8805
#   H    3.0848   -0.8112   -0.0059
#   H   -3.4706   -0.3476   -0.0013
#   H   -2.4195    1.1939    0.0103
conformer(
    label = 'PQBOSHSVUVOHJ-UHFFFAOYSA',
    E0 = (-230.215, 'kJ/mol'),
    modes = [
        IdealGasTranslation(mass=(87.0446, 'amu')),
        NonlinearRotor(
            inertia = ([50.9224, 223.841, 268.583], 'amu*angstrom^2'),
            symmetry = 6,
        ),
        HarmonicOscillator(
            frequencies = ([216.438, 341.023, 383.267, 442.362, 552.759, 630.448, 835.946, 875.741, 973.668, 1009.78, 1086.68, 1133.98, 1143.1, 1163.79, 1202.81, 1338.24, 1378.44, 1389.58, 1421.85, 1429.94, 1442.56, 1772.48, 2888.91, 2903.93, 2945.44, 3013.98, 3048.71, 3050.01, 3157.15], 'cm^-1'),
        ),
        HinderedRotor(
            inertia = (2.7868, 'amu*angstrom^2'),
            symmetry = 3,
            fourier = (
                [
                    [0.0122779, 0.0332134, -2.58459, -0.0424759, -0.0227094],
                    [1.6005e-05, -3.6872e-06, 1.75497e-05, 2.23284e-06, -2.28907e-06],
                ],
                'kJ/mol',
            ),
        ),
        HinderedRotor(
            inertia = (8.30961, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-14.1558, -18.9679, -1.30428, 0.460903, -0.339634],
                    [1.34277e-05, 5.91198e-05, 5.28968e-06, -1.33566e-05, 2.63813e-06],
                ],
                'kJ/mol',
            ),
        ),
        HinderedRotor(
            inertia = (1.38168, 'amu*angstrom^2'),
            symmetry = 2,
            fourier = (
                [
                    [-0.0907292, -2.2494, -0.0357771, -0.122638, 0.143103],
                    [-0.00143862, -0.0368031, -0.00190358, 0.00893209, 0.00587006],
                ],
                'kJ/mol',
            ),
        ),
        HinderedRotor(
            inertia = (10.1834, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-2.19018, -0.916427, -1.20192, -0.0684474, 0.272926],
                    [0.0283827, 0.0350623, 0.0798041, -0.00864581, -0.0911413],
                ],
                'kJ/mol',
            ),
        ),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
)

# Thermodynamics for PQBOSHSVUVOHJ-UHFFFAOYSA:
#   Enthalpy of formation (298 K)   =   -49.233 kcal/mol
#   Entropy of formation (298 K)    =    85.216 cal/(mol*K)
#    =========== =========== =========== =========== ===========
#    Temperature Heat cap.   Enthalpy    Entropy     Free energy
#    (K)         (cal/mol*K) (kcal/mol)  (cal/mol*K) (kcal/mol)
#    =========== =========== =========== =========== ===========
#            300      28.307     -49.176      85.405     -74.798
#            400      32.730     -46.125      94.153     -83.786
#            500      37.318     -42.624     101.947     -93.597
#            600      41.747     -38.666     109.150    -104.156
#            800      48.933     -29.563     122.195    -127.318
#           1000      54.216     -19.220     133.712    -152.932
#           1500      61.755      10.041     157.338    -225.966
#           2000      64.972      41.828     175.605    -309.382
#           2400      66.381      68.118     187.584    -382.084
#    =========== =========== =========== =========== ===========
thermo(
    label = 'PQBOSHSVUVOHJ-UHFFFAOYSA',
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.21105, 0.0683891, -0.000179219, 3.01268e-07, -1.83685e-10, -27695, 9.87109],
                Tmin = (10, 'K'),
                Tmax = (550.883, 'K'),
            ),
            NASAPolynomial(
                coeffs = [1.83079, 0.0453255, -2.63304e-05, 7.22149e-09, -7.64812e-13, -27040.9, 20.2637],
                Tmin = (550.883, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (-230.306, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (291.007, 'J/(mol*K)'),
    ),
)

