%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) opt=(calcfc,verytight,gdiis,maxcycles=900) freq iop(7/33=1,2/16=3) 

Gaussian input prepared by ASE

0 2
O                 1.6098710593        0.0264737726        1.0209702076
O                 0.5553854876       -1.2852655959       -0.5860331405
C                -0.4962438763       -0.9805597310        1.5978782356
C                -0.0263633554       -1.6639369634        2.8501510790
C                 0.5602121879       -0.7915619542        0.5826181878
C                 2.5780312761        0.3112170849        0.0122837891
H                -0.9007535643        0.0188542842        1.8617366608
H                -1.3474607295       -1.5518726606        1.1483826234
H                -0.4233504982       -1.1509282656        3.7584521824
H                 1.0902911391       -1.6632447951        2.9204680807
H                -0.3603218322       -2.7093797613        2.8805152358
H                 3.5024592193        0.6731002348        0.4777638677
H                 2.6557732541       -0.4658503166       -0.7557341784



