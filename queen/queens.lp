row(1..n).
column(1..n).


{queen(X,Y): row(X), column(Y)}=n.

:- queen(X,Y), queen(XX,Y), X!=XX.
:- queen(X,Y), queen(X,YY), Y!=YY.
:- queen(X,Y), queen(XX,YY), (X,Y) != (XX,YY), X+Y==XX+YY.

:- queen(X,Y), queen(XX,YY), (X,Y)!=(XX,YY), X-Y==XX-YY.

#show queen/2.
