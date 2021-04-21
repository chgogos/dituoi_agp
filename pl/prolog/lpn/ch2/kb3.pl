loves(vincent,mia).
loves(marsellus,mia).
jealous(A,B):-
loves(A,C),
loves(B,C).

%% ?- jealous(X,Y).
%% X = Y, Y = vincent ;
%% X = vincent,
%% Y = marsellus ;
%% X = marsellus,
%% Y = vincent ;
%% X = Y, Y = marsellus.
