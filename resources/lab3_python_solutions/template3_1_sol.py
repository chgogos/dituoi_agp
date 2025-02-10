import unittest
import random


def e_approx(n):
    total = 0
    for _ in range(n):
        s = 0
        c = 0
        while s < 1:
            s += random.random()
            c += 1
        total += c
    return total / n


# Mην αλλάξετε κάτι από εδώ και κάτω
class Test(unittest.TestCase):
    def test_e_approximation(self):
        self.assertAlmostEqual(e_approx(1_000_000), 2.7182818, delta=0.001)


if __name__ == "__main__":
    unittest.main()
