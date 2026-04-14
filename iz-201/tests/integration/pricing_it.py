import unittest
from shop.pricing import final_price_cents


class TestPricingIntegration(unittest.TestCase):

    def test_full_flow_typical_purchase(self):
        result = final_price_cents(2500, discount_percent=20, tax_percent=20)
        self.assertEqual(result, 2400)

    def test_zero_discount_high_tax(self):
        result = final_price_cents(1000, discount_percent=0, tax_percent=50)
        self.assertEqual(result, 1500)

    def test_free_after_discount(self):
        result = final_price_cents(9999, discount_percent=100, tax_percent=20)
        self.assertEqual(result, 0)
        