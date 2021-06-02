qsort [] = []
qsort (h:t) =
   qsort [b | b <- t, b <= h]
   ++ [h] ++
   qsort [b | b <- t, b > h]
