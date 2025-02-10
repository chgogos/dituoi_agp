# Θεωρήστε ως λέξεις τις συμβολοσειρές που περιέχουν μόνο χαρακτήρες του αγγλικού αλφαβήτου.

import re
import unittest

with open("metamorphosis.txt", encoding="utf-8") as f:
    a_list = f.readlines()

text = "".join(a_list[45:52])
text = text.lower()
print(text)

# Πλήθος των λέξεων του κειμένου
def q1():
    results = re.findall(r"\b[a-z]+\b", text)
    results = set(results)
    # print(results)
    return len(results)

def q1_alt1(): # 1ος εναλλακτικός τρόπος επίλυσης του ερωτήματος 1
    pattern = re.compile(r"\b[a-z]+\b")
    results = pattern.findall(text)
    results = set(results)
    # print(results)
    return len(results)

def q1_alt2(): # 2ος εναλλακτικός τρόπος επίλυσης του ερωτήματος 1
    pattern = re.compile(r"\b[a-z]+\b")
    results = set()
    for x in pattern.finditer(text):
        results.add(x.group(0))
    # print(results)
    return len(results)

# Πλήθος των λέξεων που ξεκινούν με τον χαρακτήρα 'h' και τελειώνουν με τον χαρακτήρα 'e'
def q2():
    results = re.findall(r"\bh[a-z]*e\b", text)
    results = set(results)
    # print(results)
    return len(results)


# Πλήθος των λέξεων του κειμένου με 5 χαρακτήρες
def q3():
    results = re.findall(r"\b[a-z]{5}\b", text)
    results = set(results)
    # print(results)
    return len(results)


# Πλήθος λέξεων του κειμένου που περιέχουν συνεχόμενους τους χαρακτήρες 'a', 's'
def q4():
    results = re.findall(r"\b[a-z]*as[a-z]*\b", text)
    results = set(results)
    # print(results)
    return len(results)


# πλήθος λέξεων του κειμένου που περιέχουν συνεχόμενους τους χαρακτήρες 'a', 's' σε οποιαδήποτε σειρά
def q5():
    results = re.findall(r"\b[a-z]*as|sa[a-z]*\b", text)
    results = set(results)
    # print(results)
    return len(results)


# πλήθος λέξεων του κειμένου που ξεκινούν και τελειώνουν με τον ίδιο χαρακτήρα
def q6():
    results = re.findall(r"\b([a-z])([a-z]*\1)\b", text)
    results = [x[0] + x[1] for x in results]
    results = set(results)
    # print(results)
    return len(results)


# πλήθος λέξεων του κειμένου που ξεκινούν και τελειώνουν με τους 2 ίδιους χαρακτήρες
def q7():
    results = re.findall(r"\b([a-z]{2})([a-z]*\1)\b", text)
    results = [x[0] + x[1] for x in results]
    results = set(results)
    # print(results)
    return len(results)


# Mην αλλάξετε κάτι από εδώ και κάτω
class TestReExamples(unittest.TestCase):
    def test_q1(self):
        self.assertEqual(q1(), 70)
        self.assertEqual(q1_alt1(), 70)
        self.assertEqual(q1_alt2(), 70)

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
