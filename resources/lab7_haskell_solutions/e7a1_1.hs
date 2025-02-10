doubleFactorial :: (Eq p, Num p) => p -> p
doubleFactorial 0 = 1
doubleFactorial 1 = 1
doubleFactorial n = n * doubleFactorial (n - 2)