%% Ερώτημα Α
and_gate(0,0,0).
and_gate(0,1,0).
and_gate(1,0,0).
and_gate(1,1,1).

xor_gate(0,0,0).
xor_gate(0,1,1).
xor_gate(1,0,1).
xor_gate(1,1,0).

half_adder(X,Y,Carry,Sum) :-
        and_gate(X,Y, Carry),
        xor_gate(X,Y,Sum).

%% Ερώτημα Β
or_gate(0,0,0).
or_gate(0,1,1).
or_gate(1,0,1).
or_gate(1,1,1).

full_adder(Carry,Xi,Yi,NextCarry,Si) :-
        half_adder(Xi,Yi,C,S),
        half_adder(Carry, S, C2, Si),
        or_gate(C2,C, NextCarry).

