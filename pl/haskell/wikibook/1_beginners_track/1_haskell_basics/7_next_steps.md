# Επόμενα βήματα

## if/then/else

Αν και υπάρχει η συνάρτηση signum που επιστρέφει το πρόσημο μιας αριθμητικής τιμής, θα υλοποιήσουμε τη δική μας συνάρτηση mySignum.

```
mySignum x =
    if x < 0 
        then -1
        else if x > 0
            then 1
            else 0
```

[mySignum.hs](./mySignum.hs)

Παραδείγματα με τη mySignum.

```
*Main> mySignum 5
1
*Main> mySignum 0
0
*Main> mySignum (5 - 10)
-1
*Main> mySignum (-1)
-1
```

Οι παρενθέσεις στο -1 του τελευταίου παραδείγματος είναι υποχρεωτικές, αλλιώς η Haskell θα επιχειρούσε να αφαιρέσει από τη συνάρτηση mySignum την τιμή 1.

Η if/then/else της Haskell είναι διαφορετική από την if προστακτικών γλωσσών. Στην περίπτωση της Haskell πρέπει πάντα να υπάρχει πρόταση then και πρόταση else, καθώς θα πρέπει η δομή να επιστρέφει αποτέλεσμα και στις δύο περιπτώσεις, το οποίο μάλιστα να είναι του ίδιου τύπου και στις δύο περιπτώσεις.

Εναλλακτικά, και μάλλον απλούστερα, η συνάρτηση mySignum μπορεί να υλοποιηθεί με φρουρούς.

```
mySignum x
    | x < 0     = -1
    | x > 0     = 1
    | otherwise = 0
```

[mySignumGuards.hs](./mySignumGuards.hs)

## Pattern matching

Έστω το ακόλουθο πρόγραμμα που αποδίδει πόντους σε διαγωνιζόμενους ανάλογα με τη θέση τερματισμού τους ως εξής:

* 10 πόντους για το νικητή
* 6 πόντους για τον δεύτερο
* 4 πόντους για τον τρίτο
* 3 πόντους για τον τέταρτο
* 2 πόντους για τον πέμπτο
* 1 πόντο για τον έκτο
* κανένα πόντο για τους υπόλοιπους

Η συνάρτηση μπορεί να γραφεί με την if/then/else ως εξής

```
pts :: Int -> Int
pts x =
    if x == 1
        then 10
        else if x == 2
            then 6
            else if x == 3
                then 4
                else if x == 4
                    then 3
                    else if x == 5
                        then 2
                        else if x == 6
                            then 1
                            else 0
```

[pointsIfThenElse.hs](./pointsIfThenElse.hs)

Με τη χρήση pattern matching ο κώδικας είναι απλούστερος καθώς το όρισμα της συνάρτησης εξετάζεται αν ταιριάζει με τον αριθμό που βρίσκεται σε κάθε σειρά αριστερά του =. Στην τελευταία σειρά το σύμβολο  _ είναι ειδικός χαρακτήρας και σημαίνει "οτιδήποτε".

```
pts :: Int -> Int
pts 1 = 10
pts 2 = 6
pts 3 = 4
pts 4 = 3
pts 5 = 2
pts 6 = 1
pts _ = 0
```

[pointsPatternMatching.hs](./pointsPatternMatching.hs)


Μπορούμε να συνδυάσουμε τα στυλ γραφής (π.χ. pattern matching και guards)


```
pts :: Int -> Int
pts 1 = 10
pts 2 = 6
pts x
    | x <= 6    = 7 - x
    | otherwise = 0
```

[pointsMix.hs](./pointsMix.hs)

**Παράδειγμα ορισμού της συνάρτησης τελεστή (||) με pattern matching**

```
(||) :: Bool -> Bool -> Bool
False || False = False
_     || _     = True
```
[or.hs](./or.hs)

ή 

```
(||) :: Bool -> Bool -> Bool
True  || _ = True
False || y = y
```
[orAlt.hs](./orAlt.hs)

αλλά αυτό είναι λάθος

```
(&&) :: Bool -> Bool -> Bool
x && x = x -- oops!
_ && _ = False
```

[orWrong.hs](./orWrong.hs)

## Patterns σε λίστες και πλειάδες

Υλοποίηση της fst με δική μας συνάρτηση

```
fst' :: (a, b) -> a
fst' (x, _) = x
```

[myfst.hs](./myfst.hs)

```
head             :: [a] -> a
head (x:_)       =  x
head []          =  error "Prelude.head: empty list"

tail             :: [a] -> [a]
tail (_:xs)      =  xs
tail []          =  error "Prelude.tail: empty list"
```

[my_head_tail.hs](./my_head_tail.hs)

## let bindings (προσδέσεις)

Οι προσδέσεις let αποτελούν εναλλακτική των προτάσεων where έτσι ώστε να πραγματοποιούνται τοπικές δηλώσεις.

Παράδειγμα: εύρεση πραγματικών λύσεων δευτεροβάθμιας εξίσωσης ax^2+bx+c=0

```
roots a b c =
    ((-b + sqrt(b * b - 4 * a * c)) / (2 * a),
     (-b - sqrt(b * b - 4 * a * c)) / (2 * a))
```

[roots.hs](./roots.hs)

με χρήση let bindings

```
roots a b c =
    let sdisc = sqrt (b * b - 4 * a * c)
    in  ((-b + sdisc) / (2 * a),
         (-b - sdisc) / (2 * a))
```

[roots_let_bindings.hs](./roots_let_bindings.hs)

ή ακόμα και με πολλαπλά let bindings


```
roots a b c =
    let sdisc = sqrt (b * b - 4 * a * c)
        twice_a = 2 * a
    in  ((-b + sdisc) / twice_a,
         (-b - sdisc) / twice_a)
```

[roots_many_let_bindings.hs](./roots_many_let_bindings.hs)

