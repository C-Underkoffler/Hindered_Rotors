%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) opt=(calcfc,verytight,gdiis,maxcycles=900) freq iop(7/33=1,2/16=3) 

Gaussian input prepared by ASE

0 1
O                 0.5031880000       -0.4985190000        0.0000000000
C                -0.4878220000        0.5006990000        0.0000000000
C                -1.8449050000       -0.1651530000       -0.0000000000
C                 1.8007270000        0.0329090000       -0.0000000000
H                -0.3686780000        1.1403490000       -0.8843530000
H                -0.3686780000        1.1403490000        0.8843540000
H                -1.9570090000       -0.7920010000       -0.8831790000
H                -2.6366900000        0.5829050000        0.0000000000
H                -1.9570090000       -0.7920010000        0.8831790000
H                 1.9773380000        0.6487620000       -0.8890360000
H                 1.9773380000        0.6487620000        0.8890360000
H                 2.4998920000       -0.7997080000       -0.0000000000


