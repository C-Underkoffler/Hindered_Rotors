%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) Opt=(CalcFC,ModRedun)

Gaussian Input Prepared from Scan Object

0 2
O     -0.6391214978     -0.728820504     0.9012762037
C     0.3298665785     -0.5581969044     -0.1208712293
C     1.5941828891     -1.2702711751     0.2966296714
C     -1.8358387877     -0.1656293183     0.6507681065
H     -0.0649035611     -0.9686432949     -1.0559959841
H     0.5057764967     0.5113345964     -0.2672303025
H     1.401963383     -2.3318715203     0.4426105042
H     1.9716206902     -0.855654933     1.229751971
H     2.3597229301     -1.1567512519     -0.4695944616
H     -2.1122113167     0.0142514639     -0.380662735
H     -2.5797617747     -0.3480135153     1.4085007014

B 5 2
B 2 3
B 6 2
B 8 3
B 10 4
B 1 2
B 11 4
B 4 1
B 7 3
B 9 3
D 2 1 4 10 S 72 10.0


