# Coordinates for DHVSQGCG_con in Input Orientation (angstroms):
#   O   -1.6927   -0.6528    0.4099
#   C    1.0761    0.2794    0.5958
#   C   -0.0720    1.0438   -0.0745
#   C    1.7607   -0.6989   -0.3510
#   C   -1.1585    0.1546   -0.5560
#   H    1.8012    1.0015    0.9749
#   H    0.6835   -0.2570    1.4607
#   H   -0.4734    1.7760    0.6399
#   H    0.3077    1.6112   -0.9269
#   H    2.1471   -0.1821   -1.2314
#   H    2.5948   -1.2033    0.1356
#   H    1.0589   -1.4586   -0.6948
#   H   -1.8152    0.4492   -1.3654
#   H   -2.4200   -1.1628    0.0497
conformer(
    label = 'DHVSQGCG_con',
    E0 = (-98.8114, 'kJ/mol'),
    modes = [
        IdealGasTranslation(mass=(73.0653, 'amu')),
        NonlinearRotor(
            inertia = ([59.4925, 159.234, 177.826], 'amu*angstrom^2'),
            symmetry = 3,
        ),
        HarmonicOscillator(
            frequencies = ([56.2406, 144.76, 232.051, 255.23, 336.707, 374.714, 454.365, 603.911, 738.017, 823.045, 840.688, 925.57, 1008.75, 1040.59, 1055.61, 1157.48, 1174.87, 1227.34, 1243.41, 1303.79, 1318.54, 1350.29, 1386.63, 1405.65, 1428.96, 1435.05, 1441.07, 2851.24, 2921.24, 2931.46, 2945.37, 2965.57, 2987.51, 2995.41, 3030.85, 3741.96], 'cm^-1'),
        ),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
)

# Thermodynamics for DHVSQGCG_con:
#   Enthalpy of formation (298 K)   =   -18.671 kcal/mol
#   Entropy of formation (298 K)    =    79.527 cal/(mol*K)
#    =========== =========== =========== =========== ===========
#    Temperature Heat cap.   Enthalpy    Entropy     Free energy
#    (K)         (cal/mol*K) (kcal/mol)  (cal/mol*K) (kcal/mol)
#    =========== =========== =========== =========== ===========
#            300      26.476     -18.618      79.703     -42.529
#            400      32.839     -15.649      88.201     -50.929
#            500      38.692     -12.068      96.169     -60.152
#            600      43.874      -7.933     103.692     -70.148
#            800      52.047       1.706     117.501     -92.295
#           1000      57.910      12.731     129.777    -117.046
#           1500      66.902      44.204     155.176    -188.561
#           2000      71.383      78.892     175.104    -271.316
#           2400      73.584     107.911     188.325    -344.069
#    =========== =========== =========== =========== ===========
thermo(
    label = 'DHVSQGCG_con',
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.72401, 0.0276916, 2.74888e-05, -4.98102e-08, 2.00775e-11, -11888.6, 9.73047],
                Tmin = (10, 'K'),
                Tmax = (883.588, 'K'),
            ),
            NASAPolynomial(
                coeffs = [2.79776, 0.0451564, -2.46901e-05, 6.55784e-09, -6.80731e-13, -12243, 11.1528],
                Tmin = (883.588, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (-98.8491, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (332.579, 'J/(mol*K)'),
    ),
)
