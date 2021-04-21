member2(X,[X|_]).
member2(X,[_|T]) :- member2(X,T).

%% ?- member(yolanda, [yolanda, trudy, vincent, jules]).
%% true.

%% ?- member(X, [yolanda, trudy, vincent, jules]).
%% X = yolanda;
%% X = trudy;
%% X = vincent;
%% X = jules.
