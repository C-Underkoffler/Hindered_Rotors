%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) opt=(calcfc,verytight,gdiis,maxcycles=900) freq iop(7/33=1,2/16=3) 

Gaussian input prepared by ASE

0 2
O                -2.3149950000       -0.3327460000       -0.0744130000
C                 1.3316440000        0.5772170000        0.2464570000
C                -0.1087930000        0.7487540000       -0.2363420000
C                 1.9458990000       -0.7499360000       -0.1854420000
C                -1.0303920000       -0.2458540000        0.3761600000
H                 1.9337760000        1.4030810000       -0.1344700000
H                 1.3510340000        0.6580180000        1.3361080000
H                -0.4503990000        1.7710810000       -0.0182980000
H                -0.1361460000        0.6462520000       -1.3290740000
H                 1.9428350000       -0.8385340000       -1.2731170000
H                 2.9769070000       -0.8379840000        0.1549630000
H                 1.3816660000       -1.5917440000        0.2147880000
H                -0.9518520000       -0.4916760000        1.4268190000
H                -2.3580080000       -0.0376100000       -0.9874140000


