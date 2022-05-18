# Δηλώσεις τύπων

Η Haskell επιτρέπει τον ορισμό τύπων από τον προγραμματιστή πέρα από τους προκαθορισμένους τύπους της γλώσσας.

Υποστηρίζει τη δήλωση νέων τύπων με 3 τρόπους.

* Τη δήλωση δεδομένων (```data```)  που ορίζουν νέους τύπους δεδομένων.
* Τη δήλωση τύπων (```type```) για συνώνυμα τύπων, δηλαδή εναλλακτικά ονόματα για υπάρχοντες τύπους.
* Τη δήλωση ```newtype``` για νέους τύπους δεδομένων ισοδύναμους με ήδη υπάρχοντες.

Στη συνέχεια θα δούμε τη δήλωση ```data``` και τη δήλωση ```type```.

## ```data``` και συναρτήσεις κατασκευής

Η λέξη κλειδί ```data``` χρησιμοποιείται για να ορίσει νέους τύπους δεδομένων χρησιμοποιώντας υπάρχοντες τύπους ως δομικά στοιχεία.

```
data Anniversary = Birthday String Int Int Int       -- name, year, month, day
                 | Wedding String String Int Int Int -- spouse name 1, spouse name 2, year, month, day
```

Η παραπάνω δήλωση αφορά έναν νέο τύπο δεδομένων με όνομα ```Anniversary``` που μπορεί να είναι είτε ```Birthday``` είτε ```Wedding```. Ένα ```Birthday``` περιέχει ένα λεκτικό και τρεις ακεραίους και ένα ```Wedding``` περιέχει δύο λεκτικά και τρεις ακεραίους. Η δήλωση των δύο πιθανών τύπων για τον τύπο δεδομένων ```Anniversary``` γίνεται με τη χρήση του συμβόλου \|. Η δήλωση ορίζει και δύο συναρτήσεις κατασκευαστές με ονόματα ```Birthday``` και ```Wedding``` αντίστοιχα.

Οι τύποι που ορίζονται με δηλώσεις δεδομένων (```data```) συχνά αναφέρονται ως ***algebraic data types***.

Τα ονόματα των τύπων πρέπει να ξεκινούν με κεφαλαίο τον πρώτο χαρακτήρα.

Αν ρωτήσουμε τον τύπο για παράδειγμα του ```Birthday``` θα λάβουμε το ακόλουθο αποτέλεσμα:

```
*Main> :t Birthday
Birthday :: String -> Int -> Int -> Int -> Anniversary
```

που σημαίνει ότι πρόκειται για μια συνάρτηση που λαμβάνει ένα λεκτικό και τρεις ακεραίους και αποτιμάται σε ```Anniversary```.

Η κλήση των κατασκευαστών δεν διαφέρει από την κλήση άλλων συναρτήσεων. Για παράδειγμα

```
johnSmith :: Anniversary
johnSmith = Birthday "John Smith" 1968 7 3
```

```
smithWedding :: Anniversary
smithWedding = Wedding "John Smith" "Jane Smith" 1987 3 4
```

Τα δύο παραπάνω μπορούν να τοποθετηθούν σε μια λίστα.

```
anniversariesOfJohnSmith :: [Anniversary]
anniversariesOfJohnSmith = [johnSmith, smithWedding]
```

ή και να δημιουργηθούν απευθείας μέσα στη λίστα.

```
anniversariesOfJohnSmith = [Birthday "John Smith" 1968 7 3, Wedding "John Smith" "Jane Smith" 1987 3 4]
```

## Αποδόμηση τύπων

Για να χρησιμοποιηθούν οι νέοι τύποι δεδομένων θα πρέπει να έχουμε πρόσβαση στα περιεχόμενά τους. Για παράδειγμα, δείτε τη συνάρτηση ```showAnniversary```.

```
showDate :: Int -> Int -> Int -> String
showDate y m d = show y ++ "-" ++ show m ++ "-" ++ show d

showAnniversary :: Anniversary -> String
showAnniversary (Birthday name year month day) =
  name ++ " born " ++ showDate year month day
showAnniversary (Wedding name1 name2 year month day) =
  name1 ++ " married " ++ name2 ++ " on " ++ showDate year month day
```

Στη συνάρτηση ```showAnniversary``` οι μεταβλητές προσδένονται στις τιμές που δίνονται. Η έκφραση μέσα στις παρενθέσεις αν και μοιάζουν με κλήσεις των κατασκευαστών, στην πραγματικότητα δεν είναι, αλλά είναι η απαιτούμενη σύνταξη για να επιτευχθεί η πρόσδεση των μεταβλητών.

```
*Main> showAnniversary (Birthday "Nikos" 1 10 1999)
"Nikos born 1-10-1999"
```

## Η χρήση του ```type``` για τη δημιουργία συνωνύμων

Προκειμένου να ενισχυθεί η σαφήνεια του κώδικα των προηγούμενων παραδειγμάτων θα μπορούσε να διευκρινίζεται ότι τα λεκτικά στον τύπο ```Anniversary``` έχουν ρόλο ονομάτων. Αυτό μπορεί να επιτευχθεί με την ακόλουθη δήλωση:

```
type Name = String
```

Πλέον το ```Name``` είναι συνώνυμο του ```String```. Οποιαδήποτε συνάρτηση δέχεται ένα ```String``` θα μπορεί να δέχεται και ένα ```Name```.

Η χρήση συνωνύμων type επιτρέπουν την ανάθεση ψευδωνύμων σε σύνθετους τύπους λιστών και πλειάδων.

Ακολουθεί ένα παράδειγμα αναμόρφωσης του προηγούμενου κώδικα έτσι ώστε να χρησιμοποιεί συνώνυμα.

```
type Name = String

data Anniversary = 
   Birthday Name Date
   | Wedding Name Name Date

data Date = Date Int Int Int   -- Year, Month, Day

johnSmith :: Anniversary
johnSmith = Birthday "John Smith" (Date 1968 7 3)

smithWedding :: Anniversary
smithWedding = Wedding "John Smith" "Jane Smith" (Date 1987 3 4)

type AnniversaryBook = [Anniversary]

anniversariesOfJohnSmith :: AnniversaryBook
anniversariesOfJohnSmith = [johnSmith, smithWedding]

showDate :: Date -> String
showDate (Date y m d) = show y ++ "-" ++ show m ++ "-" ++ show d 

showAnniversary :: Anniversary -> String
showAnniversary (Birthday name date) =
   name ++ " born " ++ showDate date
showAnniversary (Wedding name1 name2 date) =
   name1 ++ " married " ++ name2 ++ " on " ++ showDate date
```
