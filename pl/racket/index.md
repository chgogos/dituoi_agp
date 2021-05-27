# Racket

## Αριθμητικές συναρτήσεις

```
> (+ 3 4)
7
> (- 10 5 4)
1
> (* 3 7 2) 
42
> (/ 10 2)
5
> (sqrt 2)
1.4142135623730951
> (max 3 4 5 1)
5
> (modulo 10 3)
1
```

## Ορισμός συναρτήσεων

Μια έκφραση λάμδα.

```
> (lambda (x) (* x x))
#<procedure>
```

Χρήση της λάμδα έκφρασης κατ' αναλογία με τις επώνυμες συναρτήσεις.

```
> ((lambda (x) (* x x)) 7)
49
```

Η συνάρτηση define 
* Συνδέει ένα όνομα με μια τιμή (δημιουργώντας μια επώνυμη τιμή και όχι μια μεταβλητή)
* Συνδέει ένα όνομα με μια έκφραση λάμδα

Δημιουργία επώνυμης τιμής

```
> (define pi 3.14)
> pi
3.14
```

Σύνδεση ονόματος με έκφραση λάμδα

```
> (define (square x) (* x x))
> (square 2)
4
```

Συνάρτηση υπολογισμού της υποτείνουσας ενός ορθογωνίου τριγώνου.

```
> (define (hypotenuse side1 side2)
    (sqrt (+ (square side1) (square side2)))
)
> (hypotenuse 3 5)
5.830951894845301
```

## Συναρτήσεις κατηγορημάτων

```
> (= 1 2)
#f
> (>= 1 2)
#t
> (even? 2)
#t
> (even? 1)
#f
> (not #t)
#f
```

## Ροή ελέγχου

Παράδειγμα if-else

```
(define (factorial n)
  (if (= n 1)
      1
      (* n (factorial (- n 1)))))
```

Παράδειγμα πολλαπλής επιλογής

```
(define (leap? year)
    (cond
    ((zero? (modulo year 400)) #t)
    ((zero? (modulo year 100)) #f)
    (else (zero? (modulo year 4)))
))
```

## Συναρτήσεις λιστών

**quote**

```
> (quote a)
`a
> (quote (a b c))
'(a b c)
```

ή

```
> 'a
'a
> '(a b c))
'(a b c)
```

**car cdr cons**

```
> (car '(a b c))
'a
> (cdr '(a b c))
'(b c)
> (cons 'a '(b c))
'(a b c)
```

**caar cadr cadar κλπ**

για τη συνάρτηση cadr ισχύει ότι:

```
(cadr x) είναι ισοδύναμο με (car(cdr x))
```

παρόμοια και για τις άλλες σχετικές συναρτήσεις

```
> (cadr '(a b c d))
'b
> (caar '((a b) c d))
'a
> (cadar '((a b c) d e f))
'b
```

**cons**

```
> (cons 'a '(b c))
'(a b c)
```

**list**

```
> (list 'a 'b 'c)
'(a b c)
```

## Παραδείγματα επεξεργασίας λιστών

**Παράδειγμα 1**

Επίλυση προβλήματος ιδιότητας μέλους ενός δεδομένου ατόμου σε μια δεδομένη λίστα που δεν περιλαμβάνει υπολίστες (απλή λίστα).

```
(define (my_member atm a_list)
    (cond
        ((null? a_list) #f)
        ((eq? atm (car a_list)) #t)
        (else (my_member atm (cdr a_list)))
))
```

```
> (my_member 'a '(a b c))
#true
```

**Παράδειγμα 2**

Διαπίστωση του εάν δύο δεδομένες απλές λίστες είναι ίσες.

```
(define (equalsimp list1 list2)
    (cond
        ((null? list1) (null? list2))
        ((null? list2) #f)
        ((eq? (car list1) (car list2))
            (equalsimp (cdr list1) (cdr list2)))
        (else #f)
    )
)
```

```
> (equalsimp '(a b) '(a b))
#true
```

**Παράδειγμα 3**

Κατασκευή μιας νέας λίστας που περιέχει όλα τα στοιχεία δύο δεδομένων ορισμάτων λιστών.

```
(define (my_append list1 list2)
    (cond 
        ((null? list1) list2)
        (else (cons (car list1) (my_append (cdr list1) list2)))
    )
)
```

```
> (my_append '(a b) '(c d e))
(list 'a 'b 'c 'd 'e)
```