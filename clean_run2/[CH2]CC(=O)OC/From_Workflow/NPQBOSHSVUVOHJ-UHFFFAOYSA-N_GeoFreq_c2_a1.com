%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) opt=(calcfc,verytight,gdiis,maxcycles=900) freq iop(7/33=1,2/16=3) 

Gaussian input prepared by ASE

0 2
O                 1.4766458492        0.4272820750        0.9131780022
O                -0.0315150963       -0.5024957515       -0.5615326853
C                -0.8466001791        0.4218457775        1.5470572340
C                 2.4288792263        0.0621123118       -0.0522168080
C                 0.2006876635        0.0694687466        0.5416899265
C                -1.1099701895       -0.7389380080        2.4686794836
H                -1.7920944041        0.7038747491        1.0184541413
H                -0.4920756960        1.3029629637        2.1388551008
H                 2.5236003854       -1.0332985711       -0.1074341042
H                 3.4092316729        0.5035839742        0.2581734974
H                 2.1466083227        0.4602568707       -1.0547269113
H                -1.7485764584       -1.5489731688        2.0651873750
H                -0.2762378643       -1.0602782533        3.1110053017



