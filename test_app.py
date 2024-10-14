import unittest
from app import add, subtract, multiplication, division

class TestApp(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(5, 5), 0)
    
    def test_multiplication(self):
        self.assertEqual(multiplication(5, 3), 15)
        self.assertEqual(multiplication(5, 5), 25)
    
    def test_division(self):
        self.assertEqual(division(5, 5), 1.0)
        self.assertEqual(division(10, 2), 5.0)

if __name__ == '__main__':
    unittest.main()
