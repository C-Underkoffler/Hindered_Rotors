%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) Opt=(CalcFC,ModRedun)

Gaussian Input Prepared from Scan Object

0 1
C     0.7591841831     -0.0453957393     0.0525856138
C     -0.7591862552     0.0453564945     -0.0525893412
H     1.0814986537     -0.0765940923     1.092818684
H     1.2391816357     0.8128818043     -0.4163181363
H     1.1357664035     -0.9428477563     -0.4370491541
H     -1.081571645     0.0757915943     -1.0928093293
H     -1.1356491788     0.9432116727     0.4363297103
H     -1.239223797     -0.8125039779     0.4170319526

B 8 2
B 2 1
B 3 1
B 4 1
B 5 1
B 6 2
B 7 2
D 5 1 2 6 S 36 10.0


