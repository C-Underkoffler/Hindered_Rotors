%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) opt=(calcfc,verytight,gdiis,maxcycles=900) freq iop(7/33=1,2/16=3) 

Gaussian input prepared by ASE

0 2
O                -0.7970253422       -1.0055315676       -0.7687416195
C                 1.2924506099        0.2805716579       -0.2772948227
C                -1.4697852204        0.1343415026       -0.3826366722
C                 0.5394957953       -1.0390079862       -0.3703985282
H                 0.6291948640        1.0829450525        0.0708200019
H                 2.1524727754        0.2004071818        0.4328472136
H                 1.7051179515        0.5750199614       -1.2605985000
H                -1.2825557284        0.3831399617        0.6924206956
H                -1.1762268444        1.0156898856       -1.0041241199
H                -2.5667795323       -0.0436302594       -0.5190042690
H                 1.0626073108       -1.8631390462       -0.9203793263


