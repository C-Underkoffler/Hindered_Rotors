%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) opt=(calcfc,verytight,gdiis,maxcycles=900) freq iop(7/33=1,2/16=3) 

Gaussian input prepared by ASE

0 2
O                 1.1101210000       -0.7221040000       -0.0000000000
O                 0.1064290000        1.2913480000        0.0000000000
C                -2.5183810000        0.0157670000       -0.0000000000
C                 2.3620130000       -0.0466470000        0.0000000000
C                -1.2088280000       -0.6688280000        0.0000000000
C                 0.0275810000        0.0830190000       -0.0000000000
H                -3.1077690000       -0.2701220000        0.8752030000
H                -2.3838760000        1.0944450000       -0.0000100000
H                -3.1077770000       -0.2701380000       -0.8751920000
H                 3.1205580000       -0.8223640000       -0.0000000000
H                 2.4563740000        0.5805370000        0.8848160000
H                 2.4563740000        0.5805390000       -0.8848150000
H                -1.1405960000       -1.7467170000        0.0000020000



