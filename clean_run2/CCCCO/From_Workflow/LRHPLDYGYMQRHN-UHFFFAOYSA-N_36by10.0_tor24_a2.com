%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) Opt=(CalcFC,ModRedun)

Gaussian Input Prepared from Scan Object

0 1
O     1.8947082035     -0.7253437133     -0.2684462791
C     -0.0001215353     0.7061276792     -0.2281221332
C     -0.9449887069     -0.34221911     0.3484360597
C     1.4344299679     0.5230653996     0.2228006767
C     -2.3794117844     -0.148821216     -0.1282791225
H     -0.9079276536     -0.2938729485     1.4403535966
H     -0.5866541116     -1.3331568958     0.0681976843
H     -0.3322614353     1.7059745079     0.0644806909
H     -0.0282375873     0.6665805785     -1.3202956382
H     1.4830316662     0.5452538162     1.3177391431
H     2.0555415257     1.3383298228     -0.1609858985
H     -2.438434734     -0.2204815425     -1.2151922929
H     -3.0465709487     -0.9003317736     0.2922338329
H     -2.7579946392     0.833540586     0.1587922539
H     2.795670773     -0.8701821903     0.0232674263

B 14 5
B 15 1
B 6 3
B 2 3
B 7 3
B 4 2
B 8 2
B 1 4
B 9 2
B 12 5
B 10 4
B 13 5
B 3 5
B 11 4
D 7 3 5 13 S 36 10.0

