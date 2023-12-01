# file to test swap_name.py

import unittest
from swap_name import swap_name

class TestSwapName(unittest.TestCase):
   # basic test
   def test_basic(self):
      name = 'John Smith'
      expected = 'Smith, John'
      self.assertEqual(swap_name(name), expected)
   
   def test_empty(self):
      name = ""
      expected = ""
      self.assertEqual(swap_name(name), expected)

if __name__ == "__main__":
   unittest.main()