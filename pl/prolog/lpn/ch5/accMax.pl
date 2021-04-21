accMax([H|T],A,Max):-
    H > A,
    accMax(T,H,Max).

accMax([H|T],A,Max):-
    H =< A,
    accMax(T,A,Max).

accMax([],A,A).

%% wrapper
max([H|T],Max):-
    accMax(T,H,Max).

%% ?- max([1,0,5,4], Max).
%% Max = 5.

%% ?- max([-3, -1, -5, -4], Max).
%% Max= -1.
