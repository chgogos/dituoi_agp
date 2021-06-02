qsort :: Ord a => [a] -> [a]
qsort [] = []
qsort (h:t) =
   qsort [b | b <- t, b <= h]
   ++ [h] ++
   qsort [b | b <- t, b > h]
