woman(mia).
woman(jody).
woman(yolanda).
loves(vincent, mia).
loves(marsellus, mia).
loves(pumpkin, honey_bunny).
loves(honey_bunny, pumpkin).

%% ?- woman(X).
%% X = mia;
%% X = jody;
%% X = yolanda.

%% ?- loves(marsellus,X), woman(X).
%% X= mia.

%% ?- loves(pumpkin,X), woman(X).
%% false.
