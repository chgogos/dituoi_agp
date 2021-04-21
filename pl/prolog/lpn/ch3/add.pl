add(0,X,X). 
add(succ(X),Y,succ(Z)):- add(X,Y,Z).

%% add(succ(succ(0)),succ(succ(succ(0))), Result).