%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) opt=(calcfc,verytight,gdiis,maxcycles=900) freq iop(7/33=1,2/16=3) 

Gaussian input prepared by ASE

0 2
O                 0.7781762223       -0.1197717607       -0.7129339155
C                -0.2985898616       -0.0847452734        0.1579416415
C                 0.0610554871       -0.5386747239        1.5642217726
C                 1.8306780094        0.6599293114       -0.2680505528
C                -1.4561441087       -0.8786267980       -0.3774771196
H                -0.6352937773        0.9760877916        0.2661633653
H                 0.6527850487       -1.4635757263        1.5446268310
H                 0.6480821048        0.2347228875        2.0856058965
H                -0.8493658378       -0.7270089000        2.1550558773
H                 2.3260093473        0.2156367376        0.6087779392
H                 2.5785084042        0.7390460902       -1.0949503387
H                 1.4961526565        1.6762578403        0.0043189381
H                -2.3329183266       -0.9986032639        0.2829839834
H                -1.2710659420       -1.7086351552       -1.0747166832


