%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) Opt=(CalcFC,ModRedun)

Gaussian input prepared with RMG/Hands

0 1
O     0.9801018451     -0.0392724199     0.9957761357
O     -1.6572362815     1.3656252302     -1.1315747807
C     -0.1833533447     -0.1113075794     0.1751011977
C     -0.4803174446     1.3000515717     -0.351796202
C     -1.2880027528     -0.5621128674     1.1195814995
C     -0.0302037083     -1.0989444266     -0.9751439334
C     2.2266869239     0.0541455836     0.349420535
H     -0.5235961653     1.9835347578     0.5017806561
H     0.326254328     1.6304206825     -1.0059730202
H     -1.377832021     0.1367665022     1.9516890318
H     -1.0477048404     -1.5444194794     1.5236259405
H     -2.2440625431     -0.6329473992     0.6008049017
H     0.7264453857     -0.7737980445     -1.6891250283
H     -0.9739761709     -1.1794875845     -1.5107424728
H     0.2454320627     -2.0825734106     -0.5935781665
H     2.2662593876     0.8709488177     -0.3761301486
H     2.962458252     0.2493527362     1.1260698975
H     2.4922490045     -0.8770775883     -0.1569563634
H     -2.4194019169     1.311194918     -0.5527296796

B 2 4
B 5 11
B 4 3
B 2 19
B 5 10
B 16 7
B 14 6
B 6 15
B 12 5
B 7 17
B 7 1
B 3 5
B 9 4
B 3 1
B 4 8
B 18 7
B 13 6
B 6 3
D 19 2 4 9 S 36 10.0


