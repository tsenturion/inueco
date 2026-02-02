import unittest
from math_utils import divide, power

class test_math(unittest.TestCase):
    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(9, 3), 3)
        self.assertEqual(divide(5, 2), 2.5)

        with self.assertRaises(ValueError):
            divide(10, 0)
        
    def test_power(self):
        test = [
            (2, 3, 8),
            (5, 2, 25),
            (3, 3, 27),
            (10, 0, 1),
            (0, 5, 0),
            (1, 100, 1),
            (2, 10, 1024)
        ]
    
        for i, (a, b, expected) in enumerate(test):
            with self.subTest(case_number = i, base = a, degree = b):
                result = power(a, b)
                ERROR = f"Есть ошибка! {a} в степени {b}, должно быть {expected}, а получилось {result}"
                # ERROR :(
                self.assertEqual(result, expected, ERROR)

if __name__ == '__main__':
    unittest.main()