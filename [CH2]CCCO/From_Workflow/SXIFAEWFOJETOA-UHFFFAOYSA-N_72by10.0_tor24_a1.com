%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) Opt=(CalcFC,ModRedun)

Gaussian Input Prepared from Scan Object

0 2
O     1.0994740371     -1.2823492662     -0.8410261257
C     2.2159314192     -0.5698312763     1.2304599621
C     3.4157092559     0.1889165308     0.6537642984
C     0.9799515486     -0.519537553     0.342253226
C     3.9915863607     -0.42224951     -0.57488281
H     1.9582049519     -0.1399623364     2.2007749314
H     2.484084874     -1.6155647406     1.4002708455
H     4.1944357345     0.2399902227     1.427870014
H     3.1306615361     1.2261781903     0.4575113233
H     0.7404120295     0.5248820091     0.1061946772
H     0.1262274442     -0.9369471223     0.87529272
H     4.1216597406     -1.4947736532     -0.62659209
H     4.5314061253     0.1801547952     -1.2903402242
H     1.8588802389     -0.963529839     -1.3379326142

B 7 2
B 3 5
B 4 2
B 2 3
B 8 3
B 6 2
B 10 4
B 9 3
B 12 5
B 11 4
B 13 5
B 14 1
B 1 4
D 14 3 5 13 S 72 10.0


