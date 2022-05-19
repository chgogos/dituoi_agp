import Data.List (genericLength)

-- page 15
average ns = sum ns `div` length ns

average2 ns = realToFrac (sum ns) / genericLength ns

-- page 20

a = b + c
  where
    b = 1
    c = 2

d = a * 2
