%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) opt=(calcfc,verytight,gdiis,maxcycles=900) freq iop(7/33=1,2/16=3) 

Gaussian input prepared by ASE

0 2
O                -1.4968512131        0.6309264491       -0.5366372048
O                -0.7279985455       -1.5310587622       -0.1920751088
C                 1.3333448157       -1.1712025390       -2.3719148682
C                -2.4558182633        0.3402567719        0.4776613830
C                 0.3371990080       -0.1572599685       -1.8951989324
C                -0.6454328108       -0.4445516944       -0.8089702304
H                 2.0747438533       -1.4075931681       -1.5664716377
H                 0.8370742794       -2.1204643514       -2.6315532635
H                 1.8971571351       -0.7979770872       -3.2639576310
H                -2.1819663090        0.8726005443        1.4066207660
H                -2.4980662168       -0.7597155090        0.6733841508
H                -3.4523211445        0.7085988392        0.1290138973
H                 0.3608815854        0.8603728037       -2.3471630090



