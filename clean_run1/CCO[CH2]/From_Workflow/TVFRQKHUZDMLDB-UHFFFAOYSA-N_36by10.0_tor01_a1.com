%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) Opt=(CalcFC,ModRedun)

Gaussian Input Prepared from Scan Object

0 2
O     -0.7779454777     -0.1115911094     -0.6202075511
C     0.402149053     -0.6633131479     -0.0552182188
C     1.1548540269     0.3599780157     0.7734977699
C     -1.8359350781     -0.0309804654     0.2093031956
H     1.0043176205     -0.9962455261     -0.8983836202
H     0.1362355289     -1.5400932112     0.5420250919
H     1.4184122473     1.2201412073     0.1600965804
H     0.549982702     0.7065424884     1.6106379693
H     2.0696383489     -0.0783659599     1.17130475
H     -1.6801697905     -0.1604049392     1.2713623771
H     -2.6707345504     0.5272616783     -0.1793566294

B 6 2
B 4 1
B 1 2
B 5 2
B 10 4
B 7 3
B 8 3
B 2 3
B 9 3
B 11 4
D 4 1 2 6 S 36 10.0

