accLen([],Acc,Length):-
    Length = Acc.

accLen([_|L],OldAcc,Length):-
    NewAcc is OldAcc + 1,
    accLen(L,NewAcc,Length).

len2(List,Length):-
    accLen(List,0,Length).

%% ?-accLen([a,b,c],0,Len).
%% Len=3.

%% ?-len2([a,b,c],Len).
%% Len=3.