-- main :: IO ()
-- main = putStrLn (foo [1, 7, 8])

foo :: [Int] -> Int 
foo [] = 7
foo (x:xs) = if x `mod` 5 == 0 then foo xs else x + foo xs

main :: IO ()
main = print (foo [1, 7, 8])