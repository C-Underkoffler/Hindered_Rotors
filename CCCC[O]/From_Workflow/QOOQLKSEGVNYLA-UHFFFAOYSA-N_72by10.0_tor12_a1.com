%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) Opt=(CalcFC,ModRedun)

Gaussian Input Prepared from Scan Object

0 2
O     -2.6611494297     -1.197337452     1.0814066133
C     0.9245693823     -0.6582660907     0.0580875942
C     -0.5335198067     -1.0863849881     -0.089842349
C     1.0979002342     0.847225591     0.2389932293
C     -1.3636399172     -0.7798181529     1.1520996691
H     1.4754980389     -0.9820614866     -0.8259330804
H     1.3719200545     -1.1837926773     0.9060355057
H     -0.5892970472     -2.1603422882     -0.2749070854
H     -0.9913555679     -0.5894916115     -0.9478473963
H     2.1510780873     1.1245421509     0.2415254274
H     0.6098487453     1.3928107946     -0.5703810519
H     0.6695052985     1.1941471492     1.1797935122
H     -0.8788732867     -1.150197288     2.0685949661
H     -1.4495106211     0.3133003276     1.2956841598

B 7 2
B 5 3
B 8 3
B 1 5
B 9 3
B 10 4
B 13 5
B 3 2
B 6 2
B 11 4
B 14 5
B 12 4
B 2 4
D 4 2 3 9 S 72 10.0


