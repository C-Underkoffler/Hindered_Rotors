%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) opt=(calcfc,verytight,gdiis,maxcycles=900) freq iop(7/33=1,2/16=3) 

Gaussian input prepared by ASE

0 1
O                 1.2709878361        0.5492092308        0.3450030822
O                 1.1376646077       -1.7557084520        0.0654897425
C                -0.6813730476       -0.5875659042        1.2337481603
C                -0.5622486469        0.0232748333        2.6141292347
C                 2.4968261323        0.4314061219       -0.3726123922
C                 0.6269459683       -0.6823081605        0.5097766155
H                -1.3704452882        0.0250335991        0.6360549816
H                -1.1375197230       -1.6034836901        1.3155248243
H                -1.5700754873        0.1677932796        3.0658860039
H                -0.0501386920        1.0152293892        2.5700820660
H                 0.0304927092       -0.6417155431        3.2916804091
H                 2.9243517247       -0.5793192252       -0.2463534898
H                 3.2018340727        1.1996551908        0.0280784889
H                 2.3200026524        0.6296805103       -1.4610053102


