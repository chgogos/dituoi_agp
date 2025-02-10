sumInt :: [Int] -> Int
sumInt [] = 0
sumInt (x:xs) = x + sumInt xs