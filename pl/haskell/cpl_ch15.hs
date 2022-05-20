-- παραγοντικό (υλοποίηση 1)
fact1 :: (Eq p, Num p) => p -> p
fact1 0 = 1
fact1 1 = 1
fact1 n = n * fact1 (n - 1)

-- παραγοντικό (υλοποίηση 2)
fact2 :: (Num p, Ord p) => p -> p
fact2 n
  | n == 0 = 1
  | n == 1 = 1
  | n > 0 = n * fact2 (n -1)
  | otherwise = error "only non negative integers are allowed"

-- παραγοντικό (υλοποίηση 3)
prod :: Num p => [p] -> p
prod [] = 1
prod (a : x) = a * prod x

fact3 :: (Num p, Enum p) => p -> p
fact3 n = prod [1 .. n]

-- παραγοντικό (υλοποίηση 4)
fact4 :: (Num a, Enum a) => a -> a
fact4 n = product [1 .. n]

-------------------------------------------------
-- Αριθμοί fibonacci 1,1,2,3,5,8,13,21,...

fib :: (Eq a, Num a, Num p) => a -> p
fib 0 = 1
fib 1 = 1
fib n = fib (n -1) + fib (n -2)

-------------------------------------------------

-- παράγοντες ενός ακεραίου n
factors :: Int -> [Int]
factors n = [i | i <- [1 .. n `div` 2], n `mod` i == 0]

-- εναλλακτική υλοποίηση
factors2 :: Int -> [Int]
factors2 n = [i | i <- [1 .. x], n `mod` i == 0]
  where
    x = n `div` 2

-------------------------------------------------

-- ταξινόμηση λίστας με την quicksort
qsort :: Ord a => [a] -> [a]
qsort [] = []
qsort (h : t) =
  qsort [b | b <- t, b <= h]
    ++ [h]
    ++ qsort [b | b <- t, b > h]

-------------------------------------------------

-- συνάρτηση για έλεγχο μέλους (σε άπειρη λίστα δημιουργείται πρόβλημα αν το στοιχείο δεν υπάρχει στη λίστα)
member :: Eq t => t -> [t] -> Bool
member b [] = False
member b (a : x) = (a == b) || member b x

-- > member 16 [n*n | n <- [0..]]
-- True
-- > member 17 [n*n | n <- [0..]]
-- δεν επιστρέφει...

-- -- συνάρτηση για έλεγχο μέλους (λειτουργεί σωστά και με άπειρες λίστες)
member2 :: Ord a => a -> [a] -> Bool
member2 b (a : x)
  | a < b = member2 b x
  | a == b = True
  | otherwise = False

-- > member2 16 [n*n | n <- [0..]]
-- True
-- > member2 17 [n*n | n <- [0..]]
-- False

sub n
  | n < 10 = 0
  | n > 100 = 2
  | otherwise = 1