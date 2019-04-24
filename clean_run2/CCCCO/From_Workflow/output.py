# Coordinates for LRHPLDYG_con in Input Orientation (angstroms):
#   O    1.8947   -0.7253   -0.2684
#   C   -0.0001    0.7061   -0.2281
#   C   -0.9450   -0.3422    0.3484
#   C    1.4344    0.5231    0.2228
#   C   -2.3794   -0.1488   -0.1283
#   H   -0.9079   -0.2939    1.4404
#   H   -0.5867   -1.3332    0.0682
#   H   -0.3323    1.7060    0.0645
#   H   -0.0282    0.6666   -1.3203
#   H    1.4830    0.5453    1.3177
#   H    2.0555    1.3383   -0.1610
#   H   -2.4384   -0.2205   -1.2152
#   H   -3.0466   -0.9003    0.2922
#   H   -2.7580    0.8335    0.1588
#   H    2.7957   -0.8702    0.0233
conformer(
    label = 'LRHPLDYG_con',
    E0 = (-273.203, 'kJ/mol'),
    modes = [
        IdealGasTranslation(mass=(74.0732, 'amu')),
        NonlinearRotor(
            inertia = ([40.2078, 210.472, 228.306], 'amu*angstrom^2'),
            symmetry = 3,
        ),
        HarmonicOscillator(
            frequencies = ([81.2644, 137.386, 217.94, 231.54, 265.073, 335.021, 491.383, 712.097, 808.681, 825.787, 934.385, 941.905, 1014.28, 1049.33, 1093.94, 1115.23, 1180.46, 1207.36, 1245.26, 1272.6, 1278.76, 1346.08, 1351.58, 1388.76, 1413.41, 1431.59, 1437.53, 1445.95, 1460.04, 2878.9, 2906.42, 2913.56, 2919.65, 2922.76, 2948.68, 2966.23, 2986.78, 2992.53, 3740.39], 'cm^-1'),
        ),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

# Thermodynamics for LRHPLDYG_con:
#   Enthalpy of formation (298 K)   =   -60.326 kcal/mol
#   Entropy of formation (298 K)    =    78.220 cal/(mol*K)
#    =========== =========== =========== =========== ===========
#    Temperature Heat cap.   Enthalpy    Entropy     Free energy
#    (K)         (cal/mol*K) (kcal/mol)  (cal/mol*K) (kcal/mol)
#    =========== =========== =========== =========== ===========
#            300      26.685     -60.273      78.398     -83.792
#            400      33.285     -57.272      86.984     -92.066
#            500      39.540     -53.627      95.092    -101.173
#            600      45.261     -49.382     102.816    -111.072
#            800      54.687     -39.340     117.195    -133.096
#           1000      61.385     -27.692     130.164    -157.855
#           1500      71.344       5.766     157.160    -229.973
#           2000      76.484      42.859     178.466    -314.073
#           2400      78.900      73.969     192.639    -388.366
#    =========== =========== =========== =========== ===========
thermo(
    label = 'LRHPLDYG_con',
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.86114, 0.0271844, 2.66325e-05, -4.06413e-08, 1.38532e-11, -32876.2, 8.41221],
                Tmin = (10, 'K'),
                Tmax = (1082.36, 'K'),
            ),
            NASAPolynomial(
                coeffs = [4.9164, 0.0424329, -2.10367e-05, 5.06497e-09, -4.79184e-13, -34226.2, -1.9437],
                Tmin = (1082.36, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (-273.295, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (357.522, 'J/(mol*K)'),
    ),
)

