%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) opt=(calcfc,verytight,gdiis,maxcycles=900) freq iop(7/33=1,2/16=3) 

Gaussian input prepared by ASE

0 2
O                -0.9643106126        1.5899159345        0.0975155268
C                 0.7949573458       -0.8409390662       -0.2194568069
C                -0.7225317046       -0.8618420908       -0.1220962264
C                 1.4545811857        0.2006840039        0.5819168316
C                -1.3849743160        0.3944143015       -0.6306232199
H                 1.1617240900       -1.8639632845        0.1145367796
H                 1.0995861612       -0.7452280956       -1.2958302438
H                -1.0246663585       -1.0409555803        0.9427948145
H                -1.1066506764       -1.7351482223       -0.7116670036
H                 2.4221249073        0.6119169170        0.2141486373
H                 1.3439986448        0.1629674773        1.6895074034
H                -0.0044703328        1.4290098935        0.2807197697
H                -1.1665007180        0.5419226597       -1.7286104678
H                -2.4986928658        0.3264863003       -0.5161982853



