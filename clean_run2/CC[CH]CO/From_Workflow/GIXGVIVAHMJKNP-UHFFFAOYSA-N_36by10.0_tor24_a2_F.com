%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) Opt=(CalcFC,ModRedun)

Gaussian Input Prepared from Scan Object

0 2
O     1.9151539118     -0.8104812514     0.0483778591
C     -0.999228993     -0.0631579609     -0.5265241369
C     1.4748973797     0.5383423507     -0.0772469552
C     -2.3005079751     -0.2501899733     0.2498435838
C     0.0290845029     0.6976510695     0.2336125035
H     -1.2161071036     0.4623797038     -1.4677242692
H     -0.585192445     -1.030840366     -0.8182705041
H     -2.1253281959     -0.816457841     1.1645598966
H     -3.042641963     -0.7829599279     -0.3428939059
H     -2.7243330823     0.714246503     0.5321197653
H     2.0791368538     1.2014531657     0.5474156605
H     1.6812779419     0.7966328842     -1.1215871118
H     -0.2877452125     1.516416537     0.8676566864
H     1.6809643804     -1.1176288934     0.927709928

B 8 4
B 7 2
B 2 4
B 14 1
B 13 5
B 10 4
B 6 2
B 9 4
B 11 3
B 12 3
B 3 5
B 1 3
B 5 2
D 12 3 5 13 S 36 10.0
D 14 1 3 12 F
D 4 2 5 13 F
D 7 2 4 9 F



