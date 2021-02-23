import unittest


def find_odd(values):
    """
    δέχεται μία λίστα με ακέραιες τιμές και επιστρέφει την τιμή που υπάρχει
    περιττό αριθμό φορών (θεωρείστε ότι υπάρχει τέτοια τιμή και ότι είναι μόνο μία)
    """
    a_dict = {}
    for x in values:
        if x in a_dict:
            a_dict[x] += 1
        else:
            a_dict[x] = 1
    for k in a_dict:
        if a_dict[k] % 2 == 1:
            return k
    return None


class TestFunctions(unittest.TestCase):

    def test_find_odd(self):
        self.assertEqual(find_odd([1]), 1)
        self.assertEqual(find_odd([1, 1, 2, 2, 3, 4, 4]), 3)
        self.assertEqual(find_odd([7, 7, 1, 2, 1, 7, 4, 4, 2, 2, 2]), 7)


if __name__ == "__main__":
    unittest.main()
