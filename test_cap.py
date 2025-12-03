
import unittest
import cap #importing cap.py module

class TestCap(unittest.TestCase):

    def test_one_word(self):
        text = 'python'
        result = cap.title(text) #using module.method of cap.py
        self.assertEqual(result,'Python')

    def test_multiple_words(self):
        text = 'Monty Python'
        result = cap.title(text)
        self.assertEqual(result,'Monty Python')

if __name__ == '__main__':
    unittest.main()
