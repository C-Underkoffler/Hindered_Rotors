%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) Opt=(CalcFC,ModRedun)

Gaussian Input Prepared from Scan Object

0 2
O     0.3783348898     -0.4033473384     0.8403427085
C     0.0270492168     0.6493924621     -0.0454172444
C     -0.1792362618     0.1425789048     -1.4600004881
C     1.6699502328     -0.7835311812     0.8068996376
H     -0.893491405     1.0730861741     0.3514044548
H     0.8016696958     1.4206105267     -0.0088308478
H     0.7363223498     -0.2953909599     -1.8558727638
H     -0.4759678329     0.9626078523     -2.1132454667
H     -0.9593674357     -0.6168298275     -1.4772740826
H     2.2922125835     -0.4536896776     -0.013452302
H     1.8899135947     -1.6786819991     1.3635881321

B 2 3
B 6 2
B 11 4
B 10 4
B 8 3
B 7 3
B 9 3
B 1 2
B 5 2
B 4 1
D 11 1 4 10 S 72 10.0


