%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) opt=(calcfc,verytight,gdiis,maxcycles=900) freq iop(7/33=1,2/16=3) 

Gaussian input prepared by ASE

0 2
O                -4.4534692513        3.1204472665      -14.0752224495
C                -3.3858124430        0.1243201269      -16.0812530431
C                -3.9542087012        1.8108647788      -14.1508908780
C                -4.6861812701       -0.5983305255      -15.7894083103
C                -3.3023928741        1.4869710444      -15.4606969195
H                -3.2248464051        0.2054428138      -17.1670305453
H                -2.5494174491       -0.5179728896      -15.7051260495
H                -5.0196302783       -0.3795488554      -14.7638172077
H                -5.4942238730       -0.2761860588      -16.4920872159
H                -4.5544967026       -1.7018682770      -15.8978384981
H                -3.2278984769        1.6990116456      -13.3058916444
H                -4.7457916117        1.0791922331      -13.9540460362
H                -2.8733049503        2.3007042509      -16.0595011548
H                -4.7817377155        3.3575743089      -14.9672448377


