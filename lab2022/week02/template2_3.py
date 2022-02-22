import unittest


def longest_words(s):
    pass


# Mην αλλάξετε κάτι από εδώ και κάτω
class TestLongestWords(unittest.TestCase):
    def test(self):
        s1 = ""
        self.assertEqual(longest_words(s1), [])
        s2 = "arta"
        self.assertEqual(longest_words(s2), ["arta"])
        s3 = "arta Άρτα"
        self.assertEqual(longest_words(s3), ["arta", "Άρτα"])
        s4 = "....arta,,, Άρτα....."
        self.assertEqual(longest_words(s4), ["arta", "Άρτα"])
        s5 = "ab,,cd..ef gh.."
        self.assertEqual(longest_words(s5), ["ab", "cd", "ef", "gh"])
        s6 = """Το Lorem Ipsum είναι απλά ένα κείμενο χωρίς νόημα για τους επαγγελματίες της τυπογραφίας και στοιχειοθεσίας Το Lorem Ipsum είναι το επαγγελματικό πρότυπο όσον αφορά το κείμενο χωρίς νόημα, από τον 15ο αιώνα, όταν ένας ανώνυμος τυπογράφος πήρε ένα δοκίμιο και ανακάτεψε τις λέξεις για να δημιουργήσει ένα δείγμα βιβλίου Όχι μόνο επιβίωσε πέντε αιώνες αλλά κυριάρχησε στην ηλεκτρονική στοιχειοθεσία παραμένοντας με κάθε τρόπο αναλλοίωτο Έγινε δημοφιλές τη δεκαετία του '60 με την έκδοση των δειγμάτων της Letraset όπου περιελάμβαναν αποσπάσματα του Lorem Ipsum και πιο πρόσφατα με το λογισμικό ηλεκτρονικής σελιδοποίησης όπως το Aldus PageMaker που περιείχαν εκδοχές του Lorem Ipsum"""
        self.assertEqual(longest_words(s6), ["στοιχειοθεσίας"])
        s7 = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""
        self.assertEqual(longest_words(s7), ["reprehenderit"])


if __name__ == "__main__":
    unittest.main()
