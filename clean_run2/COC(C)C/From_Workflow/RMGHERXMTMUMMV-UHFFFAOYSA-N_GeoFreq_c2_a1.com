%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) opt=(calcfc,verytight,gdiis,maxcycles=900) freq iop(7/33=1,2/16=3) 

Gaussian input prepared by ASE

0 1
O                 0.7725934619        0.2330941787       -0.7302578587
C                -0.2384886700        0.0752752509        0.1998443715
C                -1.3015358123        1.1136094126       -0.0324458605
C                -0.8060178385       -1.3306466637        0.1922870605
C                 1.8991354296       -0.5383748418       -0.4040995455
H                 0.1703782650        0.2481451182        1.2047335188
H                -2.1927592988        0.9166895050        0.6118471296
H                -0.9312613210        2.1183468548        0.2026222431
H                -1.6329702688        1.1127028165       -1.0907939077
H                -1.4707766908       -1.4974597994        1.0474006413
H                -1.3923215049       -1.5285830313       -0.7390426636
H                 0.0135706977       -2.0616922701        0.2391296995
H                 1.5934003878       -1.5498777332       -0.0595153833
H                 2.4902545447       -0.0618576492        0.3930952719
H                 2.5238223167       -0.6302269982       -1.3048947356



