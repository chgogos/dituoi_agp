myReplicate :: (Eq t, Num t) => t -> a -> [a]
myReplicate 0 _ = []
myReplicate n x = x : myReplicate (n-1) x