%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) Opt=(CalcFC,ModRedun)

Gaussian Input Prepared from Scan Object

0 1
O     0.6791793242     -0.6328857885     -0.308860189
C     -0.4218387561     -0.0096703792     0.3265377817
C     -0.5821099445     1.4429124044     -0.1030902379
C     -1.6426405945     -0.8358402333     -0.0267858062
C     1.9331559936     -0.1263632195     0.0656366758
H     -0.2596200228     -0.0455675706     1.4133257789
H     -0.6763245991     1.4962703586     -1.1886284881
H     0.2641200338     2.0560043488     0.2035689476
H     -1.4799244779     1.8687987524     0.3443121666
H     -2.5287227225     -0.4446273377     0.4717520195
H     -1.4978522908     -1.8724580786     0.2717413979
H     -1.807405239     -0.8070710158     -1.104271535
H     2.1141373446     0.871966197     -0.3423552896
H     2.0320765596     -0.0822107626     1.1564009037
H     2.6867423914     -0.8040886752     -0.3288051259

B 15 5
B 12 4
B 14 5
B 10 4
B 11 4
B 6 2
B 1 5
B 8 3
B 9 3
B 7 3
B 13 5
B 4 2
B 3 2
B 2 1
D 6 2 4 11 S 36 10.0
D 2 1 5 15 F
D 5 1 2 6 F
D 6 2 3 9 F


