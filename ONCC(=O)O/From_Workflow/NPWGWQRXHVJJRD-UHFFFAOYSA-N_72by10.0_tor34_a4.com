%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) Opt=(CalcFC,ModRedun)

Gaussian Input Prepared from Scan Object

0 1
O     1.824726     0.305281     -0.763898
O     -1.951165     -0.539757     -0.468067
O     -0.893683     1.266395     0.322
N     1.506208     -0.197379     0.527823
C     0.226819     -0.858458     0.417619
C     -0.905584     0.093748     0.083884
H     -0.008589     -1.320531     1.37943
H     0.283496     -1.648561     -0.327292
H     1.37544     0.64273     1.086425
H     2.687397     -0.072838     -0.947963
H     -2.647633     0.113755     -0.614661

B 9 4
B 4 1
B 7 5
B 5 4
B 8 5
B 6 5
B 11 2
B 3 6
B 2 6
B 10 1
D 11 4 5 8 S 72 10.0


