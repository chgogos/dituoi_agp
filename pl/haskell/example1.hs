fac :: (Eq p, Num p) => p -> p
fac 0 = 1
fac n = n * fac (n-1)

main :: IO ()
main = print (fac 42)