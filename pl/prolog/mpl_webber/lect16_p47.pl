myappend([], L, L).
myappend([H|L1], L2, [H|L3]) :-
    myappend(L1, L2, L3).