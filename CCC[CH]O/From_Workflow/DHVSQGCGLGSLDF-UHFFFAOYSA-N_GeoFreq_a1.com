%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) opt=(calcfc,verytight,gdiis,maxcycles=900) freq iop(7/33=1,2/16=3) 

Gaussian input prepared by ASE

0 2
O                38.9460883207      -32.2366787197        1.1662123144
C                39.6111716779      -33.0684787522        4.8390916418
C                39.9040629712      -32.6614729984        3.4113828407
C                38.5969347388      -32.1947795335        5.5258194441
C                38.7230805431      -32.6821447915        2.5112988220
H                39.2626104758      -34.1360272021        4.8606111269
H                40.5704785462      -33.0430206093        5.4214455357
H                40.3705001147      -31.6251523287        3.4180416142
H                40.7113077709      -33.3350203574        3.0005500886
H                37.6166029421      -32.2151833558        4.9845588290
H                38.4208992546      -32.5419940592        6.5753514242
H                38.9449403354      -31.1315387686        5.5645851955
H                37.7560847327      -32.2772969320        2.8902124166
H                39.8916500195      -32.4163706131        0.9853600292


