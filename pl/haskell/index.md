# Haskell

H Haskell είναι μια αμιγής συναρτησιακή γλώσσα προγραμματισμού οκνηρής αποτίμησης. Η Haskell διαθέτει ισχυρό στατικό σύστημα τύπων (strong static typing) που αντιλαμβάνεται τους τύπους που απαιτούνται για τις συναρτήσεις και τις παραμέτρους τους.

Τα παραδείγματα κώδικα που ακολουθούν είναι από το "[7 Languages in 7 Weeks, by Bruce A. Tate - A Pragmatic Guide to Learning Programming Languages](https://pragprog.com/titles/btlang/seven-languages-in-seven-weeks/)" και από άλλες πηγές.

Ενεργοποίηση και τερματισμός του διερμηνευτή ghci της Haskell.

```
ghci
GHCi, version 8.0.2: http://www.haskell.org/ghc/  :? for help
Prelude> "Hello World!"
"Hello World!"
Prelude> :quit
```

## Εκφράσεις και βασικοί τύποι

**Αριθμοί**

```hs
> 1 + 2
3
> (+) 1 2
3
> 1 + 2 * 3
7
> 1 + 2 * 3.0
7.0
> 2 ^ 10
1024
> div 10 3
3
> mod 10 3
1
> gcd 24 56
8 
```

**Λεκτικά**

```hs
> "hi"
"hi"
> "hello " ++ "world"
"hello world"
-- δεικτοδότηση λεκτικού με το !!
> "hello" !! 1
'e'
```

**Χαρακτήρες**

Ένα λεκτικό είναι μια λίστα χαρακτήρων.

```hs
> 'a'
'a'
> ['a', 'b']
"ab"
```

**Boolean**

```hs
> 1 == 2-1
True
> 1 /= 1
False
```

## Συναρτήσεις

Οι συναρτήσεις στην Haskell αποτελούνται από δύο τμήματα. Ένα προαιρετικό τμήμα δήλωσης του τύπου της συνάρτησης. Ένα τμήμα με την υλοποίηση της συνάρτησης. Η Haskell έχει ένα ισχυρό σύστημα συμπερασμού για τον εντοπισμό των τύπων που χρησιμοποιούνται στις συναρτήσεις.

Πρόσδεση της μεταβλητής x σε τοπική εμβέλεια.

```hs
> let x = 42
> x
42
```

Πρόσδεση της συνάρτησης double σε τοπική εμβέλεια.

```hs
> let double x = 2 * x
> double 21
42
```

Αποθήκευση συνάρτησης σε αρχείο.

```hs
double :: Integer -> Integer
double x = 2 * x
```
[day1.hs](./day1.hs)

Φόρτωση κώδικα, κλήση συνάρτησης.

```
$ ghci
GHCi, version 8.0.2: http://www.haskell.org/ghc/  :? for help
Prelude> :load day1.hs
*Main> double 10
20
*Main> :quit
```

ή 

```
$ ghci day1.hs
GHCi, version 8.0.2: http://www.haskell.org/ghc/  :? for help
*Main> double 10
20
*Main> :quit
```


## Αναδρομή

```hs
> let fact x = if x == 0 then 1 else fact (x - 1) * x
> fact 3
6
```

**Αντιστοίχιση μοτίβων (pattern matching)**

```hs
factpm :: Integer -> Integer
factpm 0 = 1
factpm x = x * factpm (x - 1)
```
[day1.hs](./day1.hs))

```hs
> factpm 5
120
```

**Φρουροί (guards)**

Οι φρουροί είναι συνθήκες που περιορίζουν τις τιμές των ορισμάτων όπως στη συνέχεια. Όταν η συνθήκη ενός φρουρού ικανοποιείται η Haskell καλεί την κατάλληλη συνάρτηση.

```hs
factg :: Integer -> Integer
factg x
    | x > 1 = x * factg (x-1)
    | otherwise 1
```
[day1.hs](./day1.hs)

```hs
> factg 5
120
```

## Πλειάδες και λίστες

Στις πλειάδες τα στοιχεία μπορούν να είναι διαφορετικού τύπου ενώ στις λίστες όλα τα στοιχεία είναι του ίδιου τύπου. 

Μια λίστα και μια πλειάδα.

```hs
>:type [1,2,3]
[1,2,3] :: Num a => [a]
>:type ('1',2,3)
('1',2,3) :: (Num a, Num b) => (Char,b,a)
```

**Πρώτο (fst) και δεύτερο (snd) στοιχείο σε πλειάδα**

```hs
> fst (1,2)
1
> snd (1,2)
2
```

Συνάρτηση εύρεσης όρων της ακολουθίας fibonacci.

```hs
fib :: Integer -> Integer
fib 0 = 1
fib 1 = 1
fib x = fib (x - 1) + fib (x - 2)
```
[day1.hs](./day1.hs)

```hs
> fib 10
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
[day1.hs](./day1.hs)

```hs
> fib 100
354224848179261915075
```

**head, tail, init, last σε λίστες**

```hs
> head [1,2,3,4]
1
> tail [1,2,3,4]
[2,3,4]
> let (h:t) = [1,2,3,4]
> h
1
Prelude> t
[2,3,4]
> init [1,2,3,4]
[1,2,3]
> last [1,2,3,4]
4
```

**Σύνθεση (composition)**

```hs
> let second = head . tail
> second [1,2,3]
second = 2
```

## Διάσχιση λιστών

**Μέγεθος λίστας**

```hs
size [] = 0
size (h:t) = 1 + size t
```
[day1.hs](./day1.hs)

```hs
> size [1,2,3,4]
4
```

**Γινόμενο τιμών λίστας**

```hs
> product [1,2,3,4]
24
```
[day1.hs](./day1.hs)

**Συνδυασμός λιστών με το zip**

```hs
> zip [1,2,3,4] [5,6,7,8]
[(1,5),(2,6),(3,7),(4,8)]
```

**Συνδυασμός λιστών με συνάρτηση με το zipWith**

```hs
> zipWith (*) [1,2,3,4] [5,6,7,8]
[5,12,21,32]
```


## Δημιουργία λιστών

```hs
> 1:[2,3]
[1,2,3]
```

**Συνάρτηση που επιστρέφει μια λίστα με τους άρτιους αριθμούς μιας λίστας**

```hs
allEven :: [Integer] -> [Integer]
allEven [] = []
allEven (h:t) = if even h then h:allEven t else allEven t
```
[day1.hs](./day1.hs)

```hs
> allEven [1,2,3,4,5,6]
[2,4,6]
```

**Περιοχές τιμών (ranges)** 

```hs
> [1..10]
[1,2,3,4,5,6,7,8,10]
> [0,5..10]
[0,5,10]
> [2, 1.5, 0]
[2.0,1.5,1.0,0.5,0.0]
```

**Μη φραγμένες περιοχές τιμών** 

```hs
> take 5 [1..]
[1,2,3,4,5]
```

**List Comprehensions**

```hs
> [x * 2 | x <- [1, 2, 3]]
[2,4,6]
> [ (y, x) | (x, y) <- [(1, 2), (2, 3), (3, 1)]]
[(2,1),(3,2),(1,3)]
> [ (y, x) | (x, y) <- [(1, 2), (2, 3), (3, 1)]]
[(2,1),(3,2),(1,3)]
> let a = [1..10]
> let b = [0,5,20]
> [(x,y) | x <- a, y<-b]
[(1,0),(1,5),(1,20),(2,0),(2,5),(2,20),(3,0),(3,5),(3,20),(4,0),(4,5),(4,20),(5,0),(5,5),(5,20),(6,0),(6,5),(6,20),(7,0),(7,5),(7,20),(8,0),(8,5),(8,20),(9,0),(9,5),(9,20),(10,0),(10,5),(10,20)]
> [(x,y) | x <- a, y<-b, x < y]
[(1,5),(1,20),(2,5),(2,20),(3,5),(3,20),(4,5),(4,20),(5,20),(6,20),(7,20),(8,20),(9,20),(10,20)]
```


## Συναρτήσεις υψηλότερης τάξης

**Ανώνυμες συναρτήσεις**

Η σύνταξη των ανώνυμων συναρτήσεων στη Haskell είναι η ακόλουθη.

```
(\param1 .. paramn -> function_body)
```

Μια ανώνυμη συνάρτηση επιστροφής του τετραγώνου της παραμέτρου της και η κλήση της με παράμετρο την τιμή 5.

```hs
> (\ x -> x * x) 5
25
```

Μια ανώνυμη συνάρτηση με δύο παραμέτρους.

```hs
> (\ x y-> x * y) 5 7
35
```

**map**

```hs
> map (\x -> x * x) [1, 2, 3]
[1, 4, 9]
```

```hs
squareAll list = map square list
    where square x = x *x
```

```hs
> squareAll [1, 2, 3]
[1,4,9]
```

H (+1) είναι μια μερικά εφαρμοσμένη συνάρτηση. Πρόκειται για τη συνάρτηση + στην οποία έχει προσδεθεί η μια από τις δύο παραμέτρους με τιμή 1. Η δεύτερη παράμετρος σε κάθε κλήση της συνάρτησης θα είναι μια τιμή της λίστας.

```hs
> map (+1) [1,2,3]
[2,3,4]
```

**filter**

```hs
> filter odd [1, 2, 3, 4, 5]
[1, 3, 5]
```

**foldl**

```hs
> foldl (\x sum -> sum + x) 0 [1, 2, 3, 4]
10
```

```hs
> foldl (+) 0 [1,2,3,4]
10
```

```hs
> foldl1 (+) [1,2,3,4]
10
```

## Μερικά εφαρμοσμένες συναρτήσεις και currying

Στη Haskell κάθε συνάρτηση ουσιαστικά έχει μια μόνο παράμετρο.

```hs
> let prod x y = x * y
> prod 3 4
12
> (prod 3) 4
12
> tripple = prod 3
> tripple 4
12
```
[day2.hs](./day2.hs)

## Οκνηρή αποτίμηση

H Haskell επιτρέπει άπειρες λίστες να επιστρέφονται από συναρτήσεις.

Ορισμός μιας άπειρης λίστας.

```hs
myRange start step = start:(myRange (start + step) step)
```
[day2.hs](./day2.hs)

```hs
> take 5 (myRange 10 2)
[10,12,14,16,18]
```

Σύνταξη της Haskell για μη φραγμένες περιοχές τιμών.

```hs
> take 10 [1..]
[1,2,3,4,5,6,7,8,9,10]
> take 10 [1,3..]
[1,3,5,7,9,11,13,15,17,19]
```

## Τύποι

**Πρωτογενείς τύποι**

```hs
> :type 'a'
'a' :: Char
> :type True
True :: Bool
```

**Τύποι ορισμένοι από το χρήστη**

```hs
data Suit = Spades | Hearts deriving (Show)
data Rank = Ten | Jack | Queen | King | Ace deriving (Show)
type Card = (Rank, Suit)
type Hand = [Card]
```
[day3.hs](./day3.hs)

**Αναδρομικοί τύποι**

```hs
data Tree a = Children [Tree a] | Leaf a deriving (Show)
```
[day3.hs](./day3.hs)

```hs
> let tree = Children[Leaf 1, Children [Leaf 2, Leaf 3]]
> tree
Children[Leaf 1, Children [Leaf 2, Leaf 3]]
```

**Κλάσεις**

Στην Haskell μια κλάση ορίζει ένα πρωτόκολλο λειτουργιών (σύνολο από συναρτήσεις) που πρέπει να υποστηρίζει ένας τύπος έτσι ώστε ο τύπος να θεωρείται στιγμιότυπο της κλάσης.


## Μεταγλώττιση και εκτέλεση κώδικα

```hs
fac :: (Eq p, Num p) => p -> p
fac 0 = 1
fac n = n * fac (n-1)

main :: IO ()
main = print (fac 42)
```
[example1.hs](./example1.hs)

```
$ ghc example1.hs
[1 of 1] Compiling Main             ( example1.hs, example1.o )
Linking example1.exe ...
$ example1.exe
1405006117752879898543142606244511569936384000000000
```

## Βιβλία - σημειώσεις

* [Λογικός και συναρτησιακός προγραμματισμός - Σταματόπουλος Παναγιώτης](https://repository.kallipos.gr/handle/11419/3587)


## Videos

* [Graham Hutton - Functional Programming](https://www.youtube.com/channel/UCBDp7ydYTHi1dh4Gnf3VTPA)
* [Philipp Hagenlocher - Haskell for Imperative Programmers](https://www.youtube.com/watch?v=Vgu82wiiZ90&list=PLe7Ei6viL6jGp1Rfu0dil1JH1SHk9bgDV)
* [Curtis D'Alves - Learning Haskell](https://www.youtube.com/playlist?list=PLHRF-X-NtQR4MZBvm05NshPIEI8ELID5m)

## Πηγές

* [Learning Haskell](https://wiki.haskell.org/Learning_Haskell)
* [Learn X in Y minutes](https://learnxinyminutes.com/docs/haskell/)


<!-- ## Examples -->

<!-- ### Starman

* [starman.hs](./starman.hs)

    $ ghci
    GHCi, version 8.10.3: https://www.haskell.org/ghc/  :? for help
    Prelude> :load starman.hs
    Prelude> starman "functionally" 5 -->
