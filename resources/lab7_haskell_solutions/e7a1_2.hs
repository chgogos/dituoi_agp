pow :: (Eq t, Num t, Num p) => p -> t -> p
pow x 0 = 1
pow x y = x * pow x (y -1)