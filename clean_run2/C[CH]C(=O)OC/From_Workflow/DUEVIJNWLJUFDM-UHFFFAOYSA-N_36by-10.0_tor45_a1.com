%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) Opt=(CalcFC,ModRedun)

Gaussian Input Prepared from Scan Object

0 2
O     1.1101214001     -0.7221036343     7.979e-07
O     0.1064282378     1.2913478256     -1.5581e-06
C     -2.518380437     0.0157670319     2.228e-07
C     2.36201305     -0.0466469776     5.35e-08
C     -1.2088285286     -0.6688286467     8.743e-07
C     0.0275812165     0.0830190943     -1.177e-07
H     -3.1077704385     -0.2701242926     0.875201595
H     -2.3838755281     1.0944453735     -6.399e-06
H     -3.1077753968     -0.2701351281     -0.8751941684
H     3.1205577812     -0.8223637534     5.089e-07
H     2.4563739048     0.5805385188     0.884815067
H     2.4563735961     0.5805371967     -0.8848159148
H     -1.1405958574     -1.7467176081     3.0385e-06

B 10 4
B 11 4
B 6 5
B 1 6
B 2 6
B 9 3
B 12 4
B 7 3
B 5 3
B 8 3
B 13 5
B 4 1
D 13 5 6 2 S 36 -10.0


