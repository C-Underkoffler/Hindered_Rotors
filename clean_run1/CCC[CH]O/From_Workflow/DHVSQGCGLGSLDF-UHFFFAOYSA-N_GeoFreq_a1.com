%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) opt=(calcfc,verytight,gdiis,maxcycles=900) freq iop(7/33=1,2/16=3) 

Gaussian input prepared by ASE

0 2
O                10.5922452561      -20.6583497428       13.0460737970
C                12.9186916979      -23.1100482316       14.8375857165
C                12.1046013053      -22.5032771402       13.7148800025
C                13.9693851692      -22.1902578097       15.3974578429
C                11.3498308638      -21.2804926508       14.0940936875
H                12.2304807449      -23.4339196679       15.6635150720
H                13.4138089226      -24.0437906351       14.4593505109
H                11.3912755264      -23.2959479374       13.3243918317
H                12.7798724867      -22.2772613519       12.8421649596
H                14.5139532706      -22.6804447100       16.2436273212
H                13.5138762745      -21.2419693133       15.7770705575
H                14.7244294952      -21.9207110690       14.6159902789
H                10.7451801641      -21.3029817118       15.0306646055
H                11.0537762018      -20.8954345093       12.2148994717


