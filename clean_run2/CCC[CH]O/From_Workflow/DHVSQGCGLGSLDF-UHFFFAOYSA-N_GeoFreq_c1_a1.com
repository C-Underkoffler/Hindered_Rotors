%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) opt=(calcfc,verytight,gdiis,maxcycles=900) freq iop(7/33=1,2/16=3) 

Gaussian input prepared by ASE

0 2
O                 2.6545970995        4.7064024280        2.1082004647
C                 3.5177364628        8.1833947725        2.7805899493
C                 2.7223875967        7.1593405912        1.9801910644
C                 4.7988918071        7.6336310413        3.3420034544
C                 3.3981690130        5.8335976827        1.8119167709
H                 3.7313246563        9.0540007355        2.1472259617
H                 2.8808465937        8.5686836262        3.6033231587
H                 2.5011316730        7.5872644205        0.9763849863
H                 1.7457946058        6.9963183490        2.4676442505
H                 5.6893789627        8.1789221069        2.9481205664
H                 4.8246013004        7.6887625361        4.4470776737
H                 4.8907761072        6.5614698140        3.0470799590
H                 3.9766894227        5.6769862046        0.8941553038
H                 1.9962417271        4.9684993952        2.8133144933


