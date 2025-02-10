valueAt :: (Eq t, Num t) => [p] -> t -> p
valueAt [] _ = error "Out of bounds error"
valueAt (x:_) 0 = x
valueAt (x:xs) n = valueAt xs (n-1)