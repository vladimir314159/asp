{ q(1..n,1..n) }.

:- X= 1..n, not 1{ q(X,Y) }1.
:- Y= 1..n, not 1{ q(X,Y) }1. 


d1(X,Y,X-Y+n) :- X= 1..n, Y= 1..n.
d2(X,Y,X+Y-1) :- X= 1..n, Y= 1..n.


:- D=1..n*2-1, not { q(X,Y) : d1(X,Y,D) }1. 
:- D=1..n*2-1, not { q(X,Y) : d2(X,Y,D) }1.
:- q(X,Y), blocked(X,Y).
#show q/2.
