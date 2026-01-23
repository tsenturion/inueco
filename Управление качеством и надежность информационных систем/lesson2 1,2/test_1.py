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
    def test_power_positive(self):
        """Тест возведения положительных чисел в положительную степень"""
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 2), 25)
        self.assertEqual(power(3, 4), 81)
        
    def test_power_zero_exponent(self):
        """Тест: любое число в степени 0 равно 1"""
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(100, 0), 1)
        self.assertEqual(power(-5, 0), 1)
        self.assertEqual(power(0, 0), 1)  # По определению в математике
        
    def test_power_one_exponent(self):
        """Тест: любое число в степени 1 равно самому себе"""
        self.assertEqual(power(5, 1), 5)
        self.assertEqual(power(-3, 1), -3)
        self.assertEqual(power(0, 1), 0)
        
    def test_power_negative_exponent(self):
        """Тест возведения в отрицательную степень"""
        self.assertEqual(power(2, -2), 0.25)   # 1/4
        self.assertEqual(power(5, -1), 0.2)    # 1/5
        self.assertEqual(power(10, -3), 0.001) # 1/1000
        
    def test_power_fractional_exponent(self):
        """Тест возведения в дробную степень (корни)"""
        self.assertAlmostEqual(power(4, 0.5), 2.0)      # квадратный корень
        self.assertAlmostEqual(power(8, 1/3), 2.0)      # кубический корень
        self.assertAlmostEqual(power(9, 0.5), 3.0)      # квадратный корень
        
    def test_power_negative_base(self):
        """Тест возведения отрицательных чисел в степень"""
        self.assertEqual(power(-2, 2), 4)      # (-2)² = 4
        self.assertEqual(power(-2, 3), -8)     # (-2)³ = -8
        self.assertEqual(power(-3, 4), 81)     # (-3)⁴ = 81
        
    def test_power_decimal_base(self):
        """Тест возведения десятичных чисел"""
        self.assertAlmostEqual(power(2.5, 2), 6.25)
        self.assertAlmostEqual(power(0.5, 2), 0.25)
        self.assertAlmostEqual(power(1.5, 3), 3.375)


if __name__ == '__main__':
    unittest.main()