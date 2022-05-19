# Τα πρώτα βήματα

## Ασκήσεις

**Άσκηση 2**
```
n = a `div` length xs
  where
    a = 10
    xs = [1, 2, 3, 4, 5]
```

**Άσκηση 3 & 4**
```
myLast1 xs = head (reverse xs)

myLast2 xs = head (drop (length xs - 1) xs)
```

**Άσκηση 5**
```
myInit1 xs = reverse (tail (reverse xs))

myInit2 xs = take (length xs - 1) xs
```