addThreeAndDouble(X, Y):-
    Y is (X+3) * 2.

%% ?- addThreeAndDouble(1,X).
%% X=8.

%% addThreeAndDouble(1,8).
%% true.

%% addThreeAndDouble(X,8).
%% ERROR: Arguments are not sufficiently instantiated