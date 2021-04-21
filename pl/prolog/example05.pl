%% Ερώτημα A.1
male(petros).
male(ilias).
male(demos).
male(nikos).
female(sofia).
female(helen).
female(katerina).

%% Ερώτημα A.2
follows(ilias, petros).
follows(petros,ilias).
follows(petros, demos).
follows(petros,sofia).
follows(nikos, petros).
follows(nikos, ilias).
follows(demos, sofia).
follows(demos,petros).
follows(ilias,katerina).
follows(katerina,petros).
follows(sofia,helen).
follows(helen,sofia).

%% Ερώτημα A.3
friends(X,Y):-
        follows(X,Y),
        follows(Y,X).

%% Ερώτημα A.4
male_friends(X,Y):-
        friends(X,Y),
        male(Y).

female_friends(X,Y):-
        friends(X,Y),
        female(Y).
        
%% Ερώτημα A.5
friend_same_gender(X,Y):-
 female(X),
 friends(X,Y),
 female(Y).

friend_same_gender(X,Y):-
 male(X),
 friends(X,Y),
 male(Y).

%% Ερώτημα A.6
recommend_common_friends(X,Y):-
 friends(X,Z),
 friends(Z,Y),
 X \= Y.
 
%% Ερώτημα Β.1
%% ?- follows(X, sofia).
%% X = petros ;
%% X = demos ;
%% X = helen.

%% Ερώτημα Β.2
%% ?- female(X), follows(X,sofia).
%% X = helen ;
%% false.

%% Ερώτημα Β.3
%% ?- friends(X,Y).
%% X = ilias,
%% Y = petros ;
%% X = petros,
%% Y = ilias ;
%% X = petros,
%% Y = demos ;
%% X = demos,
%% Y = petros ;
%% X = sofia,
%% Y = helen ;
%% X = helen,
%% Y = sofia.

%% Ερώτημα Β.4
%% ?- male_friends(X,petros).
%% X = ilias ;
%% X = demos ;
%% false.

%% Ερώτημα Β.5
%% ?- friend_same_gender(X,Y).
%% X = sofia,
%% Y = helen ;
%% X = helen,
%% Y = sofia ;
%% X = petros,
%% Y = ilias ;
%% X = petros,
%% Y = demos ;
%% X = ilias,
%% Y = petros ;
%% X = demos,
%% Y = petros ;
%% false.

%% Ερώτημα Β.6
%% ?- recommend_common_friends(ilias,Y).
%% Y = demos ;
%% false.