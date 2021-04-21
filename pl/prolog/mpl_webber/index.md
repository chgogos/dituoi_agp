## Prolog

## Εισαγωγή στη γλώσσα Prolog

Παραδείγματα από τα Κεφάλαια 19 έως και 22 του συγγράμματος: [Σύγχρονες Γλώσσες Προγραμματισμού, Μια Πρακτική Εισαγωγή, Adam Brooks Webber, Πανεπιστημιακές Εκδόσεις Κρήτης](https://www.cup.gr/book/sigchrones-glosses-programmatismou/)

**Πρόσδεση μεταβλητών**

Μια μεταβλητή μπορεί να είναι προσδεμένη (bound) ή μη-προσδεμένη (unbound). Αν μια μεταβλητή έχει προσδεθεί η τιμή της δεν αλλάζει.

```
Χ = 1, Χ = 2.
false.
```

**Γεγονότα και κατηγορήματα**

Τα γεγονότα:
```
parent(kim, holly).  % ο γονέας της holly είναι η kim
parent(margaret, kim).
parent(margaret, kent).
parent(esther, margaret).
parent(herbert, margaret).
parent(herbert, jean).
```
στο αρχείο [lect16_p11.pl](./lect16_p11.pl) αποτελούν μια βάση γνώσης που ορίζει το κατηγόρημα parent/2

**Ενεργοποίηση διερμηνέα της Prolog**

Εγκατάσταση της SWI-Prolog. Εκτέλεση της εντολής:

```
> swipl
Welcome to SWI-Prolog (threaded, 64 bits, version 8.2.4)
SWI-Prolog comes with ABSOLUTELY NO WARRANTY. This is free software.
Please run ?- license. for legal details.

For online help and background, visit https://www.swi-prolog.org
For built-in help, use ?- help(Topic). or ?- apropos(Word).

1 ?-
```

**Φόρτωση βάσης γνώσης**

```
?- consult(lect16_p11.pl).
```

εναλλακτικά μπορεί να γίνει και με 

```
?- [lect16_p11].
```

**Απλές ερωτήσεις**

```
?- parent(margaret, kent).
true.

?- parent(fred, pebbles).
false.
```

**Ερωτήσεις με μεταβλητές**

```
?- parent(P, jean).
P = herbert.
?- parent(P, esther).
false.
```

**Συζεύξεις**

```
?- parent(margaret, X), parent(X, holly).
X = kim ;
false.
```

**Πολλαπλές λύσεις**

```
?- parent(margaret, Child).
Child = kim ;
Child = kent.
```

```
?- parent(Parent, kim), parent(GrandParent, Parent).
Parent = margaret
GrandParent = esther ;
Parent = margaret
GrandParent = herbert ;
false.
```

**Κανόνες**

Τα γεγονότα και ο κανόνας:

```
parent(kim, holly).
parent(margaret, kim).
parent(margaret, kent).
parent(esther, margaret).
parent(herbert, margaret).
parent(herbert, jean).

greatgrandparent(GGP, GGC) :-
    parent(GGP, GP),
    parent(GP, P), parent(P, GGC).
```

στο πρόγραμμα [lect16_p23.pl](./lect16_p23.pl) ορίζουν 7 προτάσεις εκ των οποίων οι 6 είναι γεγονότα και 1 είναι κανόνας. Με τον τρόπο αυτό ορίζονται τα κατηγορήματα parent/2 και greatgrandparent/2.

Στο ερώτημα

```
?- greatgrandparent(esther, GreatGrandChild).
```

προκαλείται η ακόλουθη πρόσδεση μεταβλητών

```
GGP = esther.
GP = margaret.
GGC = holly.
```

**Κανόνες που ορίζονται βάσει άλλων κανόνων**

```
parent(kim, holly).
parent(margaret, kim).
parent(margaret, kent).
parent(esther, margaret).
parent(herbert, margaret).
parent(herbert, jean).

greatgrandparent(GGP, GGC) :-
    parent(GGP, GP),
    parent(GP, P), parent(P, GGC).
```

[lect16_p26.pl](./lect16_p26.pl)


**Αναδρομικοί κανόνες**

```
parent(kim, holly).
parent(margaret, kim).
parent(margaret, kent).
parent(esther, margaret).
parent(herbert, margaret).
parent(herbert, jean).

ancestor(X, Y) :- parent(X, Y). % ο X είναι πρόγονος του Υ
ancestor(X, Y) :-
    parent(Z, Y),
    ancestor(X, Z).
```

[lect16_p27.pl](./lect16_p27.pl)

```
?- ancestor(jean, jean).
false.

?- ancestor(kim, holly).
true.

?- ancestor(A, holly).
A = kim ;
A = margaret ;
A = esther ;
A = herbert ;
false.
```

**Η διαδικαστική όψη και η λογική όψη της Prolog**

```
greatgrandparent(GGP, GGC) :-
    parent(GGP, GP),
    parent(GP, P),
    parent(P, GGC).
```

Διαδικαστική όψη: Για να αποδείξουμε greatgrandparent(GGP,GGC), πρέπει να βρούμε τιμές για τα GGP, GGC, GP και P για τις οποίες μπορούμε να αποδείξουμε πρώτα ότι parent(GGP,GP), μετά ότι parent(GP,P) και τελικά ότι parent(P,GGC).

Λογική όψη: Aν ισχύει parent(GGP, GP) και parent(GP, P) και parent(P, GGC) τότε συνεπάγεται greatgrandparent(GGP, GGC)

Ο προγραμματισμός καθίσταται  ανώτερου επιπέδου καθώς ο προγραμματιστής απλώς περιγράφει τις  προδιαγραφές του προβλήματος και η εκτέλεση υποστηρίζεται από το σύστημα υλοποίησης.


### Τελεστές της Prolog

**Το κατηγόρημα =/2**

```
?- =(parent(adam,seth), parent(adam,X)).
X = seth.
```

μπορεί να γραφεί και ως εξής:

```
?- parent(adam,seth) = parent(adam,X).
X = seth.
```

**Αριθμητικοί τελεστές**

```
?- X = +(1,*(2,3)).
X = 1+2*3.
?- X = 1+2*3.
X = 1+2*3.
```

### Λίστες

**Κεφαλή και ουρά λίστας**

```
?- A = [1,2,3,4].
A = [1,2,3,4].

?- [1|A] = [1,2,3,4].
A = [2,3,4]. 

?- [A,B|C] = [1,2,3,4].
A = 1,
B = 2,
C = [3, 4].

?- [A,B|C] = [1,2].
A = 1,
B = 2,
C = [].
```

**Το κατηγόρημα append**

```
?- append([1,2], [3,4], Z).
Z = [1, 2, 3, 4].


?- append(X, [3,4], [1,2,3,4]).
X = [1, 2] ;
false.

?- append(X, Y, [1,2,3]).
X = []
Y = [1, 2, 3] ;
X = [1]
Y = [2, 3] ;
X = [1, 2]
Y = [3] ;
X = [1, 2, 3]
Y = [] ;
false.
```

Υλοποίηση του κατηγορήματος append

```
append([], L, L).
append([H|L1], L2, [H|L3]) :-
    append(L1, L2, L3).
```
[lect16_p47.pl](./lect16_p47.pl)

Άλλα κατηγορήματα για λίστες:

* member(X,Y) Επιτυγχάνει εάν η λίστα Y έχει ως μέλος τον όρο X.
* select(X,Y,Z) Επιτυγχάνει εάν η λίστα Y περιέχει το X ως μέλος, και ο όρος Z είναι ο ίδιος με τη λίστα Y αλλά χωρίς ένα στιγμιότυπο του όρου X.
* nth0(N,L,X) Επιτυγχάνει εάν ο N είναι ένας μη αρνητικός ακέραιος, L μια λίστα, και το X είναι το N-οστό στοιχείο της λίστας L, αρχίζοντας την αρίθμηση από το 0.
* length(L,N) Επιτυγχάνει εάν ο όρος L είναι μια λίστα με μήκος N.
* reverse(X,Y) Επιτυγχάνει εάν ο όρος Y ενοποιείται με την αναστροφή της λίστας X. 
* sort(X,Y) Επιτυγχάνει όταν o όρος Y είναι το ταξινομημένο X. (μη αναστρέψιμο)

**Ανώνυμες μεταβλητές**

Οι ανώνυμες μεταβλητές συμβολίζονται με την κάτω παύλα

```
member(X, [X|_]).
member(X, [_|T]) :-
    member(X, T).
```

[lect16_p55.pl](./lect16_p55.pl)

```
?- member(b, [a,b,c]).
true ;
false.
?- member(d, [a,b,c]).
false.
?- member(X, [a,b]).
X = a ;
X = b.
```

**Το κατηγόρημα \+/1**

```
?- member(1, [1,2,3]).
true ;
false.

?- \+ member(4, [1,2,3]).
true.
```

**Παράδειγμα (negation as failure)**

```
parent(kim, holly).
parent(margaret, kim).
parent(margaret, kent).
parent(esther, margaret).
parent(herbert, margaret).
parent(herbert, jean).

sibling(X, Y) :-
    \+ (X = Y),
    parent(P, X),
    parent(P, Y).
```
[lect16_p59a.pl](./lect16_p59a.pl)

```
?- sibling(kim, kent).
true.
?- sibling(kim, kim).
false.
?- sibling(X, Y).
false.
```

```
parent(kim, holly).
parent(margaret, kim).
parent(margaret, kent).
parent(esther, margaret).
parent(herbert, margaret).
parent(herbert, jean).

sibling(X, Y) :-
    parent(P, X),
    parent(P, Y).
    \+ (X = Y),
```
[lect16_p59b.pl](./lect16_p59b.pl)

```
?- sibling(X, Y).
X = kim
Y = kent ;
X = kent
Y = kim ;
X = margaret
Y = jean ;
X = jean
Y = margaret ;
false.
```

## Το πρόβλημα λογικής: Λύκος - Κατσίκα - Λάχανο

```
change(e, w).
change(w, e).

move([X,X,Goat,Cabbage], wolf, [Y,Y,Goat,Cabbage]) :-
    change(X, Y).
move([X,Wolf,X,Cabbage], goat, [Y,Wolf,Y,Cabbage]) :-
    change(X, Y).
move([X,Wolf,Goat,X], cabbage, [Y,Wolf,Goat,Y]) :-
    change(X, Y).
move([X,Wolf,Goat,Cab], nothing, [Y,Wolf,Goat,Cab]) :-
    change(X, Y).

guarded_or_separated(X, X, X).
guarded_or_separated(_, Y, Z) :- Y \= Z.

safe([Man, Wolf, Goat, Cabbage]) :-
    guarded_or_separated(Man, Goat, Wolf),
    guarded_or_separated(Man, Goat, Cabbage).

solution([e,e,e,e], []).
solution(Config, [Move|Moves]) :-
    move(Config, Move, NextConfig),
    safe(NextConfig),
    solution(NextConfig, Moves).
```

[lect16_p65.pl](./lect16_p65.pl)

```
?- length(L, Ν), solution([w,w,w,w], L).
```