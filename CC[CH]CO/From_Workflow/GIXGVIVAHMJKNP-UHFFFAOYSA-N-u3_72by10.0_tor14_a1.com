%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) Opt=(CalcFC,ModRedun)

Gaussian Input Prepared from Scan Object

0 2
O     -0.2569131353     9.6662224745     3.8782934705
C     -3.860208454     10.6272950932     4.0629605975
C     -1.4022743754     10.0717496892     4.6076329362
C     -4.5106760455     10.1914556078     5.3873064151
C     -2.6040494624     9.8900667637     3.7603237832
H     -3.6484084061     11.7005381599     4.1210038596
H     -4.5740194453     10.4912748673     3.2506096765
H     -3.8378872961     10.3677217144     6.2270337955
H     -5.4304431735     10.7459166026     5.5719746841
H     -4.7489080709     9.1280734179     5.3668305418
H     -1.4854593699     9.4785300656     5.5327052236
H     -1.324914926     11.1242393191     4.9144287058
H     -2.5971867739     9.0603584503     3.0669816931
H     0.4989803627     9.6433677872     4.4670660615

B 13 5
B 1 3
B 11 3
B 8 4
B 12 3
B 9 4
B 5 2
B 14 1
B 10 4
B 6 2
B 2 4
B 7 2
B 3 5
D 7 2 5 13 S 72 10.0


