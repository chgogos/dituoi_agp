# Θεωρήστε ως λέξεις τις συμβολοσειρές που περιέχουν μόνο χαρακτήρες του αγγλικού αλφαβήτου και ότι οι λέξεις χωρίζονται μεταξύ τους με κενά.

import re
import unittest

with open("metamorphosis.txt", "r") as f:
    text = f.read().replace("\n", " ")

text = text.lower()

# Πλήθος των λέξεων του κειμένου
def q1():
    pass


# Πλήθος των λέξεων του κειμένου που ξεκινούν με τον χαρακτήρα 'c' και τελειώνουν με τον χαρακτήρα 'e'
def q2():
    pass


# Πλήθος των λέξεων του κειμένου με 5 χαρακτήρες
def q3():
    pass


# Πλήθος λέξεων του κειμένου που περιέχουν συνεχόμενους τους χαρακτήρες 't', 'a', 'c'
def q4():
    pass


# πλήθος λέξεων του κειμένου που περιέχουν συνεχόμενους τους χαρακτήρες 't', 'a', 'c' σε οποιαδήποτε σειρά
def q5():
    pass


# πλήθος λέξεων του κειμένου που ξεκινούν και τελειώνουν με τον ίδιο χαρακτήρα
def q6():
    pass


# Mην αλλάξετε κάτι από εδώ και κάτω
class TestReExamples(unittest.TestCase):
    def test_regexes(self):
        self.assertEqual(q1(), 2581)
        self.assertEqual(q2(), 35)
        self.assertEqual(q3(), 397)
        self.assertEqual(q4(), 3)
        self.assertEqual(q5(), 34)
        self.assertEqual(q6(), 136)


if __name__ == "__main__":
    unittest.main()
