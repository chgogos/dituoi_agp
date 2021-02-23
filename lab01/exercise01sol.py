"""
Συμπληρώστε τη συνάρτηση find_odd έτσι ώστε να δέχεται μια λίστα με ακέραιες τιμές,
και να επιστρέφει την τιμή που υπάρχει περιττό αριθμό φορών (θεωρείστε ότι υπάρχει τέτοια τιμή και ότι έιναι μόνο μια)
"""

import unittest


def find_odd(values):
    pass


class TestFindOdd(unittest.TestCase):

    def test_samples(self):
        self.assertEqual(find_odd([1, 1]), 1)
        self.assertEqual(find_odd([1, 1, 2, 2, 3, 4, 4]), 3)
        self.assertEqual(find_odd([7, 7, 1, 2, 1, 7, 4, 4, 2, 2, 2]), 3)


if __name__ == "__main__":
    unittest.main()
