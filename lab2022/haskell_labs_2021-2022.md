# Haskell labs

## Εργαστήριο 1
1) Εγκατάσταση Haskell
2) Ορισμός απλών συναρτήσεων, κλήση συναρτήσεων
3) Τύποι, :type
4) Λίστες, πλειάδες
5) Συγγραφή main προγράμματος σε Haskell

## Εργαστήριο 2
if/then/else
pattern matching
where
guards
σύνθεση συναρτήσεων
Είσοδος/έξοδος

## Εργαστήριο 3
1) ΑΝΑΔΡΟΜΗ (RECURSION)
2) ΛΑΜΔΑ ΣΥΝΑΡΤΗΣΕΙΣ ΚΑΙ Η ΣΥΝΑΡΤΗΣΗ map (higher order functions)   
3) ΑΠΕΙΡΕΣ ΛΙΣΤΕΣ (INFINITE LISTS)
4) ΜΕΡΙΚΗ ΑΠΟΤΙΜΗΣΗ ΣΥΝΑΡΤΗΣΕΩΝ (CURRYING)
5) ΠΕΡΙΦΡΑΣΤΙΚΕΣ ΛΙΣΤΕΣ (COMPREHENSIONS)

Εκτέλεση προγράμματος Haskell στον online compiler https://replit.com/languages/haskell

```
main = do
  let z = add 3 4
  let w = add' 4
  putStrLn (show z)
  putStrLn (show w)


add x y = x + y
add' = add 1
```

Παραδείγματα ονομάτων μεταβλητών

* scalar: x
* list: xs 
* list of lists: xss
