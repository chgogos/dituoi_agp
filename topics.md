# Διάφορα θέματα

## Συναρτήσεις πρώτης τάξης (first class functions)

Μια γλώσσα προγραμματισμού λέγεται ότι διαθέτει συναρτήσεις πρώτης τάξης αν συμπεριφέρεται στις συναρτήσεις ως "πολίτες πρώτης κατηγορίας". Σε μια γλώσσα προγραμματισμού μια οντότητα είναι "πολίτης πρώτης κατηγορίας" (first class citizen) όταν η γλώσσα υποστηρίζει για την οντότητα αυτή όλες τις λειτουργίες που είναι γενικά διαθέσιμες και στις άλλες οντότητες. Τυπικά παραδείγματα τέτοιων λειτουργιών είναι το πέρασμα ως όρισμα, η επιστροφή από μια συνάρτηση και η ανάθεση σε μια μεταβλητή.  


**Παραδείγματα κώδικα**

* Python
  * [first_class_function1.py](./pl/python/first_class_function1.py)
  * [first_class_function2.py](./pl/python/first_class_function2.py)
  * [first_class_function3.py](./pl/python/first_class_function3.py)
  * [first_class_function4.py](./pl/python/first_class_function4.py)
  * [first_class_function5.py](./pl/python/first_class_function5.py)
* Javascript
  * [first_class_function1.js](./pl/javascript/first_class_function1.js)
  * [first_class_function2.js](./pl/javascript/first_class_function2.js)
  * [first_class_function3.js](./pl/javascript/first_class_function3.js)
  * [first_class_function4.js](./pl/javascript/first_class_function4.js)
  * [first_class_function5.js](./pl/javascript/first_class_function5.js)

**Πηγές**

* [Corey Schafer]()

## Κλειστότητες (closures)

Κλειστότητα είναι μια εγγραφή που αποθηκεύει μια συνάρτηση μαζί με ένα περιβάλλον (μια αντιστοίχιση κάθε ελεύθερης μεταβλητής της συνάρτησης με την τιμή με την οποία το όνομα προσδέθηκε όταν δημιουργήθηκε η κλειστότητα. Μια κλειστότητα, σε αντίθεση με μια απλή συνάρτηση, επιτρέπει στη συνάρτηση να προσπελάσει τις μεταβλητές που έχουν προσδεθεί μέσω των αναφορών  της κλειστότητας σε αυτές, ακόμα και όταν η συνάρτηση καλείται εκτός της εμβέλειάς τους)

Μια κλειστότητα εσωκλείει τις ελεύθερες μεταβλητές από το περιβάλλον της.

**Παραδείγματα κώδικα**

* [closure1.py](./pl/python/closure1.py)
* [closure2.py](./pl/python/closure2.py)
* [closure3.py](./pl/python/closure3.py)
* [closure4.py](./pl/python/closure4.py)
  
**Πηγές**

* [Corey Schafer: Closures - How to Use Them and Why They Are Useful](https://www.youtube.com/watch?v=swU3c34d2NQ)


## Άλλα

* Λογισμός λάμδα (lambda calculus)
* Υπόθεση Church-Turing (Church-Turing hypothesis)
* Ανώνυμες συναρτήσεις  (anonymous functions) = Λάμδα συναρτήσεις (lambda functions)
* Συναρτήσεις υψηλότερης τάξης (higher order functions)
* Currying
* Memoization
* duck typing
* No Code movement
  * <https://www.forbes.com/sites/enriquedans/2020/08/09/could-the-no-code-movement-put-programmers-out-of-ajob/>
  * <https://www.zdnet.com/article/with-so-much-remote-work-the-time-is-ripe-for-low-code-and-no-code-software-development/>