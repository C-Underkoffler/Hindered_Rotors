%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) opt=(calcfc,verytight,gdiis,maxcycles=900) freq iop(7/33=1,2/16=3) 

Gaussian input prepared by ASE

0 1
O                 1.2824211273        0.6883361542        0.6062240778
O                 1.2170364897       -1.4768076391       -0.1983948403
C                -0.1777239073       -0.9404852769        1.7116901590
C                 0.2497625346       -0.4797214229        3.0809135464
C                 2.2439197356        0.8694991786       -0.4823833720
C                 0.8202956517       -0.6734505816        0.6222214517
H                -0.3994544289       -2.0380144893        1.7383554018
H                -1.1433823861       -0.4309348672        1.4430498528
H                 1.0575639981       -1.1388790001        3.4869093153
H                -0.6161004291       -0.5186892810        3.7890234139
H                 0.6352316370        0.5700633758        3.0564252758
H                 3.1444499189        0.2226666323       -0.3039243800
H                 2.5390632258        1.9478828848       -0.4810767901
H                 1.7696413247        0.5991305144       -1.4635834575



