import Data.Char (toUpper)

main =
  do
    name <- getLine
    let loudName = makeLoud name
    putStrLn ("Hello " ++ loudName ++ "!")
    putStrLn ("Oh boy! Am I excited to meet you, " ++ loudName)

-- Don't worry too much about this function; it just converts a String to uppercase
makeLoud :: String -> String
makeLoud s = map toUpper s