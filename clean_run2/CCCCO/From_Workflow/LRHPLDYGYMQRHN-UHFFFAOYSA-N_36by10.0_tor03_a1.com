%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) Opt=(CalcFC,ModRedun)

Gaussian Input Prepared from Scan Object

0 1
O     2.029091     -0.668615     -0.266186
C     0.006368     0.711076     -0.208738
C     -0.941032     -0.370711     0.299164
C     1.444046     0.514888     0.245481
C     -2.386005     -0.119322     -0.116416
H     -0.874597     -0.42525     1.389864
H     -0.625976     -1.344546     -0.085049
H     -0.3382     1.687479     0.14436
H     -0.01817     0.737585     -1.301083
H     1.493255     0.524401     1.340752
H     2.067849     1.33081     -0.117142
H     -2.473171     -0.080187     -1.202815
H     -3.050901     -0.902422     0.245582
H     -2.741696     0.833114     0.278441
H     1.58862     -1.427652     0.119632

B 1 4
B 8 2
B 12 5
B 9 2
B 13 5
B 3 5
B 10 4
B 14 5
B 11 4
B 6 3
B 2 3
B 15 1
B 7 3
B 4 2
D 15 1 4 10 S 36 10.0


