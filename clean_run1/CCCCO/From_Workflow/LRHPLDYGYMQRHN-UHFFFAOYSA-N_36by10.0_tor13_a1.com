%nprocshared=20
%mem=5GB
#p m062x/6-311+g(2df,2p) Opt=(CalcFC,ModRedun)

Gaussian Input Prepared from Scan Object

0 1
O     2.3816082421     -1.2689998625     0.1819139341
C     0.2174907218     -0.1686641322     0.4997590497
C     -0.0557319904     -0.8143378613     1.8587239553
C     1.6979760723     -0.0293285799     0.1731281385
C     0.5956420011     -0.0786880911     3.0268578317
H     0.279123232     -1.854833256     1.8416993528
H     -1.1346507767     -0.8564740798     2.0143728047
H     -0.2316757567     0.828437922     0.4738731648
H     -0.2596625642     -0.7591697731     -0.2844458555
H     2.1767753533     0.6773738052     0.8589331403
H     1.8190873734     0.3678267278     -0.8337056204
H     0.3059433141     0.9734080354     3.0331641026
H     0.2996042271     -0.5136794354     3.9803697695
H     1.6850709243     -0.1153483193     2.9758921973
H     2.3772973808     -1.621557189     1.0740699739

B 3 5
B 11 4
B 14 5
B 15 1
B 6 3
B 2 3
B 7 3
B 4 2
B 8 2
B 1 4
B 9 2
B 12 5
B 10 4
B 13 5
D 3 2 4 10 S 36 10.0


