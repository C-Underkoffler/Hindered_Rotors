%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) Opt=(CalcFC,ModRedun)

Gaussian Input Prepared from Scan Object

0 2
O     0.6083361062     0.5409408693     -0.3984093823
C     -0.6587992132     0.6031845755     0.2167210566
C     1.4336468318     -0.4584031151     0.1469167398
C     -1.513173585     -0.5735734185     -0.0880933099
H     -0.5471066458     0.7245735146     1.3026078205
H     -1.1172374172     1.5240766538     -0.1615221672
H     1.0069374476     -1.4561842628     0.0072705181
H     2.3906097126     -0.403721549     -0.3658006947
H     1.5906984894     -0.2938626208     1.2189642018
H     -1.4777058452     -1.0060774156     -1.07727705
H     -2.3023198814     -0.8745462314     0.5833992673

B 11 4
B 10 4
B 5 2
B 1 2
B 6 2
B 3 1
B 2 4
B 7 3
B 9 3
B 8 3
D 3 1 2 6 S 36 -10.0



