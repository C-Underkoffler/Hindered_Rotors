%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) Opt=(CalcFC,ModRedun)

Gaussian Input Prepared from Scan Object

0 2
O     -0.4916713713     -0.4686875303     0.0391925413
C     1.8686650059     -0.0971243433     0.0056960251
C     -1.7982287776     0.0605813196     -0.0057588357
C     0.4954970856     0.4517793979     -0.0823798913
H     2.0849023266     -0.5070842971     0.9995952658
H     2.6002983175     0.6805601992     -0.2043719412
H     2.0044398035     -0.905350488     -0.7143041359
H     -2.4879985687     -0.7682593811     0.1239651182
H     -1.9474630514     0.7868664874     0.7977816382
H     -1.9828782061     0.5459366832     -0.9665098914
H     0.2602184361     1.4542049525     0.2632601069

B 11 4
B 10 3
B 1 4
B 8 3
B 6 2
B 5 2
B 4 2
B 3 1
B 7 2
B 9 3
D 4 1 3 8 S 12 30.0


