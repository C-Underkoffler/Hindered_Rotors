%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) Opt=(CalcFC,ModRedun)

Gaussian Input Prepared from Scan Object

0 2
O     -1.8116393063     -0.8753414216     0.2105965258
C     -0.0482412562     0.8064100588     0.2427253708
C     -1.4706510376     0.4423214663     -0.1660656692
C     2.2956100363     -0.3043536593     0.1486462589
C     0.9683091584     -0.0265161061     -0.4599902523
H     0.053530862     0.6882775883     1.3248537627
H     0.1107424196     1.8733465977     0.0282478477
H     -2.1888075699     1.0945540217     0.3284328917
H     -1.5863803961     0.5774372519     -1.2481962465
H     2.8363030975     -1.0818433685     -0.3886831047
H     2.9332584342     0.5896621407     0.1511919911
H     2.1920263589     -0.6123953598     1.1912339921
H     0.8457523462     -0.168711917     -1.5281608918
H     -1.1173101469     -1.4634072932     -0.0997454761

B 12 4
B 13 5
B 11 4
B 8 3
B 9 3
B 3 2
B 5 4
B 2 5
B 7 2
B 10 4
B 6 2
B 14 1
B 1 3
D 7 2 3 9 S 36 -10.0


