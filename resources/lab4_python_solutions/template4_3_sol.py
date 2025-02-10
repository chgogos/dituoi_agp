import unittest


class Stack:
    EMPTY_MSG = "Η στοίβα δεν περιέχει στοιχεία"

    def __init__(self):
        self.data = []

    def push(self, item):
        self.data.append(item)

    def pop(self):
        if len(self.data) > 0:
            self.data.pop()
        else:
            print(Stack.EMPTY_MSG)

    def clear(self):
        self.data = []

    def __str__(self):
        if len(self.data) == 0:
            return Stack.EMPTY_MSG
        else:
            s = ""
            for idx, item in enumerate(reversed(self.data)):
                if idx == 0:
                    s += f"->{item}\n"
                else:
                    s += f"  {item}\n"
            return s


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