%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) opt=(calcfc,verytight,gdiis,maxcycles=900) freq iop(7/33=1,2/16=3) 

Gaussian input prepared by ASE

0 2
O                -0.5946461757       -0.4497232564        0.3910146235
C                -0.2165006878        0.3057944829       -1.9594406281
C                -1.9823193712       -0.1467005634        0.0970478537
C                 0.2839788827        0.1213156559       -0.5804808462
H                -0.5631843767       -0.6691218418       -2.4186575939
H                 0.5960850265        0.7109399713       -2.6137261943
H                -1.0892439551        1.0116941287       -2.0107544942
H                -2.5943602715       -0.5622767164        0.9367486684
H                -2.1372732401        0.9650466153        0.0285913603
H                -2.2926236080       -0.6267962149       -0.8726986527
H                 1.2899393204       -0.3483385937       -0.4731515124


