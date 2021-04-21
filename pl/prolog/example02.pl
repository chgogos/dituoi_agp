hold_party(X):-
        birthday(X),
        happy(X).
birthday(tom).
birthday(fred).
birthday(helen).
happy(mary).
happy(jane).
happy(helen).
happy(X) :- birthday(X).

%% Ερώτημα Α
%% ?- birthday(jane).
%% false.

%% Ερώτημα Β
%% ?- hold_party(X).
%% X = helen.

%% Ερώτημα Β με ανίχνευση εκτέλεσης
%% trace.
%% ?- hold_party(X).
%% ...
%% notrace.
%% nodebug.

%% Ερώτημα Γ
%% happy(X) :- birthday(X).

%% εκ νέου εκτέλεση του ερωτήματος hold_party(X)
%% ?- hold_party(X).
%% X = tom ;
%% X = fred ;
%% X = helen ;
%% X = helen.
