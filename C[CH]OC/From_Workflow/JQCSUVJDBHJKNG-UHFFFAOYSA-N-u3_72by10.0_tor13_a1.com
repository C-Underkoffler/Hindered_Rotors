%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) Opt=(CalcFC,ModRedun)

Gaussian Input Prepared from Scan Object

0 2
O     -0.6257846214     0.6243316497     -0.7642225653
C     1.5297072406     0.440059175     -1.779243511
C     -1.5538098675     0.1620984393     0.1919929591
C     0.5377099352     -0.069381041     -0.8040230336
H     1.0876008888     0.5086647661     -2.7741805954
H     1.8908583144     1.4409947413     -1.5139901775
H     2.38872872     -0.2262805278     -1.8270201628
H     -1.8473020241     -0.8673472902     -0.0243669256
H     -2.4240622232     0.8096622405     0.138053383
H     -1.1269636352     0.2098147502     1.1974598503
H     0.8438324008     -0.5438922876     0.1237744729

B 4 2
B 10 3
B 3 1
B 7 2
B 5 2
B 8 3
B 6 2
B 1 4
B 11 4
B 9 3
D 7 2 4 11 S 72 10.0


