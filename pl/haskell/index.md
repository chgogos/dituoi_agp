# Haskell

H Haskell είναι μια αμιγής συναρτησιακή γλώσσα προγραμματισμού οκνηρής αποτίμησης. 

Παραδείγματα κώδικα από το "7 Languages in 7 Week, by Bruce Tate"

```
ghci
GHCi, version 8.0.2: http://www.haskell.org/ghc/  :? for help
Prelude> :quit
```

## Εκφράσεις και βασικοί τύποι

**Αριθμοί**

```hs
Prelude> 1 + 2
3
Prelude> (+) 1 2
3
Prelude> 1 + 2 * 3
7
Prelude> 1 + 2 * 3.0
7.0
Prelude> 2 ^ 10
1024
Prelude> div 10 3
3
Prelude> mod 10 3
1
```

**Λεκτικά**

```hs
Prelude> "hi"
"hi"
Prelude> "hello " ++ "world"
"hello world"
```

**Χαρακτήρες**

Ένα λεκτικό είναι μια λίστα χαρακτήρων.

```hs
Prelude> 'a'
'a'
Prelude> ['a', 'b']
"ab"
```

**Boolean**

```hs
Prelude> 1 == 2-1
True
Prelude> 1 /= 1
False
```

## Συναρτήσεις

Πρόσδεση της μεταβλητής x σε τοπική εμβέλεια.

```hs
Prelude> let x = 42
Prelude> x
42
```

Πρόσδεση της συνάρτησης times2 σε τοπική εμβέλεια.

```hs
Prelude> let times2 x = 2 * x
Prelude> times2 21
42
```

```hs
times2 :: Integer -> Integer
times2 x = 2 * x
```
[times2.hs](./times2.hs)

Φόρτωση κώδικα και κλήση συνάρτησης.

```
$ ghci
GHCi, version 8.0.2: http://www.haskell.org/ghc/  :? for help
Prelude> :load times2.hs
*Main> times2 10
20
:quit
```

## Αναδρομή

```hs
Prelude> let fact x = if x == 0 then 1 else fact (x - 1) * x
Prelude> fact 3
6
```

**Αντιστοίχιση μοτίβων (pattern matching)**

```hs
fact :: Integer -> Integer
fact 0 = 1
fact x = x * fact (x - 1)
```

[fact_pattern_matching.hs](./fact_pattern_matching.hs)

**Φρουροί (guards)**

Οι φρουροί είναι συνθήκες που περιορίζουν τις τιμές των ορισμάτων όπως στη συνέχεια. Όταν η συνθήκη ενός φρουρού ικανοποιείται η Haskell καλεί την κατάλληλη συνάρτηση.

```hs
fact :: Integer -> Integer
fact x
    | x > 1 = x * fact (x-1)
    | otherwise 1
```

[fact_guards.hs](./fact_guards.hs)

## Πλειάδες και λίστες

**Πρώτο (fst) και δεύτερο (snd) στοιχείο σε πλειάδα**

```hs
Prelude> fst (1,2)
1
Prelude> snd (1,2)
2
```

Συνάρτηση εύρεσης όρων της ακολουθίας fibonacci.

```hs
fib :: Integer -> Integer
fib 0 = 1
fib 1 = 1
fib x = fib (x - 1) + fib (x - 2)
```
[fib_pattern_matching.hs](./fib_pattern_matching.hs)

```hs
*Main> fib 10
10946
```

Υλοποίηση ταχύτερης έκδοσης της συνάρτησης fib (με χρήση πλειάδων).


```hs
fibTuple :: (Integer, Integer, Integer) -> (Integer, Integer, Integer)
fibTuple (x, y, 0) = (x, y, 0)
fibTuple (x, y, index) = fibTuple (y, x + y, index - 1)

fibResult :: (Integer, Integer, Integer) -> Integer
fibResult (x, y, z) =x

fib :: Integer -> Integer
fib x = fibResult (fibTuple (0, 1, x))
```
[fib_tuples.hs](./fib_tuples.hs)

```hs
*Main> fib 100
354224848179261915075
```

**head, tail, init, last σε λίστες**

```hs
Prelude> head [1,2,3,4]
1
Prelude> tail [1,2,3,4]
[2,3,4]
Prelude> let (h:t) = [1,2,3,4]
Prelude> h
1
Prelude> t
[2,3,4]
Prelude> init [1,2,3,4]
[1,2,3]
Prelude> last [1,2,3,4]
4
```

**Σύνθεση (composition)**

```hs
Prelude> let second = head . tail
Prelude> second [1,2,3]
second = 2
```

## Διάσχιση λιστών

**Μέγεθος λίστας**

```hs
size [] = 0
size (h:t) = 1 + size t
```
[size.hs](./size.hs)

```hs
*Main> size [1,2,3,4]
4
```

**Γινόμενο τιμών λίστας**


**Συνδυασμός λιστών με το zip**

```hs
Prelude> zip [1,2,3,4] [5,6,7,8]
[(1,5),(2,6),(3,7),(4,8)]
```

## Δημιουργία λιστών

```hs
Prelude> 1:[2,3]
[1,2,3]
```

**Συνάρτηση που επιστρέφει μια λίστα με τους άρτιους αριθμούς μιας λίστας**

```hs
allEven :: [Integer] -> [Integer]
allEven [] = []
allEven (h:t) = if even h then h:allEven t else allEven t
```
[all_even.hs](./all_even.hs)

```hs
*Main> allEven [1,2,3,4,5,6]
[2,4,6]
```

**Περιοχές τιμών (ranges)** 

```hs
Prelude> [1..10]
[1,2,3,4,5,6,7,8,10]
Prelude> [0,5..10]
[0,5,10]
Prelude> [2, 1.5, 0]
[2.0,1.5,1.0,0.5,0.0]
```

**Μη φραγμένες περιοχές τιμών** 

```hs
Prelude> take 5 [1..]
[1,2,3,4,5]
```

**List Comprehensions**

```hs
Prelude> [x * 2 | x <- [1, 2, 3]]
[2,4,6]
Prelude> [ (y, x) | (x, y) <- [(1, 2), (2, 3), (3, 1)]]
[(2,1),(3,2),(1,3)]
Prelude> [ (y, x) | (x, y) <- [(1, 2), (2, 3), (3, 1)]]
[(2,1),(3,2),(1,3)]
Prelude> let a = [1..10]
Prelude> let b = [0,5,20]
Prelude> [(x,y) | x <- a, y<-b]
[(1,0),(1,5),(1,20),(2,0),(2,5),(2,20),(3,0),(3,5),(3,20),(4,0),(4,5),(4,20),(5,0),(5,5),(5,20),(6,0),(6,5),(6,20),(7,0),(7,5),(7,20),(8,0),(8,5),(8,20),(9,0),(9,5),(9,20),(10,0),(10,5),(10,20)]
Prelude> [(x,y) | x <- a, y<-b, x < y]
[(1,5),(1,20),(2,5),(2,20),(3,5),(3,20),(4,5),(4,20),(5,20),(6,20),(7,20),(8,20),(9,20),(10,20)]
```


## Videos

* [Graham Hutton - Functional Programming](https://www.youtube.com/channel/UCBDp7ydYTHi1dh4Gnf3VTPA)
* [Philipp Hagenlocher - Haskell for Imperative Programmers](https://www.youtube.com/watch?v=Vgu82wiiZ90&list=PLe7Ei6viL6jGp1Rfu0dil1JH1SHk9bgDV)

<!-- ## Examples -->

<!-- ### Starman

* [starman.hs](./starman.hs)

    $ ghci
    GHCi, version 8.10.3: https://www.haskell.org/ghc/  :? for help
    Prelude> :load starman.hs
    Prelude> starman "functionally" 5 -->
