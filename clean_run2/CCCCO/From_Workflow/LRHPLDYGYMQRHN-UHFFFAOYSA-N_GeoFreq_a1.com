%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) opt=(calcfc,verytight,gdiis,maxcycles=900) freq iop(7/33=1,2/16=3) 

Gaussian input prepared by ASE

0 1
O                 2.0290910000       -0.6686150000       -0.2661860000
C                 0.0063680000        0.7110760000       -0.2087380000
C                -0.9410320000       -0.3707110000        0.2991640000
C                 1.4440460000        0.5148880000        0.2454810000
C                -2.3860050000       -0.1193220000       -0.1164160000
H                -0.8745970000       -0.4252500000        1.3898640000
H                -0.6259760000       -1.3445460000       -0.0850490000
H                -0.3382000000        1.6874790000        0.1443600000
H                -0.0181700000        0.7375850000       -1.3010830000
H                 1.4932550000        0.5244010000        1.3407520000
H                 2.0678490000        1.3308100000       -0.1171420000
H                -2.4731710000       -0.0801870000       -1.2028150000
H                -3.0509010000       -0.9024220000        0.2455820000
H                -2.7416960000        0.8331140000        0.2784410000
H                 1.5886200000       -1.4276520000        0.1196320000


