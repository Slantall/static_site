import unittest

from main import *



class TestTitle(unittest.TestCase):
    def test_extract_title(self):
        string = "test \n\n# this is the title \n\nnot this"
        self.assertEqual(extract_title(string), "this is the title")





if __name__ == "__main__":
    unittest.main()