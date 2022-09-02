import unittest
from translator import french_to_english, english_to_french 

class Tests(unittest.TestCase):

    def test_french_to_english(self):
        self.assertEqual(french_to_english(""), "there was an error")
        self.assertEqual(french_to_english("Bonjour"), "Hello")

    def test_english_to_french(self):
        self.assertEqual(english_to_french(""), "there was an error")
        self.assertEqual(english_to_french("Hello"), "Bonjour")

if __name__ == "__main__":
    unittest.main()