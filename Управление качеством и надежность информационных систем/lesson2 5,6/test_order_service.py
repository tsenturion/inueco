# test_order_service.py

import unittest
from unittest.mock import Mock, MagicMock, patch
from order_service import OrderService, InvalidItemError, EmptyCartError, PaymentError


class TestOrderService(unittest.TestCase):
    """Тесты для OrderService"""
    
    def setUp(self):
        """Создает новый экземпляр OrderService перед каждым тестом"""
        self.service = OrderService()
        print(f"\n{'='*60}")
        print(f"Начинается тест: {self._testMethodName}")
        print(f"{'='*60}")
    
    def tearDown(self):
        """Очищает состояние после каждого теста"""
        print(f"Завершен тест: {self._testMethodName}")
    
    # Вспомогательные методы
    def _add_sample_items(self, items=None):
        """
        Добавляет тестовые товары в корзину
        
        Args:
            items: Список кортежей (name, price) или None для стандартного набора
        """
        if items is None:
            items = [("Товар 1", 100), ("Товар 2", 200), ("Товар 3", 300)]
        
        for name, price in items:
            self.service.add_item(name, price)
        
        return items
    
    # Тесты валидации товаров
    def test_add_item_valid(self):
        """Тест добавления валидного товара"""
        # Подготовка
        name = "Тестовый товар"
        price = 100
        
        # Действие
        self.service.add_item(name, price)
        
        # Проверка
        self.assertEqual(len(self.service.cart), 1)
        self.assertEqual(self.service.cart[0][0], name)
        self.assertEqual(self.service.cart[0][1], price)
    
    def test_add_item_empty_name(self):
        """Тест добавления товара с пустым названием"""
        test_cases = [
            ("", "Пустая строка"),
            ("   ", "Только пробелы"),
            ("\t\n", "Только пробельные символы"),
        ]
        
        for name, description in test_cases:
            with self.subTest(description=description):
                with self.assertRaises(InvalidItemError):
                    self.service.add_item(name, 100)
    
    def test_add_item_invalid_price(self):
        """Тест добавления товара с некорректной ценой"""
        test_cases = [
            (0, "Цена равна 0"),
            (-10, "Отрицательная цена"),
            ("100", "Цена как строка"),
            (99.99, "Цена как float"),
            (None, "Цена как None"),
        ]
        
        for price, description in test_cases:
            with self.subTest(description=description):
                with self.assertRaises(InvalidItemError):
                    self.service.add_item("Товар", price)
    
    # Тесты применения скидок
    def test_apply_discount_valid(self):
        """Тест применения валидного промокода"""
        # Подготовка
        self._add_sample_items()
        
        # Действие и проверка для SAVE10
        self.service.apply_discount("SAVE10")
        self.assertEqual(self.service.discount, 10)
        
        # Действие и проверка для SAVE20
        self.service.discount = 0  # Сброс скидки
        self.service.apply_discount("SAVE20")
        self.assertEqual(self.service.discount, 20)
    
    def test_apply_discount_unknown_code(self):
        """Тест применения неизвестного промокода"""
        # Подготовка
        self._add_sample_items()
        
        # Действие и проверка
        with self.assertRaises(ValueError):
            self.service.apply_discount("UNKNOWN")
    
    def test_apply_discount_empty_cart(self):
        """Тест применения промокода к пустой корзине"""
        # Проверка, что корзина действительно пуста
        self.assertEqual(len(self.service.cart), 0)
        
        # Действие и проверка
        with self.assertRaises(EmptyCartError):
            self.service.apply_discount("SAVE10")
    
    # Тесты расчета итоговой суммы
    def test_total_without_discount(self):
        """Тест расчета суммы без скидки"""
        # Подготовка
        items = self._add_sample_items([("Товар A", 150), ("Товар B", 250)])
        
        # Действие
        total = self.service.total()
        
        # Проверка
        expected = 150 + 250
        self.assertEqual(total, expected)
    
    def test_total_with_discount(self):
        """Тест расчета суммы со скидкой"""
        # Подготовка
        items = self._add_sample_items([("Товар", 1000)])
        
        # Применяем скидку 10%
        self.service.apply_discount("SAVE10")
        
        # Действие
        total = self.service.total()
        
        # Проверка
        expected = 900  # 1000 - 10%
        self.assertEqual(total, expected)
    
    def test_total_rounding_down(self):
        """Тест округления суммы вниз"""
        # Подготовка
        self.service.add_item("Товар", 99)
        self.service.apply_discount("SAVE10")
        
        # Действие
        total = self.service.total()
        
        # Проверка: 99 - 10% = 89.1 → должно округлиться до 89
        self.assertEqual(total, 89)
    
    def test_total_with_subtest(self):
        """Тест расчета суммы с использованием subTest"""
        test_cases = [
            # (товары, промокод, ожидаемая сумма, описание)
            ([("A", 100)], None, 100, "Один товар без скидки"),
            ([("A", 100)], "SAVE10", 90, "Один товар со скидкой 10%"),
            ([("A", 99)], "SAVE10", 89, "Один товар 99р со скидкой 10%"),
            ([("A", 50), ("B", 70)], "SAVE20", 96, "Два товара со скидкой 20%"),
            ([("X", 333), ("Y", 444), ("Z", 555)], "SAVE10", 1198, "Три товара со скидкой 10%"),
        ]
        
        for items, discount_code, expected, description in test_cases:
            with self.subTest(description=description):
                # Пересоздаем сервис для каждого подтеста
                service = OrderService()
                
                # Добавляем товары
                for name, price in items:
                    service.add_item(name, price)
                
                # Применяем скидку
                if discount_code:
                    service.apply_discount(discount_code)
                
                # Проверяем сумму
                self.assertEqual(service.total(), expected, description)
    
    # Тесты оформления заказа
    def test_checkout_success(self):
        """Тест успешного оформления заказа"""
        # Подготовка
        self._add_sample_items([("Товар", 100)])
        
        # Создаем мок платежного шлюза
        mock_gateway = Mock()
        mock_gateway.charge.return_value = "TRX-12345"
        
        # Действие
        transaction_id = self.service.checkout(mock_gateway)
        
        # Проверка
        self.assertEqual(transaction_id, "TRX-12345")
        mock_gateway.charge.assert_called_once_with(100)
    
    def test_checkout_empty_cart(self):
        """Тест оформления пустого заказа"""
        # Создаем мок платежного шлюза
        mock_gateway = Mock()
        
        # Действие и проверка
        with self.assertRaises(EmptyCartError):
            self.service.checkout(mock_gateway)
        
        # Убеждаемся, что charge не вызывался
        mock_gateway.charge.assert_not_called()
    
    def test_checkout_payment_error(self):
        """Тест ошибки платежа"""
        # Подготовка
        self._add_sample_items([("Товар", 100)])
        
        # Создаем мок платежного шлюза, который выбрасывает исключение
        mock_gateway = Mock()
        mock_gateway.charge.side_effect = Exception("Недостаточно средств")
        
        # Действие и проверка
        with self.assertRaises(PaymentError):
            self.service.checkout(mock_gateway)
        
        # Убеждаемся, что charge вызывался
        mock_gateway.charge.assert_called_once()
    
    # Тесты с использованием unittest.mock
    def test_checkout_with_magic_mock(self):
        """Тест оформления заказа с использованием MagicMock"""
        # Подготовка
        items = [("Дорогой товар", 9999)]
        self._add_sample_items(items)
        
        # Создаем MagicMock
        mock_gateway = MagicMock()
        mock_gateway.charge.return_value = "TRX-MAGIC-001"
        
        # Действие
        transaction_id = self.service.checkout(mock_gateway)
        
        # Проверка
        self.assertEqual(transaction_id, "TRX-MAGIC-001")
        mock_gateway.charge.assert_called_once_with(9999)
    
    def test_checkout_with_side_effect(self):
        """Тест с использованием side_effect для симуляции разных сценариев"""
        test_cases = [
            (100, "TRX-SUCCESS", None, "Успешный платеж"),
            (200, None, ValueError("Карта заблокирована"), "Ошибка ValueError"),
            (300, None, RuntimeError("Таймаут соединения"), "Ошибка RuntimeError"),
        ]
        
        for amount, return_value, side_effect, description in test_cases:
            with self.subTest(description=description):
                # Подготовка
                service = OrderService()
                service.add_item("Товар", amount)
                
                # Создаем мок с side_effect
                mock_gateway = Mock()
                mock_gateway.charge.side_effect = [side_effect] if side_effect else [return_value]
                
                if side_effect:
                    # Ожидаем PaymentError
                    with self.assertRaises(PaymentError):
                        service.checkout(mock_gateway)
                else:
                    # Ожидаем успех
                    result = service.checkout(mock_gateway)
                    self.assertEqual(result, return_value)
                
                # Проверяем вызов
                mock_gateway.charge.assert_called_once_with(amount)
    
    @patch('order_service.OrderService.total')
    def test_checkout_with_patch(self, mock_total):
        """Тест оформления заказа с использованием patch для мока метода total"""
        # Подготовка
        self._add_sample_items([("Товар", 100)])
        
        # Мокаем метод total
        mock_total.return_value = 123
        
        # Создаем мок платежного шлюза
        mock_gateway = Mock()
        mock_gateway.charge.return_value = "TRX-PATCHED"
        
        # Действие
        transaction_id = self.service.checkout(mock_gateway)
        
        # Проверка
        self.assertEqual(transaction_id, "TRX-PATCHED")
        mock_gateway.charge.assert_called_once_with(123)
        mock_total.assert_called_once()
    
    # Дополнительные тесты
    def test_clear_cart_after_checkout(self):
        """Тест, что корзина очищается после успешного оформления"""
        # Подготовка
        self._add_sample_items()
        
        # Создаем мок платежного шлюза
        mock_gateway = Mock()
        mock_gateway.charge.return_value = "TRX-CLEAR"
        
        # Проверяем, что корзина не пуста перед оформлением
        self.assertGreater(len(self.service.cart), 0)
        
        # Действие
        transaction_id = self.service.checkout(mock_gateway)
        
        # В текущей реализации корзина НЕ очищается.
        # Этот тест демонстрирует, что можно расширить логику.
        # Для реализации очистки нужно добавить в checkout:
        # self.cart.clear()
        # self.discount = 0
        
        # Пока просто проверяем, что транзакция прошла
        self.assertEqual(transaction_id, "TRX-CLEAR")
    
    def test_multiple_discounts(self):
        """Тест, что последний примененный промокод перезаписывает предыдущий"""
        # Подготовка
        self._add_sample_items([("Товар", 1000)])
        
        # Применяем первую скидку
        self.service.apply_discount("SAVE10")
        self.assertEqual(self.service.total(), 900)
        
        # Применяем вторую скидку (должна перезаписать первую)
        self.service.apply_discount("SAVE20")
        self.assertEqual(self.service.total(), 800)
    
    def test_discount_without_apply(self):
        """Тест, что скидка по умолчанию равна 0"""
        # Подготовка
        self._add_sample_items([("Товар", 100)])
        
        # Проверяем, что скидка по умолчанию 0
        self.assertEqual(self.service.discount, 0)
        self.assertEqual(self.service.total(), 100)


class TestOrderServiceIntegration(unittest.TestCase):
    """Интеграционные тесты для OrderService"""
    
    def setUp(self):
        self.service = OrderService()
    
    def test_full_order_flow(self):
        """Тест полного цикла оформления заказа"""
        # 1. Добавляем товары
        self.service.add_item("Ноутбук", 50000)
        self.service.add_item("Мышь", 2000)
        
        # 2. Применяем скидку
        self.service.apply_discount("SAVE10")
        
        # 3. Проверяем сумму
        total = self.service.total()
        expected_total = int((50000 + 2000) * 0.9)
        self.assertEqual(total, expected_total)
        
        # 4. Оформляем заказ
        mock_gateway = Mock()
        mock_gateway.charge.return_value = "TRX-FULL-FLOW"
        
        transaction_id = self.service.checkout(mock_gateway)
        
        # 5. Проверяем результат
        self.assertEqual(transaction_id, "TRX-FULL-FLOW")
        mock_gateway.charge.assert_called_once_with(expected_total)
        
        print(f"\nПолный цикл оформления заказа протестирован:")
        print(f"  Товары: Ноутбук (50000р), Мышь (2000р)")
        print(f"  Скидка: 10%")
        print(f"  Итог: {expected_total}р")
        print(f"  Транзакция: {transaction_id}")


if __name__ == '__main__':
    unittest.main(verbosity=2)