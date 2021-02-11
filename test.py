# To run this file, click the shell tab on the right
# Use the following command:
#
# python test.py
#
# This is how you call python from the command line
# If you have it installed on your computer, it works the same way!
# You can also use this command: 
#
# python test.py -v
#
# The -v at the end is called a flag, in this case it stands for verbose
# Verbose means "using more words then necessary" and is a common flag to get more detailed output from a compile

import unittest
from main import is_odd

class TestIsOdd(unittest.TestCase):
# Note the naming convention. 
# Tests need to start with the word test
# They will not be run by unittest.main() if they don't follow that convention
    def test_odd_num(self):
        self.assertTrue(is_odd(3))

    def test_even_num(self):
        self.assertFalse(is_odd(8))

    #Edge Case
    def test_zero_num(self):
        self.assertFalse(is_odd(0))

    #Exception testing 
    def test_throws_exception(self):
        with self.assertRaises(Exception):
          is_odd('hello')

    #This does not get called
    def this_is_not_a_test(self):
        self.assertTrue(True)

    #This does get called 
    def test_this_is_not_a_test(self):
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
