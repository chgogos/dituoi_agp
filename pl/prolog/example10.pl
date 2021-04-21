%% non tail recursive
sum([],0).
sum([H|T],S) :-
    sum(T,S1),
    S is S1+H.

%% tail recursive
sum2(L,S):-
    sum2(L,0,S).
sum2([],S,S).
sum2([H|T],A,S):-
    NS is A + H,
    sum2(T,NS,S).

%% non tail recursive
prod([],1).
prod([H|T],P):-
    prod(T,P1),
    P is P1*H.

%% tail recursive
prod2(L,P):-
    prod2(L,1,P).
prod2([],P,P).
prod2([H|T],A,P):-
    NP is A * H,
    prod2(T,NP,P).

% ?- sum([4,3,2,1],X).
% X = 10.

% ?- sum2([4,3,2,1],X).
% X = 10.

% ?- prod([4,3,2,1],X).
% X = 24.

% ?- prod2([4,3,2,1],X).
% X = 24.
