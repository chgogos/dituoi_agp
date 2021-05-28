fact :: Integer -> Integer
fact x
    | x > 1 = x * fact (x-1)
    | otherwise = 1