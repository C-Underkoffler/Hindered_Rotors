%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) opt=(calcfc,verytight,gdiis,maxcycles=900) freq iop(7/33=1,2/16=3) 

Gaussian input prepared by ASE

0 2
O                 1.6111831499        0.7239742680      -13.8620880863
C                 0.4860635498        0.4861630803      -10.2134289795
C                 1.7948943891        0.7040352096      -12.4707413594
C                 0.7311367689       -0.9695828808       -9.8683214395
C                 0.5192141460        0.7633025580      -11.6868471135
H                 1.2407520030        1.0964708814       -9.6944169695
H                -0.5121740834        0.7856957654       -9.8043199253
H                 0.1896364915       -1.6381763845      -10.5543614867
H                 1.8222518609       -1.2061298189       -9.9314162267
H                 0.3885492616       -1.1867129544       -8.8279456271
H                 2.3551877332       -0.2365787189      -12.2354156781
H                 2.4680880805        1.5143738221      -12.1693152542
H                -0.4260154387        0.6519997974      -12.2336536770
H                 0.9949653916        1.4589103772      -14.0616825495



