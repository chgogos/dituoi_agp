# Prolog

## Παρουσιάσεις

* [<mark>Εισαγωγή στη γλώσσα Prolog - Παπασπύρου Ν., Σαγώνας Κ.</mark>](https://ocw.aoc.ntua.gr/modules/document/file.php/ECE117/lecture-16.pdf)
* [Περισσότερη Prolog - Παπασπύρου Ν., Σαγώνας Κ.](https://ocw.aoc.ntua.gr/modules/document/file.php/ECE117/lecture-17.pdf)

[<mark>Κώδικας παρουσιάσεων</mark>](./mpl_webber/index.md)

## Συγγράμματα

* [Τεχνικές Λογικού Προγραμματισμού - Η γλώσσα Prolog - Η. Σακελλαρίου, Ν. Βασιλειάδης, Π. Κεφαλάς, Δ. Σταμάτης, 2015](https://repository.kallipos.gr/handle/11419/777)
  * Κεφάλαιο 4. Σύνταξη Prolog Προγραμμάτων
  * Κεφάλαιο 5. Σημασιολογία Prolog Προγραμμάτων
* [Λογικός Προγραμματισμός - Η γλώσσα Prolog - Χ. Νομικός, 2015](http://www.cs.uoi.gr/~cnomikos/courses/pl/Prolog-2015.pdf)
* [Η γλώσσα προγραμματισμού Prolog - μέθοδος ταχείας εκμάθησης βάσει παραδειγμάτων - Κ. Σγάρμπας , 2006](https://www.dit.uoi.gr/e-class/modules/document/file.php/196/prolog_shmeiwseis_sgarbas.pdf)
* [The First 10 Prolog Programming Contests](https://dtai.cs.kuleuven.be/ppcbook/)


## Tutorials

* [<mark>Learn X in Y minutes where X=prolog</mark>](https://learnxinyminutes.com/docs/prolog/)
* [The power of Prolog by Markus Triska](https://www.metalevel.at/prolog)
* [Prolog tutorial by J.R.Fisher](https://www.cpp.edu/~jrfisher/www/prolog_tutorial/pt_framer.html)
* [Learn Prolog Now](http://www.learnprolognow.org/)
  * [Chapter 1 kb1.pl](./lpn/ch1/kb1.pl)
  * [Chapter 1 kb2.pl](./lpn/ch1/kb2.pl)
  * [Chapter 1 kb3.pl](./lpn/ch1/kb3.pl)
  * [Chapter 1 kb4.pl](./lpn/ch1/kb4.pl)
  * [Chapter 1 kb5.pl](./lpn/ch1/kb5.pl)
  * [Chapter 2 kb1.pl](./lpn/ch2/kb1.pl)
  * [Chapter 2 kb2.pl](./lpn/ch2/kb2.pl)
  * [Chapter 2 kb3.pl](./lpn/ch2/kb3.pl)
  * [Chapter 2 kb4.pl](./lpn/ch2/kb4.pl)
  * [Chapter 3 eating.pl](./lpn/ch3/eating.pl)
  * [Chapter 3 descend.pl](./lpn/ch3/descend.pl)
  * [Chapter 3 descend1.pl](./lpn/ch3/descend1.pl)
  * [Chapter 3 descend2.pl](./lpn/ch3/descend2.pl)
  * [Chapter 3 descend3.pl](./lpn/ch3/descend3.pl)
  * [Chapter 3 descend4.pl](./lpn/ch3/descend4.pl)
  * [Chapter 3 successor.pl](./lpn/ch3/successor.pl)
  * [Chapter 3 add.pl](./lpn/ch3/add.pl)
  * [Chapter 3 matryoshka.pl](./lpn/ch3/matryoshka.pl)
  * [Chapter 4 member.pl](./lpn/ch4/member.pl)
  * [Chapter 4 a2b.pl](./lpn/ch4/a2b.pl)
  * [Chapter 5 addThreeAndDouble.pl](./lpn/ch5/addThreeAndDouble.pl)
  * [Chapter 5 len1.pl](./lpn/ch5/len1.pl)
  * [Chapter 5 accLen.pl](./lpn/ch5/acclen.pl)
  * [Chapter 5 accMax.pl](./lpn/ch5/accMax.pl)
  * [Chapter 10 kb1.pl](./lpn/ch10/kb1.pl)
  * [Chapter 10 kb2.pl](./lpn/ch10/kb2.pl)
  * [Chapter 10 kb3.pl](./lpn/ch10/kb3.pl)
  * [Chapter 10 kb4.pl](./lpn/ch10/kb4.pl)
  * [Chapter 10 kb5.pl](./lpn/ch10/kb5.pl)

## Βίντεο μαθήματα για την Prolog

* [Εργαστήριο Prolog, Κ. Σγάρμπας](https://eclass.upatras.gr/modules/video/?course=EE690)
* [Εισαγωγή στην Prolog, Δ. Ψούνης)](https://www.youtube.com/playlist?list=PLLMmbOLFy25HGbFmMa6aWLBkFcI5FVabr)
* [The Power of Prolog by Markus Triska: Videos](https://www.metalevel.at/prolog/videos/)

## Λογισμικά

* [<mark>SWI-Prolog</mark>](http://www.swi-prolog.org/)
  * [swish - online εκτέλεση εντολών και προγραμμάτων Prolog](https://swish.swi-prolog.org/)
  * [SWI-Prolog editor (μόνο για windows)](http://arbeitsplattform.bildung.hessen.de/fach/informatik/swiprolog/indexe.html)
  * [pyswip (Python - SWI-Prolog bridge)](https://github.com/yuce/pyswip)
* [GNU-Prolog](http://www.gprolog.org/)


## Διάφορα

**Εμφάνιση αποτελεσμάτων**

```
?-  X = 1,  Y = 2,  Z is  X + Y, W = arta, format('X=~w Y=~w Z=~w W=~s', [X,Y,Z,W]), fail.  % στη SWI-Prolog
X=1 Y=2 Z=3 W=arta
false.
```

**Έξοδος από κατάσταση λάθους**

Ctrl + C και μετά a για abort

**Εγκατάσταση της GNU-Prolog σε Ubuntu**

```
$ sudo apt-get update
$ sudo apt-get upgrade
$ sudo apt-get gprolog
$ gprolog
GNU Prolog 1.4.5 (64 bits)
Compiled Feb  5 2017, 10:30:08 with gcc
By Daniel Diaz
Copyright (C) 1999-2016 Daniel Diaz
| ?- print('hello world').
hello world

yes
| ?- halt.
```

**Ενεργοποίηση και απενεργοποίηση ιχνηλάτησης**

```
trace.
[trace] ?- 
...
nodebug.
?-
```
