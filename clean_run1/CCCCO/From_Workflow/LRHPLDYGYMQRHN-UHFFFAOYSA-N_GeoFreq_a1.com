%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) opt=(calcfc,verytight,gdiis,maxcycles=900) freq iop(7/33=1,2/16=3) 

Gaussian input prepared by ASE

0 1
O                 2.4096024413       -1.3323164183        0.2664206668
C                 0.2730436407       -0.1252298895        0.5190770479
C                 0.0368699007       -0.8063809616        1.8496817003
C                 1.7322714311       -0.0381864842        0.1469962657
C                 0.5524754559       -0.0463027482        3.0418498329
H                 0.5307252203       -1.8190454217        1.8198052035
H                -1.0624206379       -0.9909987728        1.9804322873
H                -0.1602745652        0.9088281566        0.5335345249
H                -0.2866653213       -0.6871241319       -0.2751128728
H                 2.2647450114        0.7093110473        0.8071991398
H                 1.8552692448        0.3022936385       -0.9141678187
H                 0.0495990786        0.9491327171        3.1302752097
H                 0.3543795933       -0.6168163906        3.9850600478
H                 1.6557878508        0.1286354010        2.9685861307
H                 1.9484894099       -1.7698338308        1.0149685735


