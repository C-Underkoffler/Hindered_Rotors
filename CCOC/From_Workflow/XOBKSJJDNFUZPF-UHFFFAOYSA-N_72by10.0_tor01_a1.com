%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) Opt=(CalcFC,ModRedun)

Gaussian Input Prepared from Scan Object

0 1
O     0.6488234268     0.1445280302     -0.9630858321
C     -0.3790564702     -0.6935369181     -0.492291967
C     -1.3549606636     -0.9408938272     -1.6198820873
C     1.6042346361     0.4275954926     0.0233652996
H     -0.882359491     -0.2190312015     0.3603264363
H     0.0489373698     -1.6390562136     -0.1341826335
H     -1.7792568397     0.0008287801     -1.9643257972
H     -2.1655320477     -1.5882257113     -1.2875443376
H     -0.8491964726     -1.4173096132     -2.4581784284
H     1.1508242711     0.9393461793     0.8797427829
H     2.0870528995     -0.4881981748     0.3826153393
H     2.3565028172     1.0753572605     -0.42000923

B 2 3
B 6 2
B 7 3
B 8 3
B 11 4
B 5 2
B 9 3
B 10 4
B 4 1
B 1 2
B 12 4
D 4 1 2 6 S 72 10.0


