%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) opt=(calcfc,verytight,gdiis,maxcycles=900) freq iop(7/33=1,2/16=3) 

Gaussian input prepared by ASE

0 2
O                 1.4093450569       -0.4596275057       -3.4427417258
O                -1.2673853048       -0.8685563952       -1.0107581096
O                 1.7215725341        0.8058593563       -3.2053136431
O                -1.4470640192       -2.1599541208       -1.2500055417
C                -0.0174927080       -0.4572146174       -1.4781395366
C                 0.1240836894       -0.7213294294       -2.9525462850
C                 1.1172707577       -1.0790972137       -0.6799383255
H                 0.0015519288        0.6315392156       -1.3095337154
H                -0.6263688438       -0.1159188527       -3.5134120880
H                -0.0785174658       -1.7823885305       -3.1635654453
H                 1.2889044753       -2.1380397775       -0.9951230230
H                 2.0464957254       -0.5052343470       -0.8460059613
H                 0.8892980659       -1.0722234926        0.4079569147
H                 1.5517882788        1.2471707485       -4.0692904378


