%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) Opt=(CalcFC,ModRedun)

Gaussian Input Prepared from Scan Object

0 2
O     0.7600921379     -0.5575247622     -0.3328388666
C     -0.3726406821     0.0156229081     0.3181472557
C     -0.5780192744     1.4474055804     -0.1472625436
C     -1.5549950616     -0.873883124     -0.00270126
C     1.9614346755     -0.1101125878     0.0802284831
H     -0.1799960515     0.0022530631     1.3975844856
H     0.3013539154     2.0541843302     0.0638310506
H     -1.4368765293     1.889494254     0.3570108174
H     -0.7581352528     1.461938108     -1.2225777661
H     -2.4536473068     -0.4978721817     0.4845821934
H     -1.7238085606     -0.8888791452     -1.0795191185
H     -1.3721459146     -1.8926919005     0.3336807328
H     2.0456705017     0.2607268988     1.0951126098
H     2.7988854032     -0.5744784413     -0.4141780737

B 9 3
B 10 4
B 2 1
B 4 2
B 3 2
B 12 4
B 7 3
B 11 4
B 14 5
B 1 5
B 6 2
B 8 3
B 13 5
D 5 1 2 4 S 12 30.0


