%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) opt=(calcfc,verytight,gdiis,maxcycles=900) freq iop(7/33=1,2/16=3) 

Gaussian input prepared by ASE

0 1
O                 1.2845008204        0.5432833031        0.3742786042
O                 1.1436148431       -1.7614302784        0.0809269628
C                -0.6839863191       -0.5848946560        1.2287403794
C                -0.5763940584        0.0247600591        2.6105920262
C                 2.5042678129        0.4340971463       -0.3549510833
C                 0.6345806565       -0.6869901070        0.5246330085
H                -1.3607522264        0.0322948283        0.6217800123
H                -1.1456280030       -1.5988508702        1.3037464554
H                -1.5868192608        0.1668818396        3.0572764895
H                -0.0689627717        1.0192352445        2.5693222444
H                 0.0133440561       -0.6402035045        3.2907850323
H                 2.3198399228        0.6427849076       -1.4239323468
H                 2.9367501397       -0.5896832029       -0.2425729557
H                 3.2117106574        1.2025037474        0.0503319500


