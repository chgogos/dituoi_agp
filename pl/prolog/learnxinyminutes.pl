% https://learnxinyminutes.com/docs/prolog/

magicNumber(7).
magicNumber(9).
magicNumber(42).

nearby(X,Y) :- X = Y.
nearby(X,Y) :- Y is X+1.
nearby(X,Y) :- Y is X-1.

nearbychk(X,Y) :- X = Y, !.
nearbychk(X,Y) :- Y is X+1, !.
nearbychk(X,Y) :- Y is X-1.

nearby2(X,Y) :- nonvar(X), X = Y.
nearby2(X,Y) :- nonvar(X), Y is X+1.
nearby2(X,Y) :- nonvar(X), Y is X-1.
nearby2(X,Y) :- var(X), nonvar(Y), nearby2(Y,X).

nearby3(X,Y) :- nonvar(X), nonvar(Y), nearby2(X,Y), !.
nearby3(X,Y) :- nearby2(X,Y).

countTo(X) :- countUpTo(1,X).
countUpTo(Value, Limit) :- Value = Limit, writeln(Value), !.
countUpTo(Value, Limit) :- Value \= Limit, writeln(Value),
    NextValue is Value+1,
    countUpTo(NextValue, Limit).

countUpTo2(Value, Limit) :- writeln(Value),
    Value = Limit -> true ; (
        NextValue is Value+1,
        countUpTo2(NextValue, Limit)).

countTo2(X) :- forall(between(1,X,Y),writeln(Y)).

safe(Group) :- memberchk(joker, Group) -> memberchk(batman, Group) ; true.