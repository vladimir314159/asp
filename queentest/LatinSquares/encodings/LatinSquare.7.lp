1 { q(R, C, V) : V=1..n } 1 :- R=1..n, C=1..n.
1 { q(R, C, V) : R=1..n} 1 :- V=1..n, C=1..n.
1 { q(R, C, V) : C=1..n} 1 :- V=1..n, R=1..n.


% filter normalized latin square.
:- not q(1, C, C), C=1..n.
:- not q(R, 1, R), R=1..n.


#show q/3.