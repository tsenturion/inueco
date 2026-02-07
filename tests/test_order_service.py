import unittest
from unittest.mock import Mock, MagicMock
from order_service import OrderService, InvalidItemError, EmptyCartError, PaymentError

class TestOrderService(unittest.TestCase):

    def setUp(self):
        self.service = OrderService()

    def test_add_item_invalid_name(self):
        with self.assertRaises(InvalidItemError):
            self.service.add_item("", 100)
        with self.assertRaises(InvalidItemError):
            self.service.add_item("   ", 100)

    def test_add_item_invalid_price(self):
        with self.assertRaises(InvalidItemError):
            self.service.add_item("Apple", 0)
        with self.assertRaises(InvalidItemError):
            self.service.add_item("Apple", -10)
        with self.assertRaises(InvalidItemError):
            self.service.add_item("Apple", 10.5)  
        with self.assertRaises(InvalidItemError):
            self.service.add_item("Apple", "100") 

    def test_apply_discount_success(self):
        self.service.add_item("Item1", 100)
        self.service.apply_discount("SAVE10")
        self.assertEqual(self.service.total(), 90)
        self.service.apply_discount("SAVE20")
        self.assertEqual(self.service.total(), 80)

    def test_apply_discount_unknown_code(self):
        self.service.add_item("Item1", 100)
        with self.assertRaises(ValueError):
            self.service.apply_discount("UNKNOWN")

    def test_apply_discount_empty_cart(self):
        with self.assertRaises(EmptyCartError):
            self.service.apply_discount("SAVE10")

    def test_checkout_empty_cart(self):
        mock_gateway = Mock()
        with self.assertRaises(EmptyCartError):
            self.service.checkout(mock_gateway)

    def test_checkout_payment_failure(self):
        self.service.add_item("Item1", 100)
        mock_gateway = Mock()
        mock_gateway.charge.side_effect = Exception("Connection failed")
        with self.assertRaises(PaymentError):
            self.service.checkout(mock_gateway)

    def test_total_calculation_subtests(self):
        test_cases = [
            ([("A", 100)], None, 100),
            ([("A", 100)], "SAVE10", 90),
            ([("A", 99)], "SAVE10", 89), 
            ([("A", 50), ("B", 70)], "SAVE20", 96), 
            ([("A", 10), ("B", 20)], None, 30),
        ]

        for items, code, expected in test_cases:
            with self.subTest(items=items, code=code, expected=expected):
                local_service = OrderService()
                for name, price in items:
                    local_service.add_item(name, price)
                
                if code:
                    local_service.apply_discount(code)
                
                self.assertEqual(local_service.total(), expected)

    def test_checkout_success_mock(self):
        self.service.add_item("Laptop", 1000)
        self.service.apply_discount("SAVE10") 
        mock_gateway = Mock()
        mock_gateway.charge.return_value = "trans_xyz_123"
        result = self.service.checkout(mock_gateway)
        self.assertEqual(result, "trans_xyz_123")
        mock_gateway.charge.assert_called_once_with(900)

if __name__ == "__main__":
    unittest.main()