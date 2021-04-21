loves(vincent,mia).
loves(marsellus,mia).
loves(pumpkin, honey_bunny).
loves(honey_bunny, pumpkin).
jealous(X,Y):-loves(X,Z), loves(Y,Z).
%% jealous(X,Y):-loves(X,Z), loves(Y,Z), X\=Y.


%% ?- jealous(marsellus,W).
%% W = vincent;
%% W = marsellus.
