import unittest
import io
from io import StringIO
import sys
from scrapping import *
import scrapping as sc

class Test(unittest.TestCase):
    def test(self):
        op = io.StringIO()
        scrapping("ritvik.jain.52206")
        sys.stdout = op
        sys.stdout = sys.__stdout__
        self.assertEqual(op.getvalue(), "My name is Ritvik Jain and my current city is Roorkee\n")

if __name__ == "__main__":
    unittest.main()