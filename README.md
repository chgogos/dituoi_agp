# ΑΡΧΕΣ ΓΛΩΣΣΩΝ ΠΡΟΓΡΑΜΜΑΤΙΣΜΟΥ

Πανεπιστήμιο Ιωαννίνων - Τμήμα Πληροφορικής και Τηλεπικοινωνιών

Γκόγκος Χρήστος - Άρτα@2022

e-course μαθήματος: <http://ecourse.uoi.gr/course/view.php?id=1945>

Τελευταία ενημέρωση: 23/02/2022

## 1. ΘΕΩΡΙΑ

<!-- ### Συγγράμματα (Εύδοξος) -->

<!-- * [Αρχές Γλωσσών Προγραμματισμού 11η εκδ., Robert W. Sebesta](https://www.mgiurdas.gr/biblia/arhes-glosson-programmatismoy-11i-ekdosi)
* [Σύγχρονες Γλώσσες Προγραμματισμού, Brooks Webber Adam](https://www.cup.gr/book/sigchrones-glosses-programmatismou/)
* [Πραγματολογία των γλωσσών προγραμματισμού, Michael L. Scott](http://www.klidarithmos.gr/pragmatologia-twn-glwsswn-programmatismoy) -->

Σημειώσεις μελέτης και διαφάνειες για το [Αρχές Γλωσσών Προγραμματισμού 11η εκδ., Robert W. Sebesta](https://www.mgiurdas.gr/biblia/arhes-glosson-programmatismoy-11i-ekdosi)

* [Κεφ.1 Εισαγωγή](./cpl_sebesta/ch01/index.md)
  * [pl11ch1GR.pdf](./resources/pl11ch1GR.pdf)
* [Κεφ.3 Περιγραφή συντακτικού και σημασιολογίας](./cpl_sebesta/ch03/index.md)
  * [pl11ch3GR.pdf](./resources/pl11ch3GR.pdf)

<!-- * [Κεφ.4 Λεκτική και συντακτική ανάλυση](./cpl_sebesta/ch04/index.md)
* [Κεφ.5 Ονόματα, προσδέσεις και εμβέλειες](./cpl_sebesta/ch05/index.md)
* [Κεφ.9 Υποπρογράμματα](./cpl_sebesta/ch09/index.md)
* [Κεφ.15 Γλώσσες συναρτησιακού προγραμματισμού](./cpl_sebesta/ch15/index.md)
* [Κεφ.16 Γλώσσες λογικού προγραμματισμού](./cpl_sebesta/ch16/index.md) -->


## 2. ΕΡΓΑΣΤΗΡΙΟ

* [Python](./pl/python/index.md) 
* [Haskell](./pl/haskell/index.md) 
* [Prolog](./pl/prolog/index.md) 


### **Εβδομάδα 1 - πρώτο εργαστήριο Python**
  
* [Εγκατάσταση της Python](https://eclass.aueb.gr/modules/document/file.php/INF259/python_installation_windows.pdf)
* [Εκτέλεση κώδικα στο IDLE](https://sites.pitt.edu/~naraehan/python3/getting_started_win_first_try.html), εκτέλεση script της Python στη γραμμή εντολών
* [Μεταβλητές, τιμές και τύποι, τελεστές και εκφράσεις](https://nbviewer.org/github/chgogos/dituoi_agp/blob/main/pl/python/notebooks/01-intro.ipynb?flush_cache=true)
* Είσοδος από τον χρήστη, εμφάνιση στη γραμμή εντολών (παραδείγματα [1](./pl/python/input1.py), [2](./pl/python/passwd.py))
* Έλεγχος ροής ([επιλογή](https://nbviewer.org/github/chgogos/dituoi_agp/blob/main/pl/python/notebooks/04-conditionals.ipynb?flush_cache=true) και [επανάληψη](https://nbviewer.org/github/chgogos/dituoi_agp/blob/main/pl/python/notebooks/05-loops.ipynb?flush_cache=true))
* Αμυντικός προγραμματισμός (παραδείγματα [1](./pl/python/defensive1.py), [2](./pl/python/defensive2.py), [3](./pl/python/defensive3.py), [4](./pl/python/defensive4.py))
* [Δομές Δεδομένων (λίστα, πλειάδα, λεξικό, σύνολο)](https://nbviewer.org/github/chgogos/dituoi_agp/blob/main/pl/python/notebooks/03-lists-tuples-dictionaries-sets.ipynb?flush_cache=true)
* Τεμαχισμός λιστών και [συμβολοσειρών](https://nbviewer.org/github/chgogos/dituoi_agp/blob/main/pl/python/notebooks/02-strings.ipynb?flush_cache=true)
* [Εγκατάσταση VSCode, ms-python.python extension, εκτέλεση κώδικα Python από το VSCode](https://code.visualstudio.com/docs/python/python-tutorial)

**Άσκηση E1A1** - Γράψτε πρόγραμμα που να υπολογίζει τα 10 πρώτα ψηφία του αποτελέσματος της ακόλουθης πράξης:

<img src="https://render.githubusercontent.com/render/math?math=\sqrt{\frac{2^{101}}{\pi^{53}+11^7}}">

**Άσκηση E1A2** - Γράψτε πρόγραμμα που να εμφανίζει για τη συμβολοσειρά "How I need a drink alcoholic of course, after all those lectures involving quantum mechanics" το πλήθος των χαρακτήρων κάθε λέξης. Παρατήρηση: η μέθοδος split() σε μια συμβολοσειρά επιστρέφει μια λίστα με τις λέξεις της.

**Άσκηση E1A3** - Γράψτε πρόγραμμα που να υπολογίζει το άθροισμα 1 + 1/2 + 1/4 + 1/8 + ... όπου ο χρήστης θα δίνει το πλήθος των όρων του αθροίσματος. Διασφαλίστε με αμυντικό προγραμματισμό ότι η τιμή που δίνει ο χρήστης είναι μια μη αρνητική ακέραια τιμή, αλλιώς να ζητείται επανεισαγωγή της τιμής.

**Άσκηση E1A4** - Δώστε την εντολή import this στο IDLE και αντιγράψτε σε ένα λεκτικό το κείμενο που επιστρέφεται. Γράψτε πρόγραμμα που να εμφανίζει το πλήθος παρατηρήσεων των χαρακτήρων Α έως και Z, χωρίς διάκριση πεζών και κεφαλαίων, στο παραπάνω κείμενο.

---

### **Εβδομάδα 2 - δεύτερο εργαστήριο Python**

* Συναρτήσεις
* Εμβέλεια μεταβλητών
* Λάμδα συναρτήσεις
* Αρθρώματα
* Περιφραστικές λίστες (list comprehensions)
* Unit tests, η βιβλιοθήκη unittest

**Άσκηση E2A1** - Γράψτε μια συνάρτηση που να δέχεται δύο λεκτικά και να επιστρέφει την απόσταση Hamming (δηλαδή το πλήθος των αντίστοιχων χαρακτήρων που διαφέρουν στα δύο λεκτικά). Αν τα λεκτικά είναι διαφορετικού μήκους η συνάρτηση να επιστρέφει την τιμή -1. Τροποποιήστε το [template2_1.py](./lab2022/week02/template2_1.py) έτσι ώστε η λύση σας να επιτυγχάνει σε όλα τα unit tests.

**Άσκηση E2A2** - Γράψτε μια συνάρτηση που να ελέγχει αν μια φράση είναι παντόγραμμα, δηλαδή περιλαμβάνει και τα 24 γράμματα του Ελληνικού αλφαβήτου. Τροποποιήστε το [template2_2.py](./lab2022/week02/template2_2.py) έτσι ώστε η λύση σας να επιτυγχάνει σε όλα τα unit tests.

**Άσκηση E2A3**  -  Γράψτε μια συνάρτηση που να δέχεται ένα κείμενο, να αφαιρεί τα σύμβολα τελεία και κόμμα, να εντοπίζει το μεγαλύτερο μήκος λέξης που περιέχει και να επιστρέφει μια λίστα με όλες τις λέξεις του κειμένου με μήκος ίσο με το μεγαλύτερο μήκος. Τροποποιήστε το [template2_3.py](./lab2022/week02/template2_3.py) έτσι ώστε η λύση σας να επιτυγχάνει σε όλα τα unit tests.

**Άσκηση E2A4** - Για την ακόλουθη λίστα τιμών 56, 37, 771, 90, 16, 11 γράψτε comprehensions που να κάνουν τα ακόλουθα:
* Να δημιουργεί νέα λίστα με το πλήθος των ψηφίων κάθε τιμής.
* Να δημιουργεί νέα λίστα με τα ψηφία κάθε τιμής σε αντίστροφη σειρά.
* Να δημιουργεί νέα λίστα μόνο με τις τιμές που είναι μεγαλύτερες από το μέσο όρο των τιμών.
* Να δημιουργεί νέα λίστα με ζεύγη τιμών που το πρώτο στοιχείο κάθε ζεύγους να είναι η ίδια τιμή και δεύτερο στοιχείο μια λογική τιμή με τιμή True αν η τιμή είναι άρτια αλλιώς η τιμή False.

Τροποποιήστε το [template2_4.py](./lab2022/week02/template2_4.py) έτσι ώστε η λύση σας να επιτυγχάνει σε όλα τα unit tests.

---

