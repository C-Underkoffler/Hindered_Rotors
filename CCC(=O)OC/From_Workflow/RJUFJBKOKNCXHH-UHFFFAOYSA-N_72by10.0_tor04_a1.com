%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) Opt=(CalcFC,ModRedun)

Gaussian Input Prepared from Scan Object

0 1
O     1.2696651227     -0.7749907386     -0.3943937156
O     0.2041019749     0.9283178729     0.5864883022
C     -1.0839125428     -0.8259197463     -0.4497228605
C     -2.3439697628     -0.0871348792     -0.0329714966
C     2.5058120716     -0.1680064674     -0.0272387521
C     0.1682160884     -0.10780201     -0.0176366338
H     -1.0284734745     -0.9553683029     -1.5320026764
H     -1.0448645185     -1.8317711077     -0.0279430867
H     -2.3836686151     0.027373024     1.0484536095
H     -3.2296945731     -0.6292446245     -0.3585075099
H     -2.3671516555     0.9104567215     -0.4670704329
H     3.2841175939     -0.8245472348     -0.4013139038
H     2.5902981856     0.8202625059     -0.4749685601
H     2.5736277564     -0.0709666037     1.0545466768

B 11 4
B 10 4
B 8 3
B 5 1
B 9 4
B 3 4
B 2 6
B 14 5
B 13 5
B 6 3
B 12 5
B 7 3
B 1 6
D 6 1 5 12 S 72 10.0

