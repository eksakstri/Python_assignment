import unittest
from scrapping import *
import scrapping as sc

class Test(unittest.TestCase):
    def test(self):
        #op = io.StringIO()
        op = scrapping("ritvik.jain.52206")
        self.assertEqual(op, "My name is Ritvik Jain and my current city is Roorkee")
        #print(op.getvalue())

if __name__ == "__main__":
    unittest.main()

"""'My name is Ritvik Jain and my current city is Roorkee'
sys.stdout = op
sys.stdout = sys.__stdout__"""