%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) Opt=(CalcFC,ModRedun)

Gaussian Input Prepared from Scan Object

0 1
O     0.503207103     -0.4984994382     2.94e-08
C     -0.4878179145     0.5006664422     2.94e-08
C     -1.8449064081     -0.1651748472     2.94e-08
C     1.8007387383     0.0329438636     2.94e-08
H     -0.3687189891     1.1403630451     -0.88431959
H     -0.3687189891     1.1403630451     0.8843196489
H     -1.9570590386     -0.792040734     -0.8831609475
H     -2.6366021483     0.5829835096     2.94e-08
H     -1.9570590386     -0.792040734     0.8831610063
H     1.9773579593     0.6487234137     -0.889083614
H     1.9773579593     0.6487234137     0.8890836728
H     2.4999127665     -0.7996579796     2.94e-08

B 10 4
B 7 3
B 5 2
B 6 2
B 9 3
B 12 4
B 4 1
B 2 3
B 1 2
B 11 4
B 8 3
D 6 2 3 9 S 36 -10.0


