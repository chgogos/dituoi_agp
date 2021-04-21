woman(helen).
woman(maria).
woman(sofia).
loves(nikos, helen).    % ο Νίκος αγαπά την Ελένη
loves(helen, nikos).    % η Ελένη αγαπά τον Νίκο
loves(panos, helen).
loves(petros, viki).
loves(viki, petros).
jealous(X,Y):-
        loves(X,Z),
        loves(Y,Z),
        X \= Y.
        
% Ερώτημα Α
% γεγονότα: 8
% κανόνες: 1
% προτάσεις: 9
% κατηγορήματα: 3 (woman/1, loves/2, jealous/3)
% μεταβλητές: 2 (Χ,Υ)
% Αν ο Χ και ο Υ αγαπούν κάποιον Ζ τότε ο Χ ζηλεύει τον Υ

% Ερώτημα Β
% ?- woman(X).
% X = helen ;
% X = maria ;
% X = sofia.

% ?- loves(panos,X), woman(X).
% X = helen.

% ?- loves(petros,X), woman(X).
% false.

% ?- jealous(panos,X).
% X = nikos ;
% X = panos.

% Ερώτημα Γ
woman_loved(Y) :- loves(_,Y), woman(Y).
% X = helen ;
% X = helen ;
% false.
