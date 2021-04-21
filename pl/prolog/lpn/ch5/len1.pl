len1([],0).
len1([_|L],N):-
    len1(L,X),
    N is X + 1.

%% ?- len1([a,b,c,d,e,[a,x],t],X).
%% X=7.