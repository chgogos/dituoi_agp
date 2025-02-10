scanSum :: [Int] -> [Int]
scanSum [] = []
scanSum [x] = [x]
scanSum (x:y:xs) = x:scanSum ((x+y): xs)