%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) opt=(calcfc,verytight,gdiis,maxcycles=900) freq iop(7/33=1,2/16=3) 

Gaussian input prepared by ASE

0 2
O                 0.3691300058        0.2957863550        0.7643793628
C                -1.7819241072       -0.2162537503       -0.3033722164
C                 1.7955533731        0.0649483540        0.6150802258
C                -0.3163292274       -0.0813234929       -0.4330206792
H                -2.0768555872       -0.9953991196        0.4635116151
H                -2.2703288865        0.7450167586        0.0096564943
H                -2.2246477908       -0.5312566561       -1.2816794183
H                 2.2314298884        0.7751403497       -0.1428727454
H                 2.2697783573        0.2474768169        1.6118208080
H                 1.9947360119       -0.9946659196        0.2918209650
H                 0.2148162118       -0.8942828951       -0.9896847685


