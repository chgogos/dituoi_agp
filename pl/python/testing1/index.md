# Παράδειγμα unit tests 1

Συγγραφή συνάρτησης που δέχεται μία λίστα με ακέραιες τιμές και επιστρέφει την τιμή που υπάρχει περιττό αριθμό φορών (θεωρείστε ότι υπάρχει τέτοια τιμή και ότι είναι μόνο μία).

[set1.py](./set1.py)

```
$ python -u "e:\git_repos\dituoi_agp\pl\python\testing1\set1.py"
F
======================================================================
FAIL: test_find_odd (__main__.TestFunctions)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "e:\git_repos\dituoi_agp\pl\python\testing1\set1.py", line 15, in test_find_odd
    self.assertEqual(find_odd([1]), 1)
AssertionError: None != 1

----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (failures=1)
```

[set1sol.py](./set1sol.py)

```
python -u "e:\git_repos\dituoi_agp\pl\python\testing1\set1sol.py"
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```