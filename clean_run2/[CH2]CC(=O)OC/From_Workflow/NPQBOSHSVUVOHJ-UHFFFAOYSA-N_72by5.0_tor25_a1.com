%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) Opt=(CalcFC,ModRedun)

Gaussian Input Prepared from Scan Object

0 2
O     0.7541330518     -0.6650180334     0.2827822854
O     0.4092092731     1.4687361122     -0.2959362423
C     -1.4412521115     0.1607212649     0.5476832231
C     2.1106940709     -0.5271358403     -0.1343962876
C     -0.0045226867     0.4297595271     0.1352354468
C     -2.1200852922     -0.6852809266     -0.4735239811
H     -1.4235214842     -0.3436665185     1.5148562841
H     -1.9263362055     1.1280355562     0.6510334302
H     2.6065269598     0.2508541842     0.4425650239
H     2.1559076859     -0.2666852071     -1.1899965401
H     2.5769252834     -1.4903860735     0.0425914888
H     -2.6115707001     -0.2257110143     -1.3162220697
H     -1.9536438447     -1.7505580307     -0.4895940616

B 10 4
B 8 3
B 11 4
B 2 5
B 5 3
B 4 1
B 9 4
B 12 6
B 13 6
B 3 6
B 7 3
B 1 5
D 8 3 6 13 S 72 5.0


