%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) Opt=(CalcFC,ModRedun)

Gaussian Input Prepared from Scan Object

0 1
O     1.9582177676     0.9317155335     0.0304958358
O     -1.9553988736     0.7255530218     0.1623075814
O     -2.1124347174     -1.4035077117     -0.449228759
N     0.6755764357     0.5828983882     0.4819006384
C     0.079968852     -0.4605419466     -0.3369835519
C     -1.4402894959     -0.4488568382     -0.2062753567
H     0.3072835645     -0.2175759402     -1.3761728622
H     0.4357325591     -1.4732971286     -0.1334841674
H     0.761955956     0.2852345317     1.4491932863
H     2.5098453204     0.1392698236     0.051471128
H     -1.2206573685     1.3390082663     0.3266762273

B 6 3
B 1 10
B 5 7
B 4 5
B 6 2
B 2 11
B 4 9
B 5 6
B 1 4
B 5 8
D 9 4 5 8 S 36 -10.0


