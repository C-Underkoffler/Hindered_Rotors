%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) Opt=(CalcFC,ModRedun)

Gaussian Input Prepared from Scan Object

0 2
O     -1.7907140536     -0.7214144654     0.3048965902
C     1.0738709111     0.2806933217     0.5873614828
C     -0.1065195686     1.0408599027     -0.0340350264
C     1.7516469455     -0.6653646521     -0.3968060483
C     -1.1854739633     0.15378532     -0.5487433358
H     1.7935972444     1.0079136541     0.965755578
H     0.7411665359     -0.2782178681     1.4686240223
H     -0.5088370729     1.7409985185     0.7129243882
H     0.2572737556     1.647801268     -0.8650982799
H     2.1057867533     -0.1172137654     -1.2709764978
H     2.6062869933     -1.1651261041     0.0572208428
H     1.0560979216     -1.4271396487     -0.748982896
H     -1.8462690231     0.467436027     -1.342520846
H     -1.2044903792     -0.9190105082     1.039883026

B 3 2
B 2 4
B 9 3
B 10 4
B 7 2
B 14 1
B 6 2
B 1 5
B 13 5
B 12 4
B 5 3
B 8 3
B 11 4
D 4 2 3 9 S 36 10.0


