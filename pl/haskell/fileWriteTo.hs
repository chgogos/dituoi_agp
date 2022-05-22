main :: IO ()
main = do
  let a_list = ["Arta", "Informatics", "Telecommunications"]
  writeFile ("output_from_haskell.txt") (unlines a_list)
