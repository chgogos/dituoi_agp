dropInt :: Int -> [a] -> [a]
dropInt 0 x = x
dropInt _ [] = []
dropInt n (x:xs) = dropInt (n-1) xs