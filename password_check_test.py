import unittest
from strongpassword import *

class TestPasswordChecker(unittest.TestCase):
    def test_has_caps(self):
       password = 'Hellotheremate7'
       self.assertEqual(hasCaps(password), True)
       self.assertNotEqual(hasCaps('no caps'), True)
    
    def test_has_digits(self):
        password = 'Hellotheremate7'
        self.assertEqual(hasDigit(password), True)
        self.assertNotEqual(hasDigit('no digits'), True)
      

unittest.main()