%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) Opt=(CalcFC,ModRedun)

Gaussian Input Prepared from Scan Object

0 2
O     -0.62238     -0.747656     0.157503
C     0.418413     1.477924     0.042669
C     1.729732     -0.739799     -0.013136
C     -1.897792     -0.185926     -0.055089
C     0.45771     0.006244     -0.208841
H     1.336721     1.933305     -0.322629
H     -0.418457     1.970589     -0.452214
H     0.342405     1.699649     1.117331
H     2.552478     -0.237547     -0.519407
H     1.989819     -0.817195     1.051448
H     1.640929     -1.752861     -0.402905
H     -2.008981     0.142772     -1.091606
H     -2.622543     -0.96752     0.155081
H     -2.081701     0.659403     0.611258

B 3 5
B 2 5
B 10 3
B 5 1
B 8 2
B 7 2
B 6 2
B 9 3
B 12 4
B 13 4
B 14 4
B 1 4
B 11 3
D 4 1 5 3 S 36 -10.0


