%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) Opt=(CalcFC,ModRedun)

Gaussian Input Prepared from Scan Object

0 2
O     0.3161477777     -0.7909841736     0.3243617718
C     2.4619534626     -1.7270729298     -0.4269501693
C     2.8259252635     -2.59531479     0.7819435045
C     1.6413149367     -0.4958006749     -0.0669389629
C     1.6641667459     -3.272700677     1.4192799314
H     3.3812563685     -1.3955063237     -0.9144612578
H     1.9042072442     -2.3200051141     -1.1560941532
H     3.3561987022     -1.9877326415     1.520410246
H     3.5487927     -3.3556350641     0.4538601871
H     1.5523392047     0.1545903125     -0.9365835287
H     2.1579554539     0.0729116683     0.7163642665
H     1.6943760864     -3.5581185786     2.4603369848
H     0.9076718615     -3.7322184623     0.7976209623
H     0.3430565873     -1.384964779     1.0804851751

B 6 2
B 3 5
B 14 1
B 7 2
B 8 3
B 9 3
B 13 5
B 10 4
B 11 4
B 4 2
B 1 4
B 2 3
B 12 5
D 6 2 4 11 S 36 10.0


