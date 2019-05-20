row(1..8).
column(1..8).

knightmove(X,Y,N):-knightmove(X-2,Y-1,N-1), row(X), column(Y), N<65.
knightmove(X,Y,N):-knightmove(X-2,Y+1,N-1), row(X), column(Y), N<64.
knightmove(X,Y,N):-knightmove(X+1,Y-2,N-1), row(X), column(Y), N<65.
knightmove(X,Y,N):-knightmove(X-1,Y-2,N-1), row(X), column(Y), N<65.
knightmove(X,Y,N):-knightmove(X+2,Y-1,N-1),  row(X), column(Y), N<65.
knightmove(X,Y,N):-knightmove(X+2,Y+1,N-1), row(X), column(Y), N<65.
knightmove(X,Y,N):-knightmove(X+1,Y+2,N-1),  row(X), column(Y), N<65.
knightmove(X,Y,N):-knightmove(X-1,Y+2,N-1),  row(X), column(Y), N<65.

{cycle(X,Y,N): row(X), column(Y)}=1 :- N=1..8*8.
:- knightmove(X,Y,N), not cycle(X,Y,N).

on(X,Y):-cycle(X,Y,_).

:-not  on(X,Y), row(X), column(Y). 

#show cycle/3. 



#show knightmove.
