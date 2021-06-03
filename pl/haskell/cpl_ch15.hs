-- γινόμενο λίστας ακεραίων
prod :: [Int] -> Int
prod [] = 1
prod (a:x) = a * prod x

-- παραγοντικό ακεραίου με χρήση της συνάρτησης γινομένου λίστας
fact :: Int -> Int
fact n = prod [1..n]

-------------------------------------------------

-- παράγοντες ενός ακεραίου n
factors :: Int -> [Int]
factors n = [i | i <- [1..n `div` 2], n `mod` i == 0]

-- εναλλακτική υλοποίηση
factors2 :: Int -> [Int]
factors2 n = [i | i <- [1..x], n `mod` i == 0]
   where x = n `div` 2

-------------------------------------------------

-- ταξινόμηση λίστας με την quicksort
qsort :: Ord a => [a] -> [a]
qsort [] = []
qsort (h:t) =
   qsort [b | b <- t, b <= h]
   ++ [h] ++
   qsort [b | b <- t, b > h]

-------------------------------------------------

-- συνάρτηση για έλεγχο μέλους (σε άπειρη λίστα δημιουργείται πρόβλημα αν το στοιχείο δεν υπάρχει στη λίστα)
member :: Eq t => t -> [t] -> Bool
member b [] = False
member b (a:x) = (a == b) || member b x

-- > member 16 [n*n | n <- [0..]]
-- True
-- > member 17 [n*n | n <- [0..]]
-- δεν επιστρέφει...

-- -- συνάρτηση για έλεγχο μέλους (λειτουργεί σωστά και με άπειρες λίστες)
member2 :: Ord a => a -> [a] -> Bool
member2 b (a:x)
   | a < b = member2 b x
   | a == b = True
   | otherwise = False

-- > member2 16 [n*n | n <- [0..]]
-- True
-- > member2 17 [n*n | n <- [0..]]
-- False
