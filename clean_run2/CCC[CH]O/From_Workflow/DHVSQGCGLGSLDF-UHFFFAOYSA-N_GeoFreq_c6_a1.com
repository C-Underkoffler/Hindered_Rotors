%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) opt=(calcfc,verytight,gdiis,maxcycles=900) freq iop(7/33=1,2/16=3) 

Gaussian input prepared by ASE

0 2
O                 0.5746055866        0.2043733990       -1.0248165419
C                 1.4873742814        1.2358587525        2.4039218684
C                 1.3182888188        0.1866392978        1.3119265377
C                 1.1329905369        0.7557965527        3.7833191085
C                 0.2591509007        0.4758963919        0.2935217931
H                 2.5280765108        1.5845804016        2.3963931728
H                 0.8732189242        2.1283051816        2.1645086096
H                 1.1057349706       -0.7928609737        1.7967973554
H                 2.2782149828        0.0685209918        0.7804093175
H                 0.8184516731       -0.3149595974        3.7831772643
H                 1.9931303511        0.8486053115        4.4735621992
H                 0.2938939739        1.3536833421        4.2115721121
H                -0.7579267110        0.1316230583        0.5138128133
H                 1.5610364636        0.3310955526       -1.1258513409



