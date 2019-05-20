row(1..n).
column(1..n).


{q(X,Y): row(X), column(Y)}=n.

{q(X,Y): row(X)}=1 :- column(Y).

{q(X,Y): column(Y)}=1 :- row(X).

:- q(X,Y), blocked(X,Y).


:- q(X,Y), q(XX,YY), (X,Y) > (XX,YY), X+Y==XX+YY.

:- q(X,Y), q(XX,YY), (X,Y) > (XX,YY), X-Y==XX-YY.

#show q/2.
