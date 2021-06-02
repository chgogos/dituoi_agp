-- εφαρμογή συνάρτησης σε όλα τα στοιχεία μιας λίστας
squareAll :: Num b => [b] -> [b]
squareAll list = map square list
  where
    square x = x * x

-------------------------------------------------

-- δημιουργία μιας άπειρης λίστας
myRange :: Num t => t -> t -> [t]
myRange start step = start : (myRange (start + step) step)
