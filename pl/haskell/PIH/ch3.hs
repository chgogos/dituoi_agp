-- page 11

-- λαμβάνει και τα δύο ορίσματα μαζί
add :: (Int, Int) -> Int
add (x, y) = x + y

zeroto :: Int -> [Int]
zeroto n = [0 .. n]

-- page 12

-- λαμβάνει ένα όρισμα τη φορά, είναι curried συνάρτηση
add' :: Int -> (Int -> Int)
add' x y = x + y

-- page 13
mult :: Int -> (Int -> (Int -> Int))
mult x y z = x * y * z
