%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) Opt=(CalcFC,ModRedun)

Gaussian Input Prepared from Scan Object

0 2
O     -0.9171349182     -0.5921185827     0.4573045814
C     0.2192605255     -0.0346732575     -0.2029405031
C     0.4599349058     1.3847142644     0.2838567319
C     1.3880645732     -0.9511372172     0.091408218
C     -2.1195949525     -0.212552509     -0.0138704158
H     0.0133269049     -0.0306349843     -1.2787527659
H     0.669370637     1.3760155708     1.3538110695
H     1.3119070383     1.823244791     -0.2349775784
H     -0.4108740321     2.0148518446     0.1078902905
H     2.2903499723     -0.5812727423     -0.3939849713
H     1.1839880686     -1.9590004474     -0.2647962921
H     1.5632702931     -0.9917103346     1.1665999561
H     -2.1770481887     0.6259984035     -0.6936251466
H     -2.9571307024     -0.5112359924     0.5935342405

B 13 5
B 9 3
B 10 4
B 2 1
B 4 2
B 3 2
B 12 4
B 7 3
B 11 4
B 14 5
B 1 5
B 6 2
B 8 3
D 14 2 3 9 S 72 10.0


