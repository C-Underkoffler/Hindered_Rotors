%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) Opt=(CalcFC,ModRedun)

Gaussian Input Prepared from Scan Object

0 2
O     -0.8417985982     0.0724548331     0.7084489378
C     0.5561849273     0.0894719099     0.4573131326
C     1.054009284     -1.194299265     -0.1999135589
C     -1.6499218298     -0.0913403218     -0.4321188123
C     0.9590638194     1.3060119935     -0.302408349
H     0.9862233442     0.1402542359     1.4654054486
H     2.1434148512     -1.2119834897     -0.1922869064
H     0.7259324669     -1.2631876261     -1.2370270974
H     0.6876606183     -2.0625587105     0.3460587135
H     -1.378392548     0.6127983315     -1.2250012988
H     -1.5904022725     -1.1084182065     -0.8295550822
H     -2.6743974921     0.1022244006     -0.1236345425
H     1.8440409504     1.3052900693     -0.9210112602
H     0.4742944788     2.2468768458     -0.0877683247

B 1 2
B 2 5
B 3 2
B 9 3
B 13 5
B 8 3
B 12 4
B 4 1
B 6 2
B 7 3
B 14 5
B 10 4
B 11 4
D 3 2 5 14 S 72 5.0


