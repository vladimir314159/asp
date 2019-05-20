row(1..n).
column(1..n).

{q(X,Y): row(X), column(Y)}=n.

:- q(X,Y), q(XX,Y), X!=XX.
:- q(X,Y), q(X,YY), Y!=YY.
:- q(X,Y), q(XX,YY), (X,Y) != (XX,YY), X+Y==XX+YY.

:- q(X,Y), q(XX,YY), (X,Y)!=(XX,YY), X-Y==XX-YY.

#show q/2.
