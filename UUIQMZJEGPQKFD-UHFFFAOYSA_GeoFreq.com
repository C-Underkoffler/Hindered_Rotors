%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) opt=(calcfc,maxcycle=1000) freq iop(7/33=1)

Gaussian input prepared by ASE

0 1
O                 2.0778000000       -0.4094000000        0.6990000000
O                 0.9904000000        1.0401000000       -0.6605000000
C                -1.4559000000        0.5574000000        0.1951000000
C                -0.4375000000       -0.5227000000        0.4673000000
C                -2.8374000000        0.0255000000       -0.0576000000
C                 3.2734000000       -0.1646000000       -0.0323000000
C                 0.9002000000        0.0684000000        0.1472000000
H                -1.4111000000        1.2966000000        1.0167000000
H                -1.1168000000        1.0482000000       -0.7527000000
H                -0.4626000000       -0.8711000000        1.5237000000
H                -0.5554000000       -1.3667000000       -0.2584000000
H                -2.8431000000       -1.0825000000       -0.2124000000
H                -3.3050000000        0.4459000000       -0.9828000000
H                -3.5535000000        0.2910000000        0.7613000000
H                 3.2227000000       -0.8217000000       -0.9369000000
H                 4.1826000000       -0.4516000000        0.5523000000
H                 3.3311000000        0.9175000000       -0.3116000000



