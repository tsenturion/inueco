import unittest
from unittest.mock import Mock, MagicMock
from order_service import OrderService, InvalidItemError, EmptyCartError, PaymentError


class TestOrderService(unittest.TestCase):
    def setUp(self):
        """Создаём новый экземпляр OrderService перед каждым тестом"""
        self.service = OrderService()
    
    # Вспомогательные методы
    def _add_sample_items(self):
        """Добавляет тестовые товары в корзину"""
        self.service.add_item("Товар 1", 100)
        self.service.add_item("Товар 2", 200)
    
    # Тесты валидации товаров
    def test_add_item_with_empty_name_raises_error(self):
        """Тест: добавление товара с пустым именем вызывает InvalidItemError"""
        test_cases = ["", "   ", " \t\n "]
        
        for name in test_cases:
            with self.subTest(name=name):
                with self.assertRaises(InvalidItemError):
                    self.service.add_item(name, 100)
    
    def test_add_item_with_invalid_price_raises_error(self):
        """Тест: добавление товара с невалидной ценой вызывает InvalidItemError"""
        # price <= 0
        with self.assertRaises(InvalidItemError):
            self.service.add_item("Товар", 0)
        
        with self.assertRaises(InvalidItemError):
            self.service.add_item("Товар", -10)
        
        # Нецелочисленный price
        with self.assertRaises(InvalidItemError):
            self.service.add_item("Товар", "10")  # строка
        
        with self.assertRaises(InvalidItemError):
            self.service.add_item("Товар", 10.5)  # float
    
    def test_add_valid_item_success(self):
        """Тест: добавление валидного товара работает корректно"""
        self.service.add_item("Товар", 100)
        self.assertEqual(len(self.service.items), 1)
        self.assertEqual(self.service.items[0], ("Товар", 100))
        
        # Проверка strip() для имени
        self.service.add_item("  Товар 2  ", 200)
        self.assertEqual(self.service.items[1], ("Товар 2", 200))
    
    # Тесты применения скидок
    def test_apply_discount_with_empty_cart_raises_error(self):
        """Тест: применение скидки к пустой корзине вызывает EmptyCartError"""
        with self.assertRaises(EmptyCartError):
            self.service.apply_discount("SAVE10")
    
    def test_apply_unknown_discount_code_raises_error(self):
        """Тест: неизвестный промокод вызывает ValueError"""
        self._add_sample_items()
        
        with self.assertRaises(ValueError):
            self.service.apply_discount("INVALID")
    
    def test_apply_valid_discount_success(self):
        """Тест: применение валидного промокода работает корректно"""
        self._add_sample_items()
        
        self.service.apply_discount("SAVE10")
        self.assertEqual(self.service.discount, 10)
        
        # Сброс и проверка другого промокода
        self.service.discount = 0
        self.service.apply_discount("SAVE20")
        self.assertEqual(self.service.discount, 20)
    
    # Тесты расчёта итоговой суммы с использованием subTest
    def test_total_with_discounts(self):
        """Тест: расчёт итоговой суммы с различными скидками"""
        test_cases = [
            # (items, discount_code, expected_total)
            ([("A", 100)], None, 100),
            ([("A", 100)], "SAVE10", 90),
            ([("A", 99)], "SAVE10", 89),  # 99 - 9.9 = 89.1 → 89
            ([("A", 50), ("B", 70)], None, 120),
            ([("A", 50), ("B", 70)], "SAVE20", 96),  # 120 - 24 = 96
            ([("A", 333)], "SAVE10", 299),  # 333 - 33.3 = 299.7 → 299
        ]
        
        for items, discount_code, expected_total in test_cases:
            with self.subTest(items=items, discount_code=discount_code):
                # Создаём новый сервис для каждого подтеста
                service = OrderService()
                
                # Добавляем товары
                for name, price in items:
                    service.add_item(name, price)
                
                # Применяем скидку
                if discount_code:
                    service.apply_discount(discount_code)
                
                # Проверяем результат
                self.assertEqual(service.total(), expected_total)
    
    # Тесты оформления заказа
    def test_checkout_with_empty_cart_raises_error(self):
        """Тест: оформление пустой корзины вызывает EmptyCartError"""
        mock_gateway = Mock()
        
        with self.assertRaises(EmptyCartError):
            self.service.checkout(mock_gateway)
    
    def test_checkout_with_payment_error_raises_payment_error(self):
        """Тест: ошибка платёжного шлюза вызывает PaymentError"""
        self._add_sample_items()
        
        # Мокируем шлюз, который выбрасывает исключение
        mock_gateway = Mock()
        mock_gateway.charge.side_effect = Exception("Недостаточно средств")
        
        with self.assertRaises(PaymentError):
            self.service.checkout(mock_gateway)
    
    def test_checkout_success_with_mock(self):
        """Тест: успешное оформление заказа с проверкой моков"""
        self._add_sample_items()
        
        # Создаём мок и задаём возвращаемое значение
        mock_gateway = Mock()
        mock_gateway.charge.return_value = "TX123456"
        
        # Вызываем метод checkout
        transaction_id = self.service.checkout(mock_gateway)
        
        # Проверяем результат
        self.assertEqual(transaction_id, "TX123456")
        
        # Проверяем вызовы мока
        mock_gateway.charge.assert_called_once_with(300)  # 100 + 200 = 300
    
    # Дополнительные тесты
    def test_total_without_discount(self):
        """Тест: расчёт суммы без скидки"""
        self.service.add_item("Товар 1", 150)
        self.service.add_item("Товар 2", 250)
        self.assertEqual(self.service.total(), 400)
    
    def test_multiple_discount_applications(self):
        """Тест: применение нескольких скидок (последняя должна перезаписать предыдущую)"""
        self._add_sample_items()
        
        self.service.apply_discount("SAVE10")
        self.assertEqual(self.service.discount, 10)
        
        self.service.apply_discount("SAVE20")
        self.assertEqual(self.service.discount, 20)
        self.assertEqual(self.service.total(), 240)  # 300 - 20% = 240
    
    def test_checkout_with_different_amounts(self):
        """Тест: оформление заказа с разными суммами"""
        test_cases = [
            ([("A", 100)], 100),
            ([("A", 100)], 90),  # с SAVE10
            ([("A", 50), ("B", 150)], 160),  # с SAVE20 (200 - 20% = 160)
        ]
        
        for items, expected_amount in test_cases:
            with self.subTest(items=items, expected_amount=expected_amount):
                service = OrderService()
                
                for name, price in items:
                    service.add_item(name, price)
                
                if expected_amount < sum(price for _, price in items):
                    service.apply_discount("SAVE20" if expected_amount == 160 else "SAVE10")
                
                mock_gateway = Mock()
                mock_gateway.charge.return_value = "TX_TEST"
                
                transaction_id = service.checkout(mock_gateway)
                
                self.assertEqual(transaction_id, "TX_TEST")
                mock_gateway.charge.assert_called_once_with(expected_amount)


if __name__ == '__main__':
    unittest.main()