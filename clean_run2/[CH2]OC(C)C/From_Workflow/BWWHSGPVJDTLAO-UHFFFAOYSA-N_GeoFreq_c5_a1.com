%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) opt=(calcfc,verytight,gdiis,maxcycles=900) freq iop(7/33=1,2/16=3) 

Gaussian input prepared by ASE

0 2
O                 0.8421275197       -0.8276392904        0.4493430750
C                -0.0889402502       -0.1832379269       -0.3519444456
C                -1.3168768365       -1.0725306279       -0.4996374097
C                 0.4324495328        0.2841633359       -1.6817187963
C                 2.1702283901       -0.5876545685        0.1451577509
H                -0.4249043510        0.7258119642        0.2056602429
H                -1.7643308485       -1.2925083752        0.4957076349
H                -2.0842606429       -0.5767178289       -1.1228941242
H                -1.0597633323       -2.0426138064       -0.9814528545
H                 1.0097055381       -0.5180854029       -2.2084716657
H                 1.0915091327        1.1578477058       -1.5635460598
H                -0.4158190202        0.5874821975       -2.3478126487
H                 2.7930860750       -1.3317365296        0.6651074883
H                 2.3555963543       -0.5403549940       -0.9573992400



