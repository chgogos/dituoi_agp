-- foo :: [Int] -> Int 
-- foo [] = 7
-- foo (x:xs) = if x `mod` 5 == 0 then foo xs else x + foo xs

bar :: [Int] -> Int 
bar [] = 7
bar (x:xs) 
    | x `mod` 5 == 0 = bar xs 
    | otherwise = x + bar xs

foo :: Int -> a -> [a]
foo 0 x = []
foo n x = x: foo (n-1) x
