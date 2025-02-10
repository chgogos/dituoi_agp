log2 :: (Num p, Integral t) => t -> p
log2 1 = 0
log2 x = 1 + log2 (x `div` 2)