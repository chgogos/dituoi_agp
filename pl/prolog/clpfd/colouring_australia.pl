:- use_module(library(clpfd)).

colourable([WA, SA, NT, Q, NSW, V, T]) :-
                rgb(WA), rgb(SA), rgb(NT), rgb(Q), rgb(NSW), rgb(V), rgb(T),
                WA #\= NT, NT #\= Q, Q #\= NSW, NSW #\= V,
                SA #\= WA, SA #\= NT, SA #\= Q, SA #\= NSW, SA #\= V.

rgb(1).
rgb(2).
rgb(3).

% ?- colourable(X).
% X = [1, 2, 3, 1, 3, 1, 1] ;
% X = [1, 2, 3, 1, 3, 1, 2] ;
% X = [1, 2, 3, 1, 3, 1, 3] ;
% X = [1, 3, 2, 1, 2, 1, 1] ;
% X = [1, 3, 2, 1, 2, 1, 2] ;
% X = [1, 3, 2, 1, 2, 1, 3] ;
% X = [2, 1, 3, 2, 3, 2, 1] ;
% X = [2, 1, 3, 2, 3, 2, 2] ;
% X = [2, 1, 3, 2, 3, 2, 3] ;
% X = [2, 3, 1, 2, 1, 2, 1] ;
% ...