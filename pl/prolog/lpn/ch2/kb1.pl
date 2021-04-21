vertical( line(point(X,_Y), point(X,_Z))).
horizontal( line(point(_X,Y), point(_Z,Y))).

%% ?- vertical(line(point(1,1),point(1,3))).
%% true.

%% ?- vertical(line(point(1,1),point(3,2))).
%% false.

%% ?- horizontal(line(point(1,1),point(1,Y))).
%% Y = 1.

%% ?- horizontal(line(point(2,3),Point)).
%% Point = point(_4494, 3).