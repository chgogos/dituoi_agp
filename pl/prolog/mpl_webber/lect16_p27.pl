parent(kim, holly).
parent(margaret, kim).
parent(margaret, kent).
parent(esther, margaret).
parent(herbert, margaret).
parent(herbert, jean).

ancestor(X, Y) :- parent(X, Y). % ο X είναι πρόγονος του Υ
ancestor(X, Y) :-
    parent(Z, Y),
    ancestor(X, Z).