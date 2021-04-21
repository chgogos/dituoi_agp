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

get_and_gate :-
        and_gate(X,Y,Z),
        format('~w AND ~w = ~w ~n', [X,Y,Z]).

%% Ερώτημα Β
or_gate(0,0,0).
or_gate(0,1,1).
or_gate(1,0,1).
or_gate(1,1,1).

full_adder(Carry,Xi,Yi,NextCarry,Si) :-
        half_adder(Xi,Yi,C,S),
        half_adder(Carry, S, C2, Si),
        or_gate(C2,C, NextCarry).

%% Ερώτημα Γ
adder_3_digits(C0,A2,A1,A0, B2,B1,B0,C3,S2,S1,S0):-
        full_adder(C0,A0,B0,C1,S0),
        full_adder(C1,A1,B1,C2,S1),
        full_adder(C2,A2,B2,C3,S2).
