%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) opt=(calcfc,verytight,gdiis,maxcycles=900) freq iop(7/33=1,2/16=3) 

Gaussian input prepared by ASE

0 2
O                 0.4492000000       -0.5057550000       -0.0516850000
C                -0.5574130000        0.4724110000        0.0229600000
C                 1.7369030000        0.0471790000        0.0096220000
C                -1.8836120000       -0.1776390000       -0.0148180000
H                -0.4307980000        1.0584580000        0.9511850000
H                -0.4508200000        1.1907900000       -0.8048800000
H                 1.8923570000        0.5870390000        0.9503750000
H                 2.4497520000       -0.7709550000       -0.0533820000
H                 1.9113870000        0.7391490000       -0.8217630000
H                -1.9655660000       -1.2257450000        0.2243230000
H                -2.7751750000        0.4155970000       -0.1389630000



