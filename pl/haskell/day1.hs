-- συνάρτηση με όνομα double που επιστρέφει την παράμετρό της διπλασιασμένη
double :: Num a => a -> a
double x = x + x

-------------------------------------------------

-- factorial (3 τρόποι)
-- με conditional
factc :: Integer -> Integer
factc x = if x == 0 then 1 else factc (x -1) * x

-- με guards
factg :: Integer -> Integer
factg x
  | x > 1 = x * factg (x -1)
  | otherwise = 1

-- με pattern matching
factpm :: Integer -> Integer
factpm 0 = 1
factpm x = x * factpm (x - 1)

-------------------------------------------------

-- ακολουθία fibonacci (3 τρόποι)
-- με pattern matching
fibpm :: Integer -> Integer
fibpm 0 = 1
fibpm 1 = 1
fibpm x = fibpm (x - 1) + fibpm (x - 2)

-- με tuples
fibTuple :: (Integer, Integer, Integer) -> (Integer, Integer, Integer)
fibTuple (x, y, 0) = (x, y, 0)
fibTuple (x, y, index) = fibTuple (y, x + y, index - 1)

fibResult :: (Integer, Integer, Integer) -> Integer
fibResult (x, y, z) = x

fibt :: Integer -> Integer
fibt x = fibResult (fibTuple (0, 1, x))

-- με σύνθεση συναρτήσεων
fibNextPair :: (Integer, Integer) -> (Integer, Integer)
fibNextPair (x, y) = (y, x + y)

fibNthPair :: Integer -> (Integer, Integer)
fibNthPair 1 = (1, 1)
fibNthPair n = fibNextPair (fibNthPair (n - 1))

fibc :: Integer -> Integer
fibc = fst . fibNthPair

-------------------------------------------------

-- μήκος λίστας
size :: Num p => [a] -> p
size [] = 0
size (h : t) = 1 + size t

-------------------------------------------------

-- γινόμενο στοιχείων λίστας
prod :: Num p => [p] -> p
prod [] = 1
prod (h : t) = h * prod t

-------------------------------------------------

-- διατήρηση μόνο των άρτιων τιμών μιας λίστας
allEven :: [Integer] -> [Integer]
allEven [] = []
allEven (h : t) = if even h then h : allEven t else allEven t