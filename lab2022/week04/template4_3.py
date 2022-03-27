import unittest

class Stack:
    def __init__(self):
        self.data = []

    def push(self, item):
        pass

    def pop(self):
        pass

    def clear(self):
        pass

    def __str__(self):
        pass

# Mην αλλάξετε κάτι από εδώ και κάτω
class TestHammingDistance(unittest.TestCase):
    def test_Stack(self):
        s = Stack()
        self.assertTrue(str(s)=="Η στοίβα δεν περιέχει στοιχεία")
        s.push(1)
        self.assertTrue(str(s)=="->1\n")
        s.push(2)
        self.assertTrue(str(s)=="->2\n  1\n")
        s.push(3)
        self.assertTrue(str(s)=="->3\n  2\n  1\n")
        s.pop()
        self.assertTrue(str(s)=="->2\n  1\n")

if __name__ == "__main__":
    unittest.main()