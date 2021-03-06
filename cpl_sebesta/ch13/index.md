# 13. Ταυτοχρονισμός

* Συγχρονισμός ανταγωνισμού και συγχρονισμός συνεργασίας
* Αμοιβαία αποκλειόμενη πρόσβαση
  * Σημαφόροι (semaphores)
  * Παρακολουθητές (monitors)
  * Μεταβίβαση μηνυμάτων
* Παράδειγμα παραγωγού και καταναλωτή
* liveness
<!-- * actor tasks vs server tasks -->

## 13.1 Εισαγωγή

### 13.1.1 Αρχιτεκτονικές πολλαπλών επεξεργαστών

* SIMD
  * Διανυσματικοί επεξεργαστές (vector processors)
* MIMD
* Κρυφός ταυτοχρονισμός
  * Διοχέτευση εντολών και δεδομένων από τη μνήμη στον επεξεργαστή
  * Ξεχωριστές γραμμές μνήμης για εντολές και δεδομένα
  * Εκ των προτέρων λήψη (prefetching) εντολών και δεδομένων
  * Παράλληλη εκτέλεση αριθμητικών πράξεων

## 13.2 Εισαγωγή στον ταυτοχρονισμό σε επίπεδο υποπρογράμματος

### 13.2.1 Θεμελιώδεις έννοιες

* Συνθήκη ανταγωνισμού (race condition)

### 13.2.2 Σχεδιασμός γλωσσών για ταυτοχρονισμό

#### Ταυτοχρονισμός μέσω βιβλιοθηκών (OpenMP)

#### Java

#### Python

#### C#

## 13.3 Σημαφόροι

* E. Dijkstra (1965)
* Ένας σημαφόρος είναι μια δομή δεδομένων που αποτελείται από έναν ακέραιο και μια ουρά στην οποία αποθηκεύονται περιγραφείς εργασιών
* Οι δύο λειτουργίες που παρέχουν οι σημαφόροι είναι οι wait και release

## 13.4 Παρακολουθητές

## 13.5 Μεταβίβαση μηνυμάτων

## 13.6 Υποστήριξη ταυτοχρονισμού στην Ada

* Ο ταυτοχρονισμός στη Java επιτυγχάνεται μέσω εργασιών που η καθεμία εκτελείται στο δικό της χώρο διευθύνσεων.

## 13.7 Νήματα στη Java

* Τα νήματα στη Java είναι ελαφρές εργασίες (lightweight processes), δηλαδή εκτελούνται στον ίδιο χώρο διευθύνσεων
* Όλες οι εφαρμογές Java εκτελούνται σε νήματα
* Προτεραιότητες: NORM_PRIORITY=5, MIN_PRIORITY=1, MAX_PRIORITY=10