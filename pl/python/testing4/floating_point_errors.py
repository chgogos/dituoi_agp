import unittest


class FloatingPoints(unittest.TestCase):
    def test_fp(self):
        # self.assertEqual(1.4 - 1.0, 0.4) # AssertionError: 0.3999999999999999 != 0.4
        self.assertAlmostEqual(1.4 - 1.0, 0.4, delta=0.001)

        # self.assertEqual(0.1 + 0.2, 0.3) # AssertionError: 0.30000000000000004 != 0.3
        self.assertAlmostEqual(0.1 + 0.2, 0.3, delta=0.001)


unittest.main()
