%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) opt=(calcfc,verytight,gdiis,maxcycles=900) freq iop(7/33=1,2/16=3) 

Gaussian input prepared by ASE

0 2
O                 0.5410056585        0.7216308319        0.9801138737
C                -0.7837244106        0.6500648422        0.3610822581
C                 1.3624899381       -0.3669576888        0.4814286943
C                -0.7756050318        0.6454469119       -1.1027043059
H                -1.3681076336        1.5194232225        0.7811672726
H                -1.3173599590       -0.2803573842        0.7637661131
H                 2.3832735769       -0.2423423005        0.9211984007
H                 1.4177083751       -0.3289640688       -0.6446540174
H                 0.9315206438       -1.3610605588        0.7922615524
H                 0.1361495957        0.2846626590       -1.6338881584
H                -1.7420073752        0.5125118907       -1.6368311539



