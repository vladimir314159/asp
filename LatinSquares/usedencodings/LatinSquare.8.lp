numbers(1..n).
row(1..n).
column(1..n).

1{q(X,Y,N): numbers(N)}1:-row(X), column(Y).

1{q(X,Y,N): column(Y)}1:-row(X), numbers(N).

1{q(X,Y,N): row(X)}1:- column(Y), numbers(N).


%q(1,1,1).

%q(1,X,X):- q(1,X-1,X-1), numbers(X).
%q(X,1,X):- q(X-1,1,X-1), numbers(X).

#show q/3.
