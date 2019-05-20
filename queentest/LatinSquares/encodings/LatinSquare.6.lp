1 { q(R, C, V) : V=1..n } 1 :- R=1..n, C=1..n.
%filter latin square.
:- q(R,C1,V), q(R,C2,V), C1 < C2.
:- q(R1,C,V), q(R2,C,V), R1 < R2.

% filter normalized latin square.
:- not q(1, C, C), C=1..n.
:- not q(R, 1, R), R=1..n.


#show q/3.