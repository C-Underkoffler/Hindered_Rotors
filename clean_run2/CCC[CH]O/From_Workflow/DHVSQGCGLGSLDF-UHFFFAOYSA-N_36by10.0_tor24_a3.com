%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) Opt=(CalcFC,ModRedun)

Gaussian Input Prepared from Scan Object

0 2
O     -1.692718369     -0.6527899646     0.4098618021
C     1.0761123993     0.279446838     0.5958166307
C     -0.0719532796     1.0438262559     -0.0744942277
C     1.7607484935     -0.6989299591     -0.3510016626
C     -1.1585313249     0.1545496884     -0.5559515325
H     1.8012023443     1.0014776717     0.9748991307
H     0.6835238065     -0.2569967133     1.460691905
H     -0.4733869374     1.7760401964     0.6398759138
H     0.307726668     1.6112231914     -0.926852991
H     2.1470906428     -0.1820801582     -1.2313531578
H     2.5947772572     -1.2033369673     0.1356248064
H     1.0588677153     -1.4586364389     -0.6948379382
H     -1.8151985599     0.4492474209     -1.3653660517
H     -2.4200298561     -1.1628280612     0.0496963726

B 3 2
B 12 4
B 7 2
B 2 4
B 11 4
B 8 3
B 6 2
B 1 5
B 5 3
B 10 4
B 14 1
B 9 3
B 13 5
D 9 3 5 13 S 36 10.0


