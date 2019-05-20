n{q(1..n,1..n)}n.

:- q(X,Y1), q(X,Y2), Y1 < Y2.
:- q(X1,Y), q(X2,Y), X1 < X2.

:-q(X1,Y1), q(X2,Y2), X1 <X2, |X1-X2|==|Y1-Y2|.

:- q(X,Y), blocked(X,Y).
