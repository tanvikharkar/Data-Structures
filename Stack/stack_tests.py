import unittest

# Use the imports below to test either your array-based stack
# or your link-based version
from stack_array import Stack
from stack_linked import Stack, Node

class TestLab2(unittest.TestCase):
    def test_simple(self):
        stack = Stack(5)
        stack.push(0)
        self.assertFalse(stack.is_empty())
        self.assertFalse(stack.is_full())
        self.assertEqual(stack.size(),1)
    
    def test(self):
        stack = Stack(1)
        stack.push(5)
        self.assertTrue(stack.is_full())
        self.assertTrue(stack.peek(), 5)
        stack.pop()
        self.assertTrue(stack.is_empty())

if __name__ == '__main__': 
    unittest.main()
