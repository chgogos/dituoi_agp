friends(X,Y):-
        follows(X,Y),
        follows(Y,X).

male_friends(X,Y):-
        friends(X,Y),
        male(Y).

follows(ilias, petros).
follows(petros,ilias).
follows(petros, demos).
follows(demos,petros).
follows(petros,sofia).

male(ilias).
male(demos).

% ?- trace.
% true.

% [trace]  ?- male_friends(petros,A).
%    Call: (8) male_friends(petros, _4796) ? creep
%    Call: (9) friends(petros, _4796) ? creep
%    Call: (10) follows(petros, _4796) ? creep
%    Exit: (10) follows(petros, ilias) ? creep
%    Call: (10) follows(ilias, petros) ? creep
%    Exit: (10) follows(ilias, petros) ? creep
%    Exit: (9) friends(petros, ilias) ? creep
%    Call: (9) male(ilias) ? creep
%    Exit: (9) male(ilias) ? creep
%    Exit: (8) male_friends(petros, ilias) ? creep
% A = ilias ;
%    Redo: (10) follows(petros, _4796) ? creep
%    Exit: (10) follows(petros, demos) ? creep
%    Call: (10) follows(demos, petros) ? creep
%    Exit: (10) follows(demos, petros) ? creep
%    Exit: (9) friends(petros, demos) ? creep
%    Call: (9) male(demos) ? creep
%    Exit: (9) male(demos) ? creep
%    Exit: (8) male_friends(petros, demos) ? creep
% A = demos ;
%    Redo: (10) follows(petros, _4796) ? creep
%    Exit: (10) follows(petros, sofia) ? creep
%    Call: (10) follows(sofia, petros) ? creep
%    Fail: (10) follows(sofia, petros) ? creep
%    Fail: (9) friends(petros, _4796) ? creep
%    Fail: (8) male_friends(petros, _4796) ? creep
% false.
