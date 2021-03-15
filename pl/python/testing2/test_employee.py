import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):

    # εκτελείται 1 φορά στη αρχή
    @classmethod
    def setUpClass(cls):
        print('setupClass')

    # εκτελείται 1 φορά στο τέλος
    @classmethod
    def tearDownClass(cls):
        print('TeardownClass')

    # εκτελείται πριν από κάθε test
    def setUp(self):
        self.emp1 = Employee("John", "Doe", 50000)
        self.emp2 = Employee("Bill", "Smith", 60000)

    # εκτελείται μετά από κάθε test
    def tearDown(self):
        print('Teardown')

    def test_email(self):
        self.assertEqual(self.emp1.email, "John.Doe@email.com")
        self.assertEqual(self.emp2.email, "Bill.Smith@email.com")

    def test_fullname(self):
        self.assertEqual(self.emp1.fullname, "John Doe")
        self.assertEqual(self.emp2.fullname, "Bill Smith")


if __name__ == "__main__":
    unittest.main()
