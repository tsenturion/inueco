import unittest
from math_utils import divide
from math_utils import pow


class TestDivide(unittest.TestCase):
    def test_correct_division(self):
        result = divide(10, 2)
        self.assertEqual(result, 5)
        
    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

#протестировать функцию pow

class TestPow(unittest.TestCase):
    def test_correct_power(self):
        result = pow(5, 2)
        self.assertEqual(result, 25)

if __name__ == '__main__':
    unittest.main()