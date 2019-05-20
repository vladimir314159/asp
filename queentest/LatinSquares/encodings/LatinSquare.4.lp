number(1..n).

1 { q(R, C, V) : number(V) } 1 :- number(R), number(C).
%filter latin square.
:- R=1..n, V=1..n, not 1{q(R,C,V)}1.
:- C=1..n, V=1..n, not 1{q(R,C,V)}1.

% filter normalized latin square.
:- not q(1, C, C), number(C).
:- not q(R, 1, R), number(R).


#show q/3.
