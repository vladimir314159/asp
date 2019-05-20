numbers(1..n).
row(1..n).
column(1..n).

1{bourd(X,Y,N): numbers(N)}1:-row(X), column(Y).

1{bourd(X,Y,N): column(Y)}1:-row(X), numbers(N).

1{bourd(X,Y,N): row(X)}1:- column(Y), numbers(N).


bourd(1,1,1).

bourd(1,X,X):- bourd(1,X-1,X-1), numbers(X).
bourd(X,1,X):- bourd(X-1,1,X-1), numbers(X).

#show bourd/3.
