%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) opt=(calcfc,verytight,gdiis,maxcycles=900) freq iop(7/33=1,2/16=3) 

Gaussian input prepared by ASE

0 2
O                 1.5727770000       -0.8177720000       -0.3599480000
C                -1.1171050000        0.3943230000       -0.5610350000
C                 1.2214790000        0.2359010000        0.5269880000
C                -1.7112030000       -0.6763090000        0.3653730000
C                 0.0843890000        1.0549900000        0.0270070000
H                -1.8708510000        1.1447160000       -0.7981020000
H                -0.8524050000       -0.0914750000       -1.5061730000
H                -0.9830760000       -1.4665000000        0.5457730000
H                -2.5961160000       -1.1269920000       -0.0820940000
H                -1.9955520000       -0.2447350000        1.3253820000
H                 0.9597540000       -0.2696820000        1.4639100000
H                 2.0855750000        0.8717110000        0.7415450000
H                 0.0643180000        2.1091900000        0.2648380000
H                 1.7407790000       -0.4374880000       -1.2254880000



