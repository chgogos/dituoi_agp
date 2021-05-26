fact :: Integer -> Integer
fact 0 = 1
fact x = x * fact (x - 1)