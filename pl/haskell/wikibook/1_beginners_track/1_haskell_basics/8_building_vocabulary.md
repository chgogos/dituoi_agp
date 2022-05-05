# Ενίσχυση "λεξιλογίου" συναρτήσεων

## Σύνθεση συναρτήσεων

Σύνθεση συναρτήσεων είναι η εφαρμογή μιας συνάρτησης σε μιαν τιμή και στη συνέχει η εφαρμογή μιας άλλης συνάρτησης στο αποτέλεσμα.

Παράδειγμα: απλές συναρτήσεις

```
f x = x + 3
square x = x ^ 2
```

μπορούμε να τις συνθέσουμε με δύο διαφορετικούς τρόπους, ανάλογα με το ποια συνάρτηση εφαρμόζουμε πρώτη.

```
Prelude> square (f 1)
16
Prelude> square (f 2)
25
Prelude> f (square 1)
4
Prelude> f (square 2)
7
```

Οι παρενθέσεις είναι υποχρεωτικές αλλιώς ο διερμηνευτής θα αποτιμούσε το square f και το f square, αντίστοιχα και θα επέστρεφε σφάλμα.

Η σύνθεση δύο συναρτήσεων μπορεί να χρησιμοποιηθεί για να οριστεί μια νέα συνάρτηση στην οποία μπορούμε να αποδώσουμε και όνομα.

```
squareOfF x = square (f x)

fOfSquare x = f (square x)
```

Υπάρχει και ένας δεύτερος, κομψός τρόπος, για σύνθεση συναρτήσεων. Χρησιμοποιεί τον τελεστή σύνθεση συναρτήσεων (.) και γίνεται απλά τοποθετώντας μια τελεία ανάμεσα σε δύο συναρτήσεις. Παρατηρήστε την αναλογία με τον τελεστή σύνθεσης των μαθηματικών συναρτήσεων.

Παράδειγμα: σύθεση συναρτήσεων με (.)
```
squareOfF x = (square . f) x

fOfSquare x = (f . square) x
```

Η σύνθεση των συναρτήσεων θα μπορούσε να γίνει και χωρίς την παράμετρο x.
```
squareOfF = square . f
```

## Ανάγκη γνώσης "λεξιλογίου" συναρτήσεων

Ο προγραμματιστής θα πρέπει να γνωρίζει πως μπορεί να βρει χρήσιμες συναρτήσεις στις βιβλιοθήκες της γλώσσας (packaged κώδικας).

## Το Prelude και οι βιβλιοθήκες

Το Prelude αποτελεί τη βασική βιβλιοθήκη που φορτώνεται αυτόματα κατά την εκκίνηση κάθε Haskell προγράμματος. Οι άλλες βιβλιοθήκες είναι διαθέσιμες ως modules που μπορούν να γίνουν import. Για παράδειγμα για να χρησιμοποιηθεί η συνάρτηση permutations από το module Data.List προσθέτουμε τη γραμμή import Data.List στην κορυφή του .hs αρχείου

```
import Data.List

testPermutations = permutations "abc"
```
[permutationsExample.hs](./perrmutationsExample.hs)

Για γρήγορη δοκιμή από το ghci μπορεί να χρησιμοποιηθεί η εντολή :m +Data.List για φόρτωση του module Data.List.

```
Prelude> :m +Data.List
Prelude Data.List> :t permutations
permutations :: [a] -> [[a]]
```

## Ένα δείγμα απλοποίησης κώδικα με χρήση συναρτήσεων βιβλιοθηκών

Έστω ότι ζητείται η συγγραφή συνάρτησης που δέχεται ένα λεκτικό που αποτελείται από λέξεις που χωρίζονται μεταξύ τους με κενά και επιστρέφει το λεκτικό με την αντίστροφη σειρά λέξεων. Για παράδειγμα το "Mary had a little lamb" να γίνεται "lamb little a had Mary".

```
monsterRevWords :: String -> String
monsterRevWords input = rejoinUnreversed (divideReversed input)
    where
    divideReversed s = go1 [] s
        where
        go1 divided [] = divided
        go1 [] (c:cs)
            | testSpace c = go1 [] cs
            | otherwise   = go1 [[]] (c:cs)
        go1 (w:ws) [c]
            | testSpace c = (w:ws)
            | otherwise   = ((c:w):ws)
        go1 (w:ws) (c:c':cs)
            | testSpace c =
                if testSpace c'
                    then go1 (w:ws) (c':cs)
                    else go1 ([c']:w:ws) cs
            | otherwise = go1 ((c:w):ws) (c':cs)
    testSpace c = c == ' '
    rejoinUnreversed [] = []
    rejoinUnreversed [w] = reverseList w
    rejoinUnreversed strings = go2 (' ' : reverseList newFirstWord) (otherWords)
        where
        (newFirstWord : otherWords) = reverseList strings
        go2 rejoined ([]:[]) = rejoined
        go2 rejoined ([]:(w':ws')) = go2 (rejoined) ((' ':w'):ws')
        go2 rejoined ((c:cs):ws) = go2 (c:rejoined) (cs:ws)
    reverseList [] = []
    reverseList w = go3 [] w
        where
        go3 rev [] = rev
        go3 rev (c:cs) = go3 (c:rev) cs
```

[monsterRevWords.hs](./monsterRevWords.hs)

Ο κώδικας μπορεί να γραφείν πολύ απλούστερα με χρήση των ακόλουθων συναρτήσεων του Prelude.

* words, χωρίζει ένα λεκτικό με βάση τα κενά του σε μια λίστα λεκτικών
* reverse, αντιστρέφει μια λίστα 
* uwords, κάνει το αντίστροφο από τη words

```
revWords :: String -> String
revWords input = (unwords . reverse . words) input
```

## Πόροι

Το [hoogle](https://hoogle.haskell.org/) επιτρέπει την αναζήτηση συναρτήσεων στις βιβλιοθήκες της γλώσσας είτε με το όνομα της συνάρτησης (π.χ. length), είτε με τον τύπο της συνάρτησης (π.χ. [a] -> Int που σημαίνει συνάρτηση από λίστα σε ακέραιο).

Πέρα από τις βιβλιοθήκες που περιλαμβάνονται στο GHC, υπάρχει ένα μεγάλο οικοσύστημα βιβλιοθηκών, που είναι διαθέσιμο μέσω του [Hackage](https://hackage.haskell.org/) και το οποίο μπορεί να εγκατασταθεί με το λογισμικό [cabal](https://cabal.readthedocs.io/en/3.6/#).
