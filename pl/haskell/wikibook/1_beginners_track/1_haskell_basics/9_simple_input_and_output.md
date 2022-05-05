# Απλή είσοδος και έξοδος

## Επιστροφή στην πραγματικότητα

Πέρα από τον υπολογισμό τιμών, επιθυμούμε τα προγράμματά μας να αλληλεπιδρούν με τον κόσμο. Για παράδειγμα το πρόγραμμα εμφάνισης του μηνύματος Hello World! στην οθόνη του υπολογιστή γράφεται στη Haskell ως εξής.

```
Prelude> putStrLn "Hello, World!
```

Η συνάρτηση putStrLn είναι διαφορετική από τις συναρτήσεις που έχουμε δει μέχρι τώρα, καθώς δεν επιστρέφει κάτι που μπορεί να χρησιμοποιηθεί από άλλη συνάρτηση, αλλά αλλάζει τα περιεχόμενα της οθόνης, δηλαδή πραγματοποιεί μια ενέργεια εκτός του "κόσμου του προγράμματος".

Ο τύπος της putStrLn είναι:

```
Prelude> :type putStrLn
putStrLn :: String -> IO ()
```

Ο τύπος της συνάρτησης putStrLn σημαίνει ότι δέχεται ένα λεκτικό και προκαλεί μια ενέργεια που επιστρέφει την κενή λίστα.

## Ακολουθίες εντολών με το do

Ο συμβολισμός do είναι ένας βολικός τρόπος τοποθέτησης πολλών ενεργειών μαζί.

Για παράδειγμα ο ακόλουθος κώδικας δέχεται ως είσοδο ένα όνομα και το εμφανίζει

```
main = do
  putStrLn "Please enter your name:"
  name <- getLine
  putStrLn ("Hello, " ++ name ++ ", how are you?")
```

[enter_your_name.hs](./enter_your_name.hs)

Ο τύπος της συνάρτησης getline δείχνει ότι πρόκειται για μια ενέργεια IO που επιστρέφει ένα String.

```
Prelude> :t getLine
getLine :: IO String
```

**Διευκρινήσεις για τη χρήση του <-**

1. Αν και ενέργειες όπως η getLine χρησιμοποιούνται σχεδόν πάντα για τη λήψη τιμών, αυτό δεν είναι απαραίτητο.

```
main = do
  putStrLn "Please enter your name:"
  getLine
  putStrLn "Hello, how are you?"
```

[left_arrow_clarrification.hs](./left_arrow_clarrification.hs)

2. Το <- μπορεί να χρησιμοποιηθεί για οποιαδήποτε ενέργεια εκτός από την τελευταία.

**Έλεγχος ενεργειών**

Εντολές της Haskell όπως η if/then/else μπορούν να χρησιμοποιηθούν με το συμβολισμό do, αλλά υπάρχουν ορισμένα σημεία που πρέπει να προσέχουμε. Για παράδειγμα έστω το επόμενο απλό πρόγραμμα "μάντεψε τον αριθμό":

```
doGuessing num = do
   putStrLn "Enter your guess:"
   guess <- getLine
   if (read guess) < num
     then do putStrLn "Too low!"
             doGuessing num
     else if (read guess) > num
            then do putStrLn "Too high!"
                    doGuessing num
            else putStrLn "You Win!"
```

[guessTheNumber.hs](./guessTheNumber.hs)

Η if/then/else δέχεται τρία ορίσματα, τη συνθήκη, τον κλάδο "then" και τον κλάδο "else". Η συνθήκη πρέπει να έχει τύπο Bool, και οι δύο κλάδοι οποιοδήποτε τύπο αρκεί να είναι ο ίδιος και για τους δύο. Στους κλάδους που οι κλήσεις συναρτήσεων είναι περισσότερες από μια πρέπει να τοποθετήσουμε το do. Αλλιώς, ανα για παράδειγμα στο πρώτο ή στο δεύτερο then δεν τοποθετήσουμε do τότε η συνάρτηση putStrLn θα κλήθεί με 3 ορίσματα (π.χ. το λεκτικό "Too low!", τη συνάρτηση doGuessing και τον ακέραιο num).

**Προσοχή στους τύπους των ενεργειών**

Γιατί ο ακόλουθος κώδικας επιστρέφει σφάλμα;

```
main =
 do putStrLn "What is your name? "
    putStrLn ("Hello " ++ getLine)
```

Η πηγή του σφάλματος είναι η ίδια και στον ακόλουθο απλούστερο κώδικα.

```
main =
 do putStrLn getLine
```

Οι τύποι των συναρτήσεων putStrLn και getLine είναι.

```
 putStrLn :: String -> IO ()
 getLine  :: IO String
```

Άρα η getLine δεν επιστρέφει String αλλά επιστρέφει IO String. Για να λάβει το String που χρειάζεται η putStrLn ως όρισμα χρειάζεται να εκτελεστεί η ενέργεια και αυτό γίνεται με το αριστερό βελάκι <-. 

```
main =
 do name <- getLine
    putStrLn name
```

και 

```
main =
 do putStrLn "What is your name? "
    name <- getLine
    putStrLn ("Hello " ++ name)
```

**Προσοχή και στους τύπους των εκφράσεων**

Έστω ο ακόλουθος κώδικας που εμφανίζει το όνομα που δίνει ο χρήστης, αλλά πλέον σε κεφαλαία.

```
import Data.Char (toUpper)

main =
 do name <- getLine
    loudName <- makeLoud name
    putStrLn ("Hello " ++ loudName ++ "!")
    putStrLn ("Oh boy! Am I excited to meet you, " ++ loudName)

-- Don't worry too much about this function; it just converts a String to uppercase
makeLoud :: String -> String
makeLoud s = map toUpper s
```

Όμως εμφανίζει το ακόλουθο σφάλμα.

```
Couldn't match expected type `IO' against inferred type `[]'
      Expected type: IO t
      Inferred type: String
    In a 'do' expression: loudName <- makeLoud name
```

Όπως και στο προηγούμενο παράδειγμα δημιουργείται πρόβλημα διότι δεν ταιριάζει ο τύπος IO με τον τύπο String. Μια λύση μπορεί να δωθεί με χρήση ενός let binding.

```
main =
 do name <- getLine
    let loudName = makeLoud name
    putStrLn ("Hello " ++ loudName ++ "!")
    putStrLn ("Oh boy! Am I excited to meet you, " ++ loudName)
```

Παρατηρήστε ότι το let binding μέσα στην do δεν χρειάζεται τη λέξη κλειδί in.
