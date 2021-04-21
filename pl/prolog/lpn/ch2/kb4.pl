house_elf(dobby).
witch(hermione).
witch('McGonagall').
witch(rita_skeeter).
wizard(harry).
magic(X):- house_elf(X).
magic(X):- wizard(X).
magic(X):- witch(X).

%% ?- magic(Hermione).
%% Hermione = dobby;
%% Hermione = harry;
%% Hermione = 'McGonagall';
%% Hermione = rita_skeeter.
