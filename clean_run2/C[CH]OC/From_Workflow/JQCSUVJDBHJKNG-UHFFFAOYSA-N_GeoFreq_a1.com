%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) opt=(calcfc,verytight,gdiis,maxcycles=900) freq iop(7/33=1,2/16=3) 

Gaussian input prepared by ASE

0 2
O                -0.6935210000        0.6855910000        0.1493270000
C                 1.4646060000       -0.5230190000        0.0423640000
C                -1.3940580000       -0.5223890000       -0.0520330000
C                 0.6249350000        0.6863190000       -0.1789950000
H                 1.4711370000       -0.8363810000        1.0950740000
H                 2.4909090000       -0.3014970000       -0.2427070000
H                 1.1333270000       -1.3793370000       -0.5479310000
H                -2.4373290000       -0.3192750000        0.1715390000
H                -1.3019270000       -0.8541450000       -1.0892750000
H                -1.0323770000       -1.3112160000        0.6105840000
H                 1.0515320000        1.6716500000       -0.0599150000



