%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) Opt=(CalcFC,ModRedun)

Gaussian Input Prepared from Scan Object

0 2
O     -1.5434028608     -1.7332640525     -0.1732092989
O     -0.0643443255     1.1727573958     -0.7277123894
O     2.44477196     0.0207393235     -0.5489578602
O     2.1809495388     -0.19214978     0.8330302737
C     -0.7585716037     0.5453885395     0.2074603035
C     -0.5996072992     -1.0257248775     -0.1497772653
C     -2.2140905817     0.9301925963     0.350081962
H     -0.2104937953     0.5152684988     1.1711456691
H     2.9320001877     0.2444381727     1.2483820905
H     0.4402887846     -1.3236352072     -0.3433982651
H     -2.7265984084     0.8028409698     -0.6014540251
H     -2.7062299154     0.310301811     1.0971288386
H     -2.2808909233     1.9743005821     0.6495013033
H     1.7146732423     0.6250880278     -0.7773323367

B 10 6
B 5 6
B 8 5
B 7 5
B 11 7
B 2 5
B 12 7
B 4 2
B 1 3
B 13 7
B 14 3
B 9 6
B 6 1
D 4 2 5 7 S 12 30.0


