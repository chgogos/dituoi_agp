# Θεωρήστε ως λέξεις τις συμβολοσειρές που περιέχουν μόνο χαρακτήρες του αγγλικού αλφαβήτου.

import re
import unittest

with open("metamorphosis.txt", "r") as f:
    text = f.read().replace("\n", " ")

text = text.lower()

# Πλήθος των λέξεων του κειμένου
def q1():
    pattern = re.compile(r"\b([a-z]*)\W")
    matches = pattern.finditer(text)
    all_matches = set()
    for match in matches:
        m = match.group(1)
        all_matches.add(m)
    # print(all_matches)
    return len(all_matches)


# Πλήθος των λέξεων του κειμένου που ξεκινούν με τον χαρακτήρα 'c' και τελειώνουν με τον χαρακτήρα 'e'
def q2():
    pattern = re.compile(
        r"\b(c[a-z]*e)\W"
    )  # λέξεις που ξεκινούν με c και τελειώνουν με e
    matches = pattern.finditer(text)
    all_matches = set()
    for match in matches:
        m = match.group(1)
        all_matches.add(m)
    # print(all_matches)
    return len(all_matches)


# Πλήθος των λέξεων του κειμένου με 5 χαρακτήρες
def q3():
    pattern = re.compile(r"\b([a-z]{5})\W")
    matches = pattern.finditer(text)
    all_matches = set()
    for match in matches:
        m = match.group(1)
        all_matches.add(m)
    # print(all_matches)
    return len(all_matches)


# Πλήθος λέξεων του κειμένου που περιέχουν συνεχόμενους τους χαρακτήρες 't', 'a', 'c'
def q4():
    pattern = re.compile(r"\b([a-z]*tac[a-zA-Z]*)\W")
    matches = pattern.finditer(text)
    all_matches = set()
    for match in matches:
        m = match.group(1)
        all_matches.add(m)
    # print(all_matches)
    return len(all_matches)


# πλήθος λέξεων του κειμένου που περιέχουν συνεχόμενους τους χαρακτήρες 't', 'a', 'c' σε οποιαδήποτε σειρά
def q5():
    pattern = re.compile(r"\b([a-z]*(tac|tca|atc|act|cat|cta)[a-zA-Z]*)\W")
    matches = pattern.finditer(text)
    all_matches = set()
    for match in matches:
        m = match.group(1)
        all_matches.add(m)
    # print(all_matches)
    return len(all_matches)


# πλήθος λέξεων του κειμένου που ξεκινούν και τελειώνουν με τον ίδιο χαρακτήρα
def q6():
    pattern = re.compile(r"\b([a-z])([a-z]*\1)\W")
    matches = pattern.finditer(text)
    all_matches = set()
    for match in matches:
        m = match.group(1) + match.group(2)
        all_matches.add(m)
    # print(all_matches)
    return len(all_matches)


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
