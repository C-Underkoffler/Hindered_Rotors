%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) Opt=(CalcFC,ModRedun)

Gaussian Input Prepared from Scan Object

0 1
O     -2.8894166526     -2.7100551977     0.3060183424
O     -4.5204646061     -0.5096176217     -2.7687310466
O     -3.2524625007     -0.1406292002     -0.9650460163
N     -4.2513222655     -2.320781941     0.3338371214
C     -4.6799694625     -2.0844677792     -1.0260426397
C     -4.0609090753     -0.807868052     -1.5426312397
H     -4.403327465     -2.8880602607     -1.7184181925
H     -5.7653501356     -1.9760206694     -1.0457176995
H     -4.729988162     -3.1338393826     0.7017540544
H     -2.4290048809     -1.8930689934     0.5222880054
H     -4.0779288352     0.2982438103     -3.0591400606

B 5 4
B 2 6
B 11 2
B 10 1
B 9 4
B 4 1
B 7 5
B 3 6
B 8 5
B 6 5
D 11 2 6 5 S 72 10.0


