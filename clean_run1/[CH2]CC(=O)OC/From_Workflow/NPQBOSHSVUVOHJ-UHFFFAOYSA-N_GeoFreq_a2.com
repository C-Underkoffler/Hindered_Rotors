%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) opt=(calcfc,verytight,gdiis,maxcycles=900) freq iop(7/33=1,2/16=3) 

Gaussian input prepared by ASE

0 2
O                 1.0726500000       -0.7025180000       -0.0004830000
O                 0.0659010000        1.2934840000        0.0007950000
C                -1.2764660000       -0.7147160000        0.0022060000
C                 2.3306920000       -0.0315580000       -0.0010660000
C                -0.0032470000        0.0968470000        0.0005560000
C                -2.4994870000        0.1196090000       -0.0027670000
H                -1.2308900000       -1.3901910000       -0.8599280000
H                -1.2323190000       -1.3815950000        0.8713890000
H                 2.4261150000        0.5935950000        0.8844550000
H                 2.4249880000        0.5941500000       -0.8863120000
H                 3.0847750000       -0.8112140000       -0.0017930000
H                -2.4194750000        1.1939550000        0.0046780000
H                -3.4705470000       -0.3475260000       -0.0085710000



