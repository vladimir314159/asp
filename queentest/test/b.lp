b(1..n).
c(1..n).
d(1..n).
{a(X,Y,Z)}:-b(X),c(Y),d(Z).

 {a(X,Y,Z): b(X), c(Y)}=1:-d(Z).

%:- 2{a(X,Y,Z):b(X), c(Y)}, d(Z). 
