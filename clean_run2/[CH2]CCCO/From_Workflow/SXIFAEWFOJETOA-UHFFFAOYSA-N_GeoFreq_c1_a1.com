%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) opt=(calcfc,verytight,gdiis,maxcycles=900) freq iop(7/33=1,2/16=3) 

Gaussian input prepared by ASE

0 2
O                -2.6944260811        0.2301020246       -0.0928327301
C                -1.0986344711       -1.1339147713       -1.3086701530
C                -2.2007136838       -2.1174348539       -1.5752908314
C                -1.3745833324       -0.1578924099       -0.1907526847
C                -3.0145806591       -2.5024536046       -0.3893636085
H                -0.8943764546       -0.5696280182       -2.2532176918
H                -0.1700840959       -1.6747968747       -1.0849334087
H                -1.7478466017       -3.0278363677       -2.0231413193
H                -2.8767934738       -1.7284778822       -2.3559268809
H                -0.7672445224        0.7692260431       -0.3392640779
H                -1.0328495257       -0.6049727464        0.7752592759
H                -2.5061232036       -2.7486699890        0.5461706122
H                -3.9725694190       -2.9994645698       -0.5598879070
H                -3.2456480304       -0.5912885788       -0.1613162993



