%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) opt=(calcfc,verytight,gdiis,maxcycles=900) freq iop(7/33=1,2/16=3) 

Gaussian input prepared by ASE

0 2
O                 1.4767012115        0.3930623351        0.8969917664
O                -0.0623255550       -0.5182410421       -0.5567576672
C                -0.8369594968        0.4237657161        1.5605657370
C                 2.4120228275        0.0205842652       -0.0820475904
C                 0.1911138570        0.0535859458        0.5418523639
C                -1.1140878710       -0.7344983200        2.4813233690
H                -1.7806577538        0.7261546608        1.0400703711
H                -0.4630229769        1.2982727128        2.1502171696
H                 3.3901370820        0.4281364995        0.2165151862
H                 2.1232297106        0.4342209301       -1.0809637706
H                 2.4815888124       -1.0899512294       -0.1534194962
H                -1.7683812025       -1.5333200900        2.0806179582
H                -0.2835854377       -1.0684683052        3.1213869263


