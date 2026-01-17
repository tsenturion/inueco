import unittest
from math_utils import divide, power  

class TestDivide(unittest.TestCase):
    def test_correct_division(self):
        result = divide(10, 2)
        self.assertEqual(result, 5)
        
    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

class TestPower(unittest.TestCase):
    def test_correct_power(self):  
        result = power(2, 5)
        self.assertEqual(result, 32)
    
    def test_power_zero_exponent(self):
        result = power(5, 0)
        self.assertEqual(result, 1)
    
    def test_power_negative_exponent(self):
        result = power(2, -2)
        self.assertEqual(result, 0.25)

if __name__ == '__main__':  
    unittest.main()