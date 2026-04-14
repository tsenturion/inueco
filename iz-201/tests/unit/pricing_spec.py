import unittest
from shop.pricing import final_price_cents


class TestFinalPrice(unittest.TestCase):

    def test_basic_with_tax(self):
        self.assertEqual(final_price_cents(1000), 1200)

    def test_discount_applied(self):
        self.assertEqual(final_price_cents(1000, discount_percent=10, tax_percent=0), 900)

    def test_discount_and_tax(self):
        self.assertEqual(final_price_cents(1000, 10, 20), 1080)

    def test_discount_0_and_100_edges(self):
        self.assertEqual(final_price_cents(1000, 0, 0), 1000)
        self.assertEqual(final_price_cents(1000, 100, 0), 0)

    def test_tax_0_and_100_edges(self):
        self.assertEqual(final_price_cents(1000, 0, 0), 1000)
        self.assertEqual(final_price_cents(1000, 0, 100), 2000)

    def test_invalid_negative_base(self):
        with self.assertRaises(ValueError):
            final_price_cents(-1)

    def test_invalid_discount_range(self):
        for value in [-1, 101]:
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    final_price_cents(1000, discount_percent=value)

    def test_invalid_tax_range(self):
        for value in [-1, 101]:
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    final_price_cents(1000, tax_percent=value)

    def test_invalid_types(self):
        for args in [
            (None, 0, 0),
            ("100", 0, 0),
            (1000, "10", 0),
            (1000, 0, "20"),
        ]:
            with self.subTest(args=args):
                with self.assertRaises(TypeError):
                    final_price_cents(*args)

    def test_bool_is_invalid(self):
        for args in [
            (True, 0, 0),
            (1000, True, 0),
        ]:
            with self.subTest(args=args):
                with self.assertRaises(TypeError):
                    final_price_cents(*args)