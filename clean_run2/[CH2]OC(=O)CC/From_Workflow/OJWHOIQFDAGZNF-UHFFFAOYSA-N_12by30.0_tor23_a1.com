%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) Opt=(CalcFC,ModRedun)

Gaussian Input Prepared from Scan Object

0 2
O     1.2187844368     -0.6603463909     0.001392167
O     0.129256573     1.3047918965     -0.0090570639
C     -1.1375275031     -0.7482480746     0.0010663746
C     -2.4105583503     0.0802889113     0.0064302597
C     0.0963087002     0.1100800715     -0.0028935734
C     2.4263583562     -0.0357551584     -0.0238687148
H     -1.0818744597     -1.4025753856     -0.8710616438
H     -1.0761891006     -1.4060303928     0.8700807088
H     -3.2854714604     -0.5665570545     0.0079818096
H     -2.4549152578     0.7240066443     -0.8697605203
H     -2.4497587464     0.720951841     0.8851474184
H     2.4538364559     1.0324190789     0.0975830891
H     3.2618783561     -0.7006139867     0.0917896892

B 5 1
B 4 3
B 9 4
B 12 6
B 13 6
B 1 6
B 7 3
B 3 5
B 10 4
B 8 3
B 11 4
B 2 5
D 7 3 4 11 S 12 30.0


