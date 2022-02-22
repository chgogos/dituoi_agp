import unittest


class TestComprehensions(unittest.TestCase):
    def test1(self):
        a_list = [56, 37, 771, 90, 16, 11]
        b_list = None # αλλάξτε αυτή την εντολή για να απαντήσετε το ερώτημα 1
        self.assertEqual(b_list, [2,2,3,2,2,2])         

    def test2(self):
        a_list = [56, 37, 771, 90, 16, 11]
        b_list = None # αλλάξτε αυτή την εντολή για να απαντήσετε το ερώτημα 2
        self.assertEqual(b_list, [65,73,177,9,61,11])         

    def test3(self):
        a_list = [56, 37, 771, 90, 16, 11]
        b_list = None # αλλάξτε αυτή την εντολή για να απαντήσετε το ερώτημα 3
        self.assertEqual(b_list, [771])         

    def test4(self):
        a_list = [56, 37, 771, 90, 16, 11]
        b_list = None # αλλάξτε αυτή την εντολή για να απαντήσετε το ερώτημα 4
        self.assertEqual(b_list, [(56,True), (37,False), (771,False), (90, True), (16, True), (11, False)]) 

if __name__ == "__main__":
    unittest.main()
