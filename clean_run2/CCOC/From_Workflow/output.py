# Coordinates for XOBKSJJDNFUZPF-UHFFFAOYSA in Input Orientation (angstroms):
#   O    0.5032   -0.4985    0.0000
#   C   -0.4878    0.5007    0.0000
#   C   -1.8449   -0.1652    0.0000
#   C    1.8007    0.0329    0.0000
#   H   -0.3687    1.1404   -0.8843
#   H   -0.3687    1.1404    0.8843
#   H   -1.9571   -0.7920   -0.8832
#   H   -2.6366    0.5830    0.0000
#   H   -1.9571   -0.7920    0.8832
#   H    1.9774    0.6487   -0.8891
#   H    1.9774    0.6487    0.8891
#   H    2.4999   -0.7997    0.0000
conformer(
    label = 'XOBKSJJDNFUZPF-UHFFFAOYSA',
    E0 = (-222.504, 'kJ/mol'),
    modes = [
        IdealGasTranslation(mass=(60.0575, 'amu')),
        NonlinearRotor(
            inertia = ([17.719, 120.587, 128.823], 'amu*angstrom^2'),
            symmetry = 9,
        ),
        HarmonicOscillator(
            frequencies = ([282.603, 455.465, 783.055, 846.941, 1014.8, 1073.36, 1121.67, 1149.31, 1149.47, 1200.86, 1249.07, 1336.76, 1368.9, 1419.94, 1422.3, 1433.82, 1436.94, 1445.85, 1466.84, 2859.19, 2876.78, 2885.49, 2920.88, 2936.47, 3007.79, 3008.95, 3009.97], 'cm^-1'),
        ),
        HinderedRotor(
            inertia = (2.55634, 'amu*angstrom^2'),
            symmetry = 3,
            fourier = (
                [
                    [-0.0457152, 0.0666641, -5.04649, -0.0562504, 0.0360085],
                    [-2.52129e-08, 1.71065e-06, 2.08536e-05, 9.34264e-07, 7.47515e-07],
                ],
                'kJ/mol',
            ),
        ),
        HinderedRotor(
            inertia = (4.76083, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-5.80344, 2.38459, -5.88725, 0.285179, -0.41475],
                    [-0.0898351, 0.209223, -0.237448, 0.144517, -0.0470819],
                ],
                'kJ/mol',
            ),
        ),
        HinderedRotor(
            inertia = (2.51372, 'amu*angstrom^2'),
            symmetry = 3,
            fourier = (
                [
                    [-0.0554762, -0.07488, -6.20558, 0.098735, 0.0697111],
                    [-0.00218131, 0.00221985, -0.0273843, 0.00102417, -0.000727875],
                ],
                'kJ/mol',
            ),
        ),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

# Thermodynamics for XOBKSJJDNFUZPF-UHFFFAOYSA:
#   Enthalpy of formation (298 K)   =   -49.251 kcal/mol
#   Entropy of formation (298 K)    =    67.484 cal/(mol*K)
#    =========== =========== =========== =========== ===========
#    Temperature Heat cap.   Enthalpy    Entropy     Free energy
#    (K)         (cal/mol*K) (kcal/mol)  (cal/mol*K) (kcal/mol)
#    =========== =========== =========== =========== ===========
#            300      22.946     -49.205      67.638     -69.496
#            400      27.453     -46.681      74.867     -76.628
#            500      31.522     -43.729      81.438     -84.448
#            600      35.182     -40.390      87.515     -92.899
#            800      41.392     -32.709      98.520    -111.525
#           1000      46.304     -23.920     108.306    -132.226
#           1500      54.216       1.433     128.757    -191.703
#           2000      58.048      29.619     144.948    -260.277
#           2400      59.666      53.187     155.686    -320.459
#    =========== =========== =========== =========== ===========
thermo(
    label = 'XOBKSJJDNFUZPF-UHFFFAOYSA',
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.98294, 0.00245477, 0.000410019, -2.65873e-06, 6.12917e-09, -27053.9, 4.76594],
                Tmin = (10, 'K'),
                Tmax = (124.291, 'K'),
            ),
            NASAPolynomial(
                coeffs = [3.26073, 0.0316554, -1.42943e-05, 2.88097e-09, -2.01946e-13, -27040.6, 6.55913],
                Tmin = (124.291, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (-222.616, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (270.22, 'J/(mol*K)'),
    ),
)

