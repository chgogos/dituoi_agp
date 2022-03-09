import unittest


# αρχή κώδικα που ελέγχεται
def fac(x):
    """Υπολογισμός παραγοντικού, αν το όρισμα είναι αρνητικός επιστρέφει -1"""
    if x < 0:
        return -1
    if x == 0 or x == 1:
        return 1
    return x * fac(x - 1)


# τέλος κώδικα που ελέγχεται


class TestFaculty(unittest.TestCase):
    def test_known_values(self):
        self.assertEqual(fac(1), 1)
        self.assertEqual(fac(2), 2)
        self.assertEqual(fac(3), 6)
        self.assertEqual(fac(4), 24)
        self.assertEqual(fac(5), 120)

    def test_corner_cases(self):
        self.assertEqual(fac(0), 1)
        self.assertEqual(fac(-1), -1)
        self.assertEqual(fac(-2), -1)
        self.assertEqual(fac(-3), -1)
        self.assertEqual(fac(-100), -1)


unittest.main()
