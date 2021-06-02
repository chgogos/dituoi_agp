-- τύπος ορισμένος από το χρήστη με δύο τιμές
data Boolean = True | False deriving (Show)

-------------------------------------------------

-- τύποι και συναρτήσεις για παιχνίδια με κάρτες
data Suit = Spades | Hearts deriving (Show)

data Rank = Ten | Jack | Queen | King | Ace deriving (Show)

type Card = (Rank, Suit)

type Hand = [Card]

value :: Rank -> Integer
value Ten = 1
value Jack = 2
value Queen = 3
value King = 4
value Ace = 5

cardValue :: Card -> Integer
cardValue (rank, suit) = value rank

-------------------------------------------------

-- πολυμορφική συνάρτηση
backwards :: [a] -> [a]
backwards [] = []
backwards (h : t) = backwards t ++ [h]

-------------------------------------------------

-- πολυμορφικός τύπος δεδομένων
data Triplet a = Trio a a a deriving (Show)

-------------------------------------------------

-- Αναδρομικός τύπος δεδομένων
data Tree a = Children [Tree a] | Leaf a deriving (Show)

depth :: (Num p, Ord p) => Tree a -> p
depth (Leaf _) = 1
depth (Children c) = 1 + maximum (map depth c)
