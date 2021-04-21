%% tutorialspoint Prolog in AI

animal(dog).
animal(cat).
animal(elephant).
animal(tiger).
animal(cobra).
animal(python).

snake(cobra).
snake(python).

% δεν λειτουργεί σωστά σε όλες τις περιπτώσεις
% likes(mary, X) :- snake(X), !, fail.
% likes(mary, X) :- animal(X).
 
likes(mary, X) :- animal(X), \+ snake(X).

%% likes(mary, dog).
%% true.

%% likes(mary, python).
%% false.

%% ?- likes(mary,X).
%% X = dog ;
%% X = cat ;
%% X = elephant ;
%% X = tiger ;
%% false.