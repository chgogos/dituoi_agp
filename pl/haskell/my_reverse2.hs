myReverse :: [Integer] -> [Integer]
myReverse [] = []
myReverse xs = last xs : myReverse (init xs)