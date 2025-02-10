plusOne :: Num a => a -> a
plusOne x = x + 1

addition :: (Eq t1, Num t1, Num t2) => t2 -> t1 -> t2
addition x 0 = x
addition x y = plusOne (addition x (y-1))