%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) opt=(calcfc,verytight,gdiis,maxcycles=900) freq iop(7/33=1,2/16=3) 

Gaussian input prepared by ASE

0 2
O                 1.0003491214       -0.0051002860        0.6692585872
C                -0.0195502785        0.0791251127       -0.2671779010
C                 0.4635585221        0.2727301244       -1.6988223982
C                -0.9822166573        1.1564547109        0.1466402352
C                 2.1135389108       -0.7155799287        0.2569474549
H                -0.5837626309       -0.8856817532       -0.2358936734
H                 0.7998547790       -0.6875889851       -2.1504960586
H                -0.3575796559        0.6666253517       -2.3263061132
H                 1.3104654503        0.9937022472       -1.7463902762
H                -0.5624543452        2.1756386846       -0.0517526809
H                -1.2143745368        1.0831142801        1.2201264392
H                -1.9409733994        1.0619378490       -0.4252819294
H                 2.4021049320       -0.4913156176       -0.7815093619
H                 2.9381516323       -0.5663178152        0.9985437945



