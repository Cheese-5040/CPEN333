from demo import Arithmetic

import unittest

class Test(unittest.TestCase):
    def test_add(self): 
        a, b = -1, 15
        arithmetic = Arithmetic()
        self.assertEqual(arithmetic.add(a,b), a+b)
    def test_subtract(self): 
        a,b = -1, 15
        arithmetic = Arithmetic()
        self.assertEqual(arithmetic.subtract(a, b), a-b)

if __name__ == '__main__':
    unittest.main()
