%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) opt=(calcfc,verytight,gdiis,maxcycles=900) freq iop(7/33=1,2/16=3) 

Gaussian input prepared by ASE

0 2
O                 1.6401049154        0.0153186899        0.8019994584
O                 0.6200109366       -1.6305805609       -0.4878236598
C                -0.4169329156       -0.9411501950        1.6109553724
C                 0.0258051034       -1.6018657233        2.8850893753
C                 0.6206056610       -0.9147207345        0.5595811642
C                 2.6376753986        0.0409097092       -0.2178336068
H                -0.7293338508        0.0997078358        1.8370039188
H                -1.3265887161       -1.4653090089        1.2226272090
H                -0.2562461999       -2.6817869307        2.8828852728
H                -0.4629682971       -1.1172281168        3.7671830060
H                 1.1130748898       -1.5374061457        3.0232568977
H                 2.2729797203       -0.3058273183       -1.1919838190
H                 3.1884965583        0.9867875993       -0.1773338909



