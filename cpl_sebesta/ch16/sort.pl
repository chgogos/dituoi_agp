sorted([]).
sorted([_]).
sorted([X, Y | List]) :- X =< Y, sorted([Y | List]).

%  sorted([1,2,3]).