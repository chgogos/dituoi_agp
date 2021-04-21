enjoys(vincent,X):- bigKahunaBurger(X), !, fail.
enjoys(vincent,X):- burger(X).
burger(X):- bigMac(X).
burger(X):- bigKahunaBurger(X).
burger(X):- whopper(X).
bigMac(a).
bigMac(c).
bigKahunaBurger(b).
whopper(d).

%% ?- enjoys(vincent,a).
%% true.

%% ?- enjoys(vincent,b).
%% false.

%% ?- enjoys(vincent,c).
%% true.

%% ?- enjoys(vincent,d).
%% true.

%% μη επιθυμητή συμπεριφορά
%% ?- enjoys(vincent,X).
%% false.
