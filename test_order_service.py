import unittest
from unittest.mock import Mock, MagicMock
from order_service import OrderService, InvalidItemError, EmptyCartError, PaymentError


class TestOrderService(unittest.TestCase):
    def setUp(self):
        """Создаем новый экземпляр OrderService перед каждым тестом"""
        self.service = OrderService()
    
    def _add_sample_items(self):
        """Вспомогательный метод для добавления тестовых товаров"""
        self.service.add_item("Товар A", 100)
        self.service.add_item("Товар B", 200)
    
    # Тесты валидации товаров
    def test_add_item_valid(self):
        """Проверка добавления валидного товара"""
        self.service.add_item("Тестовый товар", 150)
        self.assertEqual(self.service.total(), 150)
    
    def test_add_item_empty_name(self):
        """Проверка добавления товара с пустым именем"""
        with self.assertRaises(InvalidItemError):
            self.service.add_item("", 100)
        
        with self.assertRaises(InvalidItemError):
            self.service.add_item("   ", 100)
    
    def test_add_item_invalid_price(self):
        """Проверка добавления товара с невалидной ценой"""
        # Цена <= 0
        with self.assertRaises(InvalidItemError):
            self.service.add_item("Товар", 0)
        
        with self.assertRaises(InvalidItemError):
            self.service.add_item("Товар", -10)
        
        # Нецелочисленная цена
        with self.assertRaises(InvalidItemError):
            self.service.add_item("Товар", "100")  # строка
        
        with self.assertRaises(InvalidItemError):
            self.service.add_item("Товар", 99.99)  # float
    
    # Тесты применения скидок
    def test_apply_discount_save10(self):
        """Проверка применения скидки 10%"""
        self._add_sample_items()  # 100 + 200 = 300
        
        self.service.apply_discount("SAVE10")
        self.assertEqual(self.service.total(), 270)  # 300 - 10%
    
    def test_apply_discount_save20(self):
        """Проверка применения скидки 20%"""
        self.service.add_item("Товар", 500)
        self.service.apply_discount("SAVE20")
        self.assertEqual(self.service.total(), 400)  # 500 - 20%
    
    def test_apply_discount_unknown_code(self):
        """Проверка применения неизвестного промокода"""
        self._add_sample_items()
        
        with self.assertRaises(ValueError):
            self.service.apply_discount("INVALID")
    
    def test_apply_discount_empty_cart(self):
        """Проверка применения скидки к пустой корзине"""
        with self.assertRaises(EmptyCartError):
            self.service.apply_discount("SAVE10")
    
    # Параметризация через subTest
    def test_total_with_discounts(self):
        """Проверка расчета итоговой стоимости с различными скидками"""
        test_cases = [
            # (товары, промокод, ожидаемый результат)
            ([("A", 100)], None, 100),
            ([("A", 100)], "SAVE10", 90),
            ([("A", 99)], "SAVE10", 89),  # Проверка округления вниз
            ([("A", 50), ("B", 70)], "SAVE20", 96),  # (50+70)-20% = 96
            ([("A", 100), ("B", 200), ("C", 300)], "SAVE10", 540),  # 600-10%
        ]
        
        for items, discount_code, expected in test_cases:
            with self.subTest(items=items, discount=discount_code, expected=expected):
                # Создаем новый сервис для каждого подтеста
                service = OrderService()
                
                # Добавляем товары
                for name, price in items:
                    service.add_item(name, price)
                
                # Применяем скидку если указана
                if discount_code:
                    service.apply_discount(discount_code)
                
                # Проверяем результат
                self.assertEqual(service.total(), expected)
    
    # Тесты оформления заказа
    def test_checkout_success(self):
        """Успешное оформление заказа"""
        self.service.add_item("Товар", 100)
        
        # Создаем мок платежного шлюза
        mock_gateway = Mock()
        mock_gateway.charge.return_value = "TRANSACTION_12345"
        
        result = self.service.checkout(mock_gateway)
        
        # Проверяем, что charge был вызван с правильной суммой
        mock_gateway.charge.assert_called_once_with(100)
        
        # Проверяем, что возвращается правильный ID транзакции
        self.assertEqual(result, "TRANSACTION_12345")
    
    def test_checkout_empty_cart(self):
        """Оформление пустой корзины"""
        mock_gateway = Mock()
        
        with self.assertRaises(EmptyCartError):
            self.service.checkout(mock_gateway)
        
        # Убеждаемся, что charge не вызывался
        mock_gateway.charge.assert_not_called()
    
    def test_checkout_payment_error(self):
        """Ошибка при оплате"""
        self.service.add_item("Товар", 100)
        
        # Создаем мок, который вызывает исключение
        mock_gateway = Mock()
        mock_gateway.charge.side_effect = Exception("Недостаточно средств")
        
        # Проверяем, что PaymentError выбрасывается
        with self.assertRaises(PaymentError):
            self.service.checkout(mock_gateway)
        
        # Убеждаемся, что charge был вызван
        mock_gateway.charge.assert_called_once_with(100)
    
    def test_checkout_with_discount(self):
        """Оформление заказа со скидкой"""
        self.service.add_item("Товар A", 100)
        self.service.add_item("Товар B", 200)
        self.service.apply_discount("SAVE10")  # 300 - 10% = 270
        
        mock_gateway = Mock()
        mock_gateway.charge.return_value = "TRANSACTION_999"
        
        result = self.service.checkout(mock_gateway)
        
        # Проверяем, что charge был вызван с суммой после скидки
        mock_gateway.charge.assert_called_once_with(270)
        self.assertEqual(result, "TRANSACTION_999")
    
    def test_checkout_clear_cart_after_success(self):
        """Дополнительный тест: очистка корзины после успешного оформления"""
        self.service.add_item("Товар", 100)
        
        mock_gateway = Mock()
        mock_gateway.charge.return_value = "TRANSACTION_123"
        
        # Оформляем заказ
        self.service.checkout(mock_gateway)
        
        # Проверяем, что корзина пуста
        self.assertEqual(self.service.total(), 0)
        
        # Пытаемся оформить снова - должно быть исключение
        with self.assertRaises(EmptyCartError):
            self.service.checkout(mock_gateway)


if __name__ == "__main__":
    unittest.main()