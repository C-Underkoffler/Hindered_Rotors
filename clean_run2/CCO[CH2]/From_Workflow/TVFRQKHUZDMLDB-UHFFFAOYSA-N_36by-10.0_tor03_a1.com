%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) Opt=(CalcFC,ModRedun)

Gaussian Input Prepared from Scan Object

0 2
O     -0.7160914529     -0.4840897271     -0.3747255964
C     0.5397501353     -0.6087976876     0.2741910669
C     1.4880445986     0.5080385843     -0.1171070408
C     -1.5137160056     0.4928374802     0.0999340345
H     0.9312255194     -1.5777064568     -0.0294271628
H     0.3809568561     -0.6274786429     1.357331557
H     1.6327904826     0.5169598201     -1.1963658983
H     1.088379388     1.4752225744     0.1849714756
H     2.4552614178     0.3660664153     0.3640854855
H     -2.4715646865     0.5561889545     -0.3897107565
H     -1.3929352529     0.7889436856     1.1356158354

B 2 3
B 6 2
B 11 4
B 10 4
B 8 3
B 7 3
B 9 3
B 1 2
B 5 2
B 4 1
D 2 1 4 11 S 36 -10.0


