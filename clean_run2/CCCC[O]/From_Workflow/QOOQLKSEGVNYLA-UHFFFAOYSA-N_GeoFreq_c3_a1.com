%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) opt=(calcfc,verytight,gdiis,maxcycles=900) freq iop(7/33=1,2/16=3) 

Gaussian input prepared by ASE

0 2
O                 0.6273693765        1.3756666073       -1.7794568147
C                 0.7116084262       -0.4657105949        0.5461057448
C                -0.3248283847       -0.4778815021       -0.5376840947
C                 1.6942197479        0.6763779143        0.4652253538
C                -0.5284929285        0.8462776096       -1.2315974613
H                 0.1998185070       -0.4354493854        1.5405341372
H                 1.2669818899       -1.4372017564        0.5137604362
H                -0.0504319422       -1.2421882502       -1.3076614433
H                -1.3095450526       -0.8035949970       -0.1168867287
H                 2.7445266623        0.3533508815        0.6769506986
H                 1.4253052888        1.4895608502        1.1710676070
H                 1.6532720860        1.1025871020       -0.5448326927
H                -1.0241858179        1.5814439856       -0.5494782496
H                -1.2340885873        0.6620053925       -2.0728967757



