# Θεωρήστε ως λέξεις τις συμβολοσειρές που περιέχουν μόνο χαρακτήρες του αγγλικού αλφαβήτου.

import re
import unittest

text = ""  # να αλλαχθεί

# Πλήθος των λέξεων του κειμένου
def q1():
    ...


# Πλήθος των λέξεων που ξεκινούν με τον χαρακτήρα 'h' και τελειώνουν με τον χαρακτήρα 'e'
def q2():
    ...


# Πλήθος των λέξεων του κειμένου με 5 χαρακτήρες
def q3():
    ...


# Πλήθος λέξεων του κειμένου που περιέχουν συνεχόμενους τους χαρακτήρες 'a', 's'
def q4():
    ...


# πλήθος λέξεων του κειμένου που περιέχουν συνεχόμενους τους χαρακτήρες 'a', 's' σε οποιαδήποτε σειρά
def q5():
    ...


# πλήθος λέξεων του κειμένου που ξεκινούν και τελειώνουν με τον ίδιο χαρακτήρα
def q6():
    ...


# πλήθος λέξεων του κειμένου που ξεκινούν και τελειώνουν με τους 2 ίδιους χαρακτήρες
def q7():
    ...


# Mην αλλάξετε κάτι από εδώ και κάτω
class TestReExamples(unittest.TestCase):
    def test_q1(self):
        self.assertEqual(q1(), 70)

    def test_q2(self):
        self.assertEqual(q2(), 2)

    def test_q3(self):
        self.assertEqual(q3(), 12)

    def test_q4(self):
        self.assertEqual(q4(), 2)

    def test_q5(self):
        self.assertEqual(q5(), 3)

    def test_q6(self):
        self.assertEqual(q6(), 3)

    def test_q7(self):
        self.assertEqual(q7(), 1)


if __name__ == "__main__":
    unittest.main()
