%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) Opt=(CalcFC,ModRedun)

Gaussian Input Prepared from Scan Object

0 2
O     1.4527870086     0.9887274394     -0.0919483415
C     -1.2640520698     -0.5206052223     0.2315821134
C     0.0561596258     -1.0158787923     -0.3679911748
C     -1.574935485     0.9034659341     -0.0685929563
C     1.2872100508     -0.3709663393     0.2546562154
H     -2.0755932319     -1.1539096556     -0.1538910598
H     -1.256293283     -0.6820625847     1.3130397795
H     0.0686006277     -0.8294013494     -1.4447324475
H     0.1264606713     -2.096398027     -0.2256630367
H     -2.209996914     1.4801406835     0.5873941099
H     -1.4084544298     1.2870527642     -1.066112981
H     0.6689430473     1.4743339284     0.181975992
H     1.25184623     -0.4903297126     1.3448015786
H     2.185891152     -0.8753460665     -0.0991517914

B 7 2
B 1 5
B 5 3
B 6 2
B 13 5
B 10 4
B 11 4
B 12 4
B 8 3
B 9 3
B 3 2
B 2 4
B 14 5
D 9 3 5 13 S 12 30.0


