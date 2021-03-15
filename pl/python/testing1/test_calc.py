import unittest
import calc


class TestCalc(unittest.TestCase):

    # η μέθοδος είναι υποχρεωτικό να ξεκινά με test έτσι ώστε να εκτελείται ως test
    def test_add(self):
        result = calc.add(10, 5)
        self.assertEqual(result, 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)
        self.assertEqual(calc.divide(5, 2), 2.5)
        self.assertRaises(
            ValueError, calc.divide, 10, 0
        )  # προσοχή στον τρόπο με τον οποίο περνούν οι παράμετροι

    # με χρήση context manager
    def test_divide2(self):
        with self.assertRaises(ValueError):
            calc.divide(10,0)


if __name__ == "__main__":
    unittest.main()
