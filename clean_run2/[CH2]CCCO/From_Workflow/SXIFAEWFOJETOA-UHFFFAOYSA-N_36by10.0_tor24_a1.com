%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) Opt=(CalcFC,ModRedun)

Gaussian Input Prepared from Scan Object

0 2
O     -1.452787     -0.988728     -0.09195
C     -0.05616     1.015879     -0.367991
C     1.264052     0.520605     0.231583
C     -1.28721     0.370966     0.254656
C     1.574935     -0.903466     -0.068592
H     -0.126461     2.096398     -0.225662
H     -0.0686     0.829402     -1.444732
H     1.256292     0.682062     1.313041
H     2.075593     1.15391     -0.15389
H     -2.185891     0.875346     -0.099152
H     -1.251847     0.490328     1.344801
H     2.209989     -1.480144     0.587399
H     1.408461     -1.287051     -1.066114
H     -0.668943     -1.474334     0.181973

B 4 2
B 3 5
B 2 3
B 7 2
B 12 5
B 6 2
B 14 1
B 1 4
B 8 3
B 9 3
B 13 5
B 10 4
B 11 4
D 8 3 5 13 S 36 10.0


