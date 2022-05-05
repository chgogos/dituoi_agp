revWords :: String -> String
revWords input = (unwords . reverse . words) input