%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) Opt=(CalcFC,ModRedun)

Gaussian Input Prepared from Scan Object

0 2
O     0.6916398523     -0.0030517005     -0.6740597235
C     -0.3981208757     0.1365763635     0.2185251692
C     -1.659103023     -0.1128968188     -0.6024482298
C     1.9427264191     -0.017760743     -0.0335244157
C     -0.4145472564     1.4814460728     0.8603265423
H     -0.3219790578     -0.636208196     0.9967645864
H     -2.5445486177     -0.047543485     0.0278749835
H     -1.7333995779     0.6354546989     -1.3907850186
H     -1.6155063986     -1.1009098661     -1.0588927852
H     2.0009070592     -0.8344217395     0.6948116665
H     2.6974430088     -0.1715265642     -0.8008089359
H     2.1439772909     0.9245325512     0.4846841584
H     -0.1789860285     2.3477899075     0.2581397304
H     -0.8471325989     1.6273487259     1.8382129514

B 2 5
B 4 1
B 13 5
B 12 4
B 7 3
B 11 4
B 6 2
B 9 3
B 8 3
B 1 2
B 14 5
B 3 2
B 10 4
D 3 2 5 13 S 36 10.0


