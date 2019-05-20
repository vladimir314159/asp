row(1..n).
column(1..n).


{queen(X,Y): row(X), column(Y)}=n.

{queen(X,Y): row(X)}=1 :- column(Y).

{queen(X,Y): column(Y)}=1 :- row(X).



:- queen(X,Y), blocked(X,Y).


:- queen(X,Y), queen(XX,YY), (X,Y) != (XX,YY), X+Y==XX+YY.

:- queen(X,Y), queen(XX,YY), (X,Y)!=(XX,YY), X-Y==XX-YY.

#show queen/2.
