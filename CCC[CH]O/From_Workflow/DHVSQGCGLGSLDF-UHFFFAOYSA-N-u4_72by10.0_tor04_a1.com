%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) Opt=(CalcFC,ModRedun)

Gaussian Input Prepared from Scan Object

0 2
O     1.5183590868     -6.1304526356     -14.0307312829
C     2.1954470071     -5.9085619332     -11.0672618202
C     3.1180696577     -5.5692458116     -12.246643182
C     2.2050008499     -7.3918631342     -10.7169503177
C     2.7679678655     -6.2830111475     -13.505188523
H     2.5042589445     -5.3167803191     -10.2044366755
H     1.1713769011     -5.5860872906     -11.2840291814
H     4.1446092379     -5.8311064349     -11.9838979228
H     3.1030512033     -4.4809002514     -12.4056406568
H     3.21739495     -7.7214162107     -10.4792292122
H     1.571226207     -7.6006624753     -9.856111149
H     1.8542271668     -7.9938127394     -11.5552417887
H     3.5059010303     -6.4828867283     -14.2671688462
H     0.9017641017     -5.8772765153     -13.3389076485

B 14 1
B 11 4
B 2 4
B 12 4
B 6 2
B 3 2
B 7 2
B 5 3
B 13 5
B 8 3
B 1 5
B 9 3
B 10 4
D 14 1 5 13 S 72 10.0


