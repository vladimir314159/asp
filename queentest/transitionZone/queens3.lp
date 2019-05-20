{q(1..n,1..n)}.

:- X=1..n, not 1 { q(X,Y) }1.
:- Y=1..n, not 1 { q(X,Y) }1.

:- D=1..n*2-1, not { q(X,Y) : D==X-Y+n } 1.
:- D=1..n*2-1, not { q(X,Y) : D==X+Y-1 } 1.

:- q(X,Y), blocked(X,Y).
