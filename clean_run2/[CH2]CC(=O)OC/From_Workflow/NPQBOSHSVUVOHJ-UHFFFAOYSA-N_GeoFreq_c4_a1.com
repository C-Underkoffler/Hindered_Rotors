%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) opt=(calcfc,verytight,gdiis,maxcycles=900) freq iop(7/33=1,2/16=3) 

Gaussian input prepared by ASE

0 2
O                 1.4570649998        0.3884972458        0.9319819690
O                -0.1958206269       -0.3648240901       -0.4876370622
C                -0.8286652620        0.6135701775        1.6579698589
C                 2.3307617544       -0.0721295549       -0.0662972662
C                 0.1374591004        0.1681943071        0.6091663165
C                -1.2320340756       -0.5482259759        2.5261251607
H                -1.7349538173        1.0451408702        1.1626833844
H                -0.3560409976        1.4127937331        2.2825880086
H                 2.3894081990       -1.1713762634       -0.0535176580
H                 3.3432833459        0.3541205100        0.1468721475
H                 1.9902157631        0.2664520389       -1.0725841995
H                -0.5053068571       -0.8858853305        3.2907391288
H                -1.8144615346       -1.3447597800        2.0390278872



