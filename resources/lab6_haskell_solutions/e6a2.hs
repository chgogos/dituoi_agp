import System.IO

main :: IO ()
main = do
  putStrLn "Enter resistor's color code : "
  hFlush stdout
  band1 <- getLine
  band2 <- getLine
  band3 <- getLine
  let c = ohms band1 band2 band3
  putStr ("Ohms = " ++ show c)

-- Συνάρτηση με pattern matching
colorValue :: (Num a) => String -> a
colorValue "black" = 0
colorValue "brown" = 1
colorValue "red" = 2
colorValue "orange" = 3
colorValue "yellow" = 4
colorValue "green" = 5
colorValue "blue" = 6
colorValue "violet" = 7
colorValue "grey" = 8
colorValue "white" = 9
colorValue _ = -1

ohms :: (Num a) => String -> String -> String -> a
ohms band1 band2 band3 = (10 * colorValue band1 + colorValue band2) * 10 ^ colorValue band3
