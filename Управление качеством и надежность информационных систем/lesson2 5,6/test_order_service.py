import unittest
from unittest.mock import Mock, MagicMock

from order_service import InvalidItemError, EmptyCartError, PaymentError, OrderService

class TestOrderService(unittest.TestCase):

    def setUp(self):
        self.service = OrderService()

    def test_add_item_valid(self):
        self.service.add_item("Laptop", 5000)
        self.assertEqual(len(self.service.items), 1)
        self.assertEqual(self.service.items[0], {"name": "Laptop", "price": 5000})
    
    def test_add_item_invalid_name(self):
        with self.assertRaises(InvalidItemError):
            self.service.add_item("", 1000)
        with self.assertRaises(InvalidItemError):
            self.service.add_item(" ", 1000)
    
    def test_add_item_invalid_price(self):
        with self.assertRaises(InvalidItemError):
            self.service.add_item("lap", "10")
        with self.assertRaises(InvalidItemError):
            self.service.add_item("lap", 10.5)
        with self.assertRaises(InvalidItemError):
            self.service.add_item("Item", 0)
        with self.assertRaises(InvalidItemError):
            self.service.add_item("Item", -10)
        with self.assertRaises(InvalidItemError):
            self.service.add_item("Item", "100") 

    def test_apply_discount_valid(self):
        self.service.add_item("Phone", 100)
        
        self.service.apply_discount("SAVE10")
        self.assertEqual(self.service.discount, 0.10)
        
        self.service.apply_discount("SAVE20")
        self.assertEqual(self.service.discount, 0.20)

    def test_apply_discount_invalid_code(self):
        self.service.add_item("Phone", 100)
        with self.assertRaises(ValueError):
            self.service.apply_discount("UNKNOWN")

    def test_apply_discount_empty_cart(self):
        with self.assertRaises(EmptyCartError):
            self.service.apply_discount("SAVE10")

    def test_total_calculation_parametrized(self):
        scenarios = [
            ([("A", 100)], None, 100),               
            ([("A", 100)], "SAVE10", 90),             
            ([("A", 99)], "SAVE10", 89),              
            ([("A", 50), ("B", 70)], "SAVE20", 96),  
        ]

        for items_data, code, expected in scenarios:
            with self.subTest(items=items_data, code=code):
                self.service = OrderService() 
                
                for name, price in items_data:
                    self.service.add_item(name, price)
                
                if code:
                    self.service.apply_discount(code)
                
                self.assertEqual(self.service.total(), expected)

    def test_checkout_success(self):
        self.service.add_item("Book", 100)
        
        payment_gateway = Mock()
        payment_gateway.charge.return_value = "TXN_12345"
        
        result = self.service.checkout(payment_gateway)
        
        self.assertEqual(result, "TXN_12345")
        payment_gateway.charge.assert_called_once_with(100)

    def test_checkout_payment_failed(self):
        self.service.add_item("Book", 100)
        
        payment_gateway = Mock()
        payment_gateway.charge.side_effect = Exception("Connection Timeout")

        with self.assertRaises(PaymentError):
            self.service.checkout(payment_gateway)

    def test_checkout_empty_cart(self):
       
        payment_gateway = Mock()
        with self.assertRaises(EmptyCartError):
            self.service.checkout(payment_gateway)
        
        payment_gateway.charge.assert_not_called()

if __name__ == "__main__":
    unittest.main()
