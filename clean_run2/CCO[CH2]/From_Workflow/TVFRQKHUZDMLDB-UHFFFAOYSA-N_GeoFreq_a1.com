%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) opt=(calcfc,verytight,gdiis,maxcycles=900) freq iop(7/33=1,2/16=3) 

Gaussian input prepared by ASE

0 2
O                -0.7159680000       -0.4835510000       -0.3716740000
C                 0.5407500000       -0.6072570000        0.2758440000
C                 1.4889860000        0.5078860000       -0.1202340000
C                -1.5118010000        0.4951050000        0.1029740000
H                 0.9311690000       -1.5773920000       -0.0252490000
H                 0.3835970000       -0.6223440000        1.3593380000
H                 1.6322860000        0.5133730000       -1.1997100000
H                 1.0897810000        1.4760000000        0.1794530000
H                 2.4568050000        0.3670210000        0.3600810000
H                -2.4621980000        0.5700460000       -0.3997820000
H                -1.4113060000        0.7672980000        1.1477520000



