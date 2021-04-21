bigger(elephant, horse).
bigger(horse, donkey).
bigger(donkey, dog).
bigger(dog, monkey).
is_bigger(X,Y):-bigger(X,Y).
is_bigger(X,Y):-bigger(X,Z), is_bigger(Z,Y).

% Ερώτημα A
% ?- is_bigger(elephant, monkey).
% true.

% ?- is_bigger(X,donkey).
% X = horse ;
% X = elephant ;
% false.

% Ερώτημα B
% ?- is_bigger(X,monkey), is_bigger(donkey,X).
% X = dog ;
% false.