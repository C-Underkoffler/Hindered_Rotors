%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) opt=(calcfc,verytight,gdiis,maxcycles=900) freq iop(7/33=1,2/16=3) 

Gaussian input prepared by ASE

0 2
O                 3.3137869071       -1.7495615274       -1.1255012289
O                 0.3732481434       -1.1330378998        0.7756371896
O                 2.0904691583       -1.8301218981        2.5382113695
O                 1.7621111578       -3.2210340869        2.6569714337
C                 1.0565594383       -1.0815068638       -0.4507777574
C                 2.5288035423       -1.6018029242       -0.2565583422
C                 1.0916604823        0.2938362033       -1.0885892930
H                 0.6150601483       -1.8404429164       -1.1781597408
H                 0.9136800440       -3.1625857076        3.1485645500
H                 2.7638066176       -1.8347692266        0.8682325426
H                 1.4995867850        1.0581376248       -0.3816190455
H                 1.7297009300        0.2871768249       -2.0069412261
H                 0.0563533145        0.6051887931       -1.3779194391
H                 1.3315023788       -1.4997069251        1.9243124065



