%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) Opt=(CalcFC,ModRedun)

Gaussian Input Prepared from Scan Object

0 2
O     1.0726526364     -0.7025203156     -0.0047759157
O     0.065899669     1.2934186593     0.010613032
C     -1.2764531116     -0.7146734023     -0.0044643912
C     2.3306964553     -0.0315784985     0.0001238168
C     -0.0032410487     0.0968155737     0.0015022461
C     -2.4995131633     0.119585958     0.0020883784
H     -1.2317459769     -1.3793362143     -0.8751752815
H     -1.2314573648     -1.3925111753     0.8560156083
H     2.4257051069     0.5870843529     0.8902338347
H     2.4254030061     0.600581596     -0.8804842132
H     3.0847787365     -0.8112110293     -0.0059476106
H     -3.4705553887     -0.3476232258     -0.0013305067
H     -2.4195225561     1.1939357211     0.0102890026

B 11 4
B 2 5
B 1 5
B 13 6
B 12 6
B 3 6
B 8 3
B 4 1
B 10 4
B 9 4
B 7 3
B 5 3
D 4 1 5 3 S 12 30.0


