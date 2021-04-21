%% max1 = μη αποδοτικό max
max1(X,Y,Y):- X =< Y.
max1(X,Y,X):- X > Y.

%% max2 = αποδοτικό max με χρήση cut
max2(X,Y,Y):- X =< Y, !.
max2(X,Y,X):- X > Y.

%% max3 = αποδοτικό max με χρήση cut και unification μετά το cut
max3(X,Y,Y):- X =< Y, !, Y = Z.
max3(X,Y,X).

%% ?- max1(2,3,2).
%% false.

%% ?- max1(2,3,X).
%% X=3. 

%% ?- max2(2,3,X).
%% X=3.

%% ?- max3(2,3,2).
%% false.
