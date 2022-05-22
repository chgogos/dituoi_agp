main :: IO()
main = do
   content <- readFile "input_for_haskell.txt"
   let linesOfFiles = lines content
       x = map words linesOfFiles
   print x
