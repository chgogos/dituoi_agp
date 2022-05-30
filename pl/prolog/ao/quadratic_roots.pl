quadratic_roots(A,B,C,X) :-
	X is  ( - B + sqrt(B * B - 4 * A * C) ) / ( 2 * A).
quadratic_roots(A,B,C,X) :-
	X is  ( - B - sqrt(B * B - 4 * A * C) ) / ( 2 * A).

% ?- quadratic_roots(3,4,1,X). 
% X = -0.3333333333333333 ;
% X = -1.0.