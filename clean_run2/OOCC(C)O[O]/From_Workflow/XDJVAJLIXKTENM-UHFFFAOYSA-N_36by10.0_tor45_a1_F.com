%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) Opt=(CalcFC,ModRedun)

Gaussian Input Prepared from Scan Object

0 2
O     1.4398384373     -0.3304322135     -3.4435858442
O     -1.2876188149     -0.8456309514     -1.057152607
O     1.513781114     1.0827218634     -3.3013550201
O     -1.5072329651     -2.1114971886     -1.2298208095
C     0.0527994745     -0.461955338     -1.4603324417
C     0.1825797909     -0.7343416629     -2.9549500635
C     1.0953379616     -1.1711451326     -0.6287359342
H     0.0618444749     0.6113487678     -1.2794901517
H     -0.6240365331     -0.2421209404     -3.5038235292
H     0.1479060239     -1.8082010673     -3.1398505958
H     1.0285391612     -2.2473879054     -0.7788752095
H     2.0828119336     -0.8324180558     -0.9367978412
H     0.9582964236     -0.9487937916     0.4277660145
H     1.5686356883     1.3648386542     -4.2214128904

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
B 10 6
B 5 6
B 8 5
D 8 5 6 10 S 36 10.0
D 6 1 3 14 F
D 3 1 6 10 F
D 4 2 5 8 F
D 8 5 7 13 F



