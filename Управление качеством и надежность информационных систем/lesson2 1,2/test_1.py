import unittest
from math_utils import divide


class TestDivide(unittest.TestCase):
    def test_correct_division(self):
        result = divide(10, 2)
        self.assertEqual(result, 5)
        
    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_correct_pow(self):
        result = pow(5, 7)
        self.assertEqual(result, 78125)

    def test_pow_by_zero_b(self):
        result = pow(10, 0)
        self.assertEqual(result, 1)

    def test_pow_by_less_then_zero_b(self):
        result = pow(2, -1)
        self.assertEqual(result, 0.5)

#протестировать функцию pow


if __name__ == '__main__':
    unittest.main()