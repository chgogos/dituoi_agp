import unittest


def e_approx(n):
    pass


# Mην αλλάξετε κάτι από εδώ και κάτω
class Test(unittest.TestCase):
    def test_e_approximation(self):
        self.assertAlmostEqual(e_approx(1_000_000), 2.7182818, delta=0.001)


if __name__ == "__main__":
    unittest.main()
