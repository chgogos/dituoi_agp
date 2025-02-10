import System.IO

main :: IO ()
main = do
  putStr "Enter min : "
  hFlush stdout
  input1 <- getLine
  putStr "Enter max : "
  hFlush stdout
  input2 <- getLine
  putStr "Enter value : "
  hFlush stdout
  input3 <- getLine
  let min = read input1 :: Int
  let max = read input2 :: Int
  let x = read input3 :: Int
  if inRange min max x
    then putStrLn "YES"
    else putStrLn "NO"
  if inRange1 min max x
    then putStrLn "YES"
    else putStrLn "NO"
  if inRange2 min max x
    then putStrLn "YES"
    else putStrLn "NO"
  if inRange3 min max x
    then putStrLn "YES"
    else putStrLn "NO"

inRange :: (Ord a) => a -> a -> a -> Bool
inRange min max x = min <= x && x <= max

inRange1 :: (Ord p) => p -> p -> p -> Bool
inRange1 min max x =
  let iub = x <= max
      ilb = x >= min
   in ilb && iub

inRange2 :: (Ord p) => p -> p -> p -> Bool
inRange2 min max x = ilb && iub
  where
    ilb = x >= min
    iub = x <= max

inRange3 :: (Ord a) => a -> a -> a -> Bool
inRange3 min max x
  | x < min = False
  | x > max = False
  | otherwise = True