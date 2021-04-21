change(e, w).
change(w, e).

move([X,X,Goat,Cabbage], wolf, [Y,Y,Goat,Cabbage]) :-
    change(X, Y).
move([X,Wolf,X,Cabbage], goat, [Y,Wolf,Y,Cabbage]) :-
    change(X, Y).
move([X,Wolf,Goat,X], cabbage, [Y,Wolf,Goat,Y]) :-
    change(X, Y).
move([X,Wolf,Goat,Cab], nothing, [Y,Wolf,Goat,Cab]) :-
    change(X, Y).

guarded_or_separated(X, X, X).
guarded_or_separated(_, Y, Z) :- Y \= Z.

safe([Man, Wolf, Goat, Cabbage]) :-
    guarded_or_separated(Man, Goat, Wolf),
    guarded_or_separated(Man, Goat, Cabbage).

solution([e,e,e,e], []).
solution(Config, [Move|Moves]) :-
    move(Config, Move, NextConfig),
    safe(NextConfig),
    solution(NextConfig, Moves).

