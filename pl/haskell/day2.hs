-- εφαρμογή συνάρτησης σε όλα τα στοιχεία μιας λίστας
squareAll list = map square list
    where square x = x * x

-------------------------------------------------

-- δημιουργία μιας άπειρης λίστας
myRange start step = start:(myRange (start + step) step)
