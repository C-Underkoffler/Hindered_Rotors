%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) opt=(calcfc,verytight,gdiis,maxcycles=900) freq iop(7/33=1,2/16=3) 

Gaussian input prepared by ASE

0 1
O                -0.6890377019        0.2571192450       -0.9211830073
C                 0.5199513325        0.6925598621       -0.4339937590
C                 1.3223111186       -0.3326984917        0.2953616493
C                -1.5324644358       -0.2316755803        0.0500168760
H                 1.0974842939        1.0660604044       -1.3182616106
H                 0.3664172971        1.5800561386        0.2251588101
H                 2.2861531861       -0.5473700937       -0.2308480354
H                 0.7794034951       -1.2878725330        0.3874129026
H                 1.5793718518        0.0096004236        1.3299081065
H                -1.1213674006       -0.0917757936        1.0836196321
H                -1.7164738282       -1.3261209856       -0.1041848047
H                -2.5080366355        0.2870610429       -0.0025493570



