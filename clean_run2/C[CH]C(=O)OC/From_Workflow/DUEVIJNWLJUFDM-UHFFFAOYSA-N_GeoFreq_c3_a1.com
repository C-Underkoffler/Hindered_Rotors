%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) opt=(calcfc,verytight,gdiis,maxcycles=900) freq iop(7/33=1,2/16=3) 

Gaussian input prepared by ASE

0 2
O                -1.5181369759        0.6155718130       -0.5672955002
O                -0.7422596345       -1.5424803159       -0.2054201332
C                 1.3415159611       -1.1663192550       -2.3683033803
C                -2.4620529613        0.3354502370        0.4639478296
C                 0.3252744022       -0.1647610665       -1.9081095309
C                -0.6606010613       -0.4582896433       -0.8264972320
H                 2.0717505543       -1.3901849293       -1.5491981009
H                 0.8633925743       -2.1231822733       -2.6340207512
H                 1.9082194819       -0.7778645548       -3.2519729596
H                -2.5305523367       -0.7530031659        0.6426300764
H                -3.4544565682        0.7396084871        0.1448514493
H                -2.1523532705        0.8516210706        1.4062337268
H                 0.3503965376        0.8555396329       -2.3539393315


