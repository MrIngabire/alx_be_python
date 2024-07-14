import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the add method of SimpleCalculator."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        # Add more test cases as needed to thoroughly test the add method

    def test_subtraction(self):
        """Test the subtract method of SimpleCalculator."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(-1, 1), -2)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        # Add more test cases as needed to thoroughly test the subtract method

    def test_multiplication(self):
        """Test the multiply method of SimpleCalculator."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        # Add more test cases as needed to thoroughly test the multiply method

    def test_division(self):
        """Test the divide method of SimpleCalculator."""
        # Test normal division
        self.assertEqual(self.calc.divide(6, 3), 2.0)
        self.assertEqual(self.calc.divide(-6, 3), -2.0)
        self.assertEqual(self.calc.divide(0, 5), 0.0)

        # Test division by zero
        self.assertIsNone(self.calc.divide(5, 0))

    # Add more test methods as needed to cover additional scenarios

if __name__ == "__main__":
    unittest.main()

