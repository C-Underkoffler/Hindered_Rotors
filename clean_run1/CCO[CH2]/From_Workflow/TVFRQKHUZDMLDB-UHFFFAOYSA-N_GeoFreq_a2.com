%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) opt=(calcfc,verytight,gdiis,maxcycles=900) freq iop(7/33=1,2/16=3) 

Gaussian input prepared by ASE

0 2
O                -0.5848820000        0.4598380000       -0.0098280000
C                 0.4438990000       -0.5162720000       -0.0487980000
C                 1.7756760000        0.1902550000        0.0339160000
C                -1.8376140000       -0.0323800000       -0.0289990000
H                 0.3540550000       -1.0882340000       -0.9767650000
H                 0.3094640000       -1.2073220000        0.7897610000
H                 1.8921870000        0.8774690000       -0.8023020000
H                 1.8482700000        0.7573920000        0.9603820000
H                 2.5878650000       -0.5346670000        0.0043710000
H                -1.9949990000       -1.0476690000        0.3130890000
H                -2.6095530000        0.7147140000        0.0533840000


