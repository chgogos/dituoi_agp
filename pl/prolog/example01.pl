likes(john,mary).
likes(john,trains).
likes(peter,fast_cars).
likes(Person1,Person2):-
    hobby(Person1,Hobby),
    hobby(Person2,Hobby).

hobby(john,trainspotting).
hobby(tim,sailing).
hobby(helen,trainspotting).
hobby(simon,sailing).

%% Ερώτημα Α
%% ?- likes(trains,john).
%% false.

%% ?- likes(helen,john).
%% true.

%% ?- likes(tim,helen).
%% false.

%% ?- likes(john,X).
%% X = mary ;
%% X = trains ;
%% X = john ;
%% X = helen.

%% Ερώτημα B
%% ?- trace.
%% true.
%% [trace] ?- likes(john, X).
%%    Call: (8) likes(john, _3072) ? creep
%%    Exit: (8) likes(john, mary) ? creep
%% X = mary ;
%%    Redo: (8) likes(john, _3072) ? creep
%%    Exit: (8) likes(john, trains) ? creep
%% X = trains ;
%%    Redo: (8) likes(john, _3072) ? creep
%%    Call: (9) hobby(john, _3286) ? creep
%%    Exit: (9) hobby(john, trainspotting) ? creep
%%    Call: (9) hobby(_3072, trainspotting) ? creep
%%    Exit: (9) hobby(john, trainspotting) ? creep
%%    Exit: (8) likes(john, john) ? creep
%% X = john ;
%%    Redo: (9) hobby(_3072, trainspotting) ? creep
%%    Exit: (9) hobby(helen, trainspotting) ? creep
%%    Exit: (8) likes(john, helen) ? creep
%% X = helen.

%% Ερώτημα Γ
%% likes(X,trains) :- hobby(X,trainspotting).