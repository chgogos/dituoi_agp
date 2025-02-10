takeInt :: Int -> [a] -> [a]
takeInt _ [] = []
takeInt 0 _ = []
takeInt n (x:xs) = x : takeInt (n-1) xs