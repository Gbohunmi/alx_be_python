import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1, -1), -2)
        self.assertEqual(self.calc.add(3, -1), 2)
        # Add more assertions to thoroughly test the add method.
    
    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(4, 3), 1)
        self.assertEqual(self.calc.subtract(-1, 1), -2)
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        self.assertEqual(self.calc.subtract(3, -1), 4)    

    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(-1, -1), 1)
        self.assertEqual(self.calc.multiply(3, 0), 0)

    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(2, 4), 0.5)
        self.assertEqual(self.calc.divide(0, 1), 0)
        self.assertEqual(self.calc.divide(-1, -1), 1)
        self.assertEqual(self.calc.divide(3, -1), -3)
        self.assertEqual(self.calc.divide(4, 2), 2)
        self.assertEqual(self.calc.divide(3, 0), None)
 

# Remember to write additional test methods for subtract, multiply, and divide