factorial(0,1).
factorial(N,F) :-
    N>0,       % για να αποφευχθούν κλήσεις με αρνητικό Ν
    N1 is N-1,
    factorial(N1,F1),
    F is F1*N.

%% ?- factorial(5, F).
%% F = 120.