%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) Opt=(CalcFC,ModRedun)

Gaussian Input Prepared from Scan Object

0 2
O     0.6073440878     0.720975591     0.774133941
C     -0.7236336898     0.6231231029     0.3193633564
C     1.3507609298     -0.4512023593     0.5493292063
C     -0.8317565621     0.5787283984     -1.1618407762
H     -1.2300636324     1.5091256104     0.7191178954
H     -1.2129074324     -0.253109165     0.7656683168
H     2.3433502776     -0.2894502939     0.9619426433
H     1.4369348834     -0.6771554007     -0.517754895
H     0.888904983     -1.3093130047     1.0506871336
H     -0.1622333744     1.1837408519     -1.7555585197
H     -1.6813570925     0.1185950261     -1.6421477725

B 9 3
B 8 3
B 11 4
B 10 4
B 5 2
B 1 2
B 6 2
B 3 1
B 2 4
B 7 3
D 11 1 2 6 S 72 10.0


