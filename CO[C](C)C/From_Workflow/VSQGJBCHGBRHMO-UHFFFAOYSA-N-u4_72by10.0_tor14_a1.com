%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) Opt=(CalcFC,ModRedun)

Gaussian Input Prepared from Scan Object

0 2
O     -0.7057991465     -0.9084059256     0.1743912332
C     1.5838645392     -0.9829690106     -0.3855107906
C     0.4359695246     1.2693178303     0.1149999633
C     -1.9622969671     -0.2722028723     0.2365917494
C     0.3446299656     -0.1657752206     -0.288497875
H     2.0074464202     -1.1889096826     0.6070317915
H     2.3429100648     -0.4636281082     -0.9682754616
H     1.3718533207     -1.9418667509     -0.8563257773
H     -0.4384075712     1.8493264344     -0.1800147086
H     1.3090838602     1.7223938051     -0.3502938477
H     0.5483046518     1.3737295938     1.2041808892
H     -1.9843761322     0.5012579817     1.0071055454
H     -2.6896557424     -1.0403347623     0.4840761308
H     -2.2194167174     0.1737450454     -0.7276659318

B 1 4
B 13 4
B 3 5
B 9 3
B 5 1
B 10 3
B 6 2
B 11 3
B 12 4
B 8 2
B 2 5
B 14 4
B 7 2
D 7 2 5 3 S 72 10.0


