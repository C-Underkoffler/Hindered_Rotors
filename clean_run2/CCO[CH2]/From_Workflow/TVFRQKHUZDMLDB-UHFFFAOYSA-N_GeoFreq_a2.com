%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) opt=(calcfc,verytight,gdiis,maxcycles=900) freq iop(7/33=1,2/16=3) 

Gaussian input prepared by ASE

0 2
O                 0.5851330000       -0.4595720000        0.0194440000
C                -0.4443340000        0.5158660000        0.0568590000
C                -1.7752080000       -0.1903430000       -0.0415190000
C                 1.8377230000        0.0333800000        0.0213140000
H                -0.3028260000        1.2137350000       -0.7748260000
H                -0.3621510000        1.0810470000        0.9896980000
H                -1.8413760000       -0.7490130000       -0.9735850000
H                -1.8969260000       -0.8852600000        0.7875650000
H                -2.5879290000        0.5339280000       -0.0105590000
H                 2.6092580000       -0.7146570000       -0.0561950000
H                 1.9917980000        1.0433770000       -0.3375750000


