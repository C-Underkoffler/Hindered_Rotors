%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) Opt=(CalcFC,ModRedun)

Gaussian Input Prepared from Scan Object

0 1
O     1.14325626     -0.7007317103     3.577e-07
O     0.1018610403     1.2777299562     -2.088e-07
C     -1.2111304545     -0.7436850069     -1.2916e-06
C     -2.4607344594     0.1198651687     1.672e-06
C     2.3880744327     -0.0066713576     5.835e-07
C     0.0512489486     0.078881665     -2.829e-07
H     -1.1719527943     -1.4009411747     -0.8704261645
H     -1.1719515878     -1.4009457269     0.8704200761
H     -2.484273413     0.7635889532     0.8770614687
H     -3.3541954958     -0.5014982479     3.191e-07
H     -2.4842741097     0.7635939212     -0.877054453
H     3.1570774907     -0.7717672523     8.388e-07
H     2.4719402729     0.6208203193     -0.8851525684
H     2.4719398693     0.6208204928     0.8851536534

B 5 1
B 7 3
B 14 5
B 1 6
B 10 4
B 11 4
B 9 4
B 12 5
B 13 5
B 2 6
B 3 4
B 6 3
B 8 3
D 5 1 6 3 S 36 10.0


