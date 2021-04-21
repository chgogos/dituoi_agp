enjoys(vincent,X):- burger(X),
    \+ bigKahunaBurger(X).
burger(X):- bigMac(X).
burger(X):- bigKahunaBurger(X).
burger(X):- whopper(X).
bigMac(a).
bigMac(c).
bigKahunaBurger(b).
whopper(d).

%% ?- enjoys(vincent,X).
%% X = a ;
%% X = c ;
%% X = d.
