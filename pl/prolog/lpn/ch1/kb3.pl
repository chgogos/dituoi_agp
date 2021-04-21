happy(vincent).
listens2music(butch).
playsAirGuitar(vincent):- listens2music(vincent), happy(vincent).
playsAirGuitar(butch):- happy(butch).
playsAirGuitar(butch):- listens2music(butch).
%% εναλλακτική γραφή των 2 παραπάνω προτάσεων
%% playsAirGuitar(butch):- happy(butch);listens2music(butch).


%% ?- playsAirGuitar(vincent).
%% false.

%% ?- playsAirGuitar(butch).
%% true.