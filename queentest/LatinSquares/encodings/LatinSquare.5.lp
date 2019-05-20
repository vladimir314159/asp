number(1..n).

1 { q(R, C, V) : number(V) } 1 :- number(R), number(C).
%filter latin square.
:- q(R,C1,V), q(R,C2,V), C1 < C2.
:- q(R1,C,V), q(R2,C,V), R1 < R2.

% filter normalized latin square.
:- not q(1, C, C), number(C).
:- not q(R, 1, R), number(R).


#show q/3.
