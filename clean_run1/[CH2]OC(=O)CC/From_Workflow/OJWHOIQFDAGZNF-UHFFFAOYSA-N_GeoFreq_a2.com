%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) opt=(calcfc,verytight,gdiis,maxcycles=900) freq iop(7/33=1,2/16=3) 

Gaussian input prepared by ASE

0 2
O                 1.2188630000       -0.6601900000       -0.0047440000
O                 0.1291940000        1.3048970000       -0.0067870000
C                -1.1374630000       -0.7481910000        0.0015030000
C                -2.4105760000        0.0802620000        0.0057600000
C                 0.0963370000        0.1101660000       -0.0042990000
C                 2.4263970000       -0.0353080000       -0.0237850000
H                -1.0821850000       -1.4046630000       -0.8689950000
H                -1.0756430000       -1.4037410000        0.8722110000
H                -3.2854490000       -0.5666270000        0.0096530000
H                -2.4557520000        0.7217110000       -0.8720690000
H                -2.4490360000        0.7231510000        0.8828710000
H                 2.4536040000        1.0319110000        0.1057970000
H                 3.2618370000       -0.7009660000        0.0877140000



