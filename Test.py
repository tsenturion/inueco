def test_add_item_invalid_price(self):
        """Проверка валидации цены (отрицательная, 0, неверный тип)."""
        # Цена <= 0
        with self.assertRaises(InvalidItemError):
            self.service.add_item("Item", 0)
        with self.assertRaises(InvalidItemError):
            self.service.add_item("Item", -10)
            
        # Цена не int
        with self.assertRaises(InvalidItemError):
            self.service.add_item("Item", 10.5)  # Float
        with self.assertRaises(InvalidItemError):
            self.service.add_item("Item", "100") # String

    def test_apply_discount_valid(self):
        """Проверка применения корректных промокодов."""
        self.service.add_item("Phone", 100)
        
        self.service.apply_discount("SAVE10")
        self.assertEqual(self.service.discount, 0.10)
        
        self.service.apply_discount("SAVE20")
        self.assertEqual(self.service.discount, 0.20)

    def test_apply_discount_invalid_code(self):
        """Проверка ошибки при неизвестном промокоде."""
        self.service.add_item("Phone", 100)
        with self.assertRaises(ValueError):
            self.service.apply_discount("UNKNOWN")

    def test_apply_discount_empty_cart(self):
        """Проверка ошибки при попытке скидки на пустую корзину."""
        with self.assertRaises(EmptyCartError):
            self.service.apply_discount("SAVE10")

    def test_total_calculation_parametrized(self):
        """
        Параметризованный тест через subTest.
        Проверяет расчет стоимости в разных сценариях.
        """
        scenarios = [
            # items (list of tuples), discount_code, expected_total
            ([("A", 100)], None, 100),                # Без скидки
            ([("A", 100)], "SAVE10", 90),             # 100 - 10% = 90
            ([("A", 99)], "SAVE10", 89),              # 99 - 9.9 = 89.1 -> int(89)
            ([("A", 50), ("B", 70)], "SAVE20", 96),   # 120 - 20% = 96
        ]

        for items_data, code, expected in scenarios:
            with self.subTest(items=items_data, code=code):
                # Подготовка (Clean state via setUp is not enough inside loop logic, 
                # so we recreate or clean manually if needed, but here we use a fresh setup logic)
                # Лучше создать новый сервис внутри subTest или очистить текущий
                self.service = OrderService() 
                
                for name, price in items_data:
                    self.service.add_item(name, price)
                
                if code:
                    self.service.apply_discount(code)
                
                self.assertEqual(self.service.total(), expected)

    def test_checkout_success(self):
        """
        Тест успешной оплаты с использованием Mock.
        Проверяем, что checkout вызывает charge и возвращает результат.
        """
        self.service.add_item("Book", 100)
        
        # Создаем мок платежного шлюза
        payment_gateway = Mock()
        # Настраиваем успешный ответ метода charge
        payment_gateway.charge.return_value = "TXN_12345"
        
        result = self.service.checkout(payment_gateway)
        
        # Проверки
        self.assertEqual(result, "TXN_12345")
        # Убеждаемся, что charge вызвали ровно 1 раз с суммой 100
        payment_gateway.charge.assert_called_once_with(100)

    def test_checkout_payment_failed(self):
        """
        Тест провала оплаты (gateway выбрасывает ошибку).
        """
        self.service.add_item("Book", 100)
        
        payment_gateway = Mock()
        # Настраиваем side_effect, чтобы имитировать выброс исключения
        payment_gateway.charge.side_effect = Exception("Connection Timeout")
        
        # Проверяем, что checkout ловит Exception и выбрасывает PaymentError
        with self.assertRaises(PaymentError):
            self.service.checkout(payment_gateway)

    def test_checkout_empty_cart(self):
        """Проверка checkout с пустой корзиной (не доходит до шлюза)."""
        payment_gateway = Mock()
        with self.assertRaises(EmptyCartError):
            self.service.checkout(payment_gateway)
        
        # Убеждаемся, что шлюз НЕ вызывался
        payment_gateway.charge.assert_not_called()

if __name__ == "__main__":
    unittest.main()
Как запустить и проверить
Сохраните оба файла (order_service.py и test_order_service.py) в одной папке.

Откройте терминал в этой папке.

Запустите тесты с подробным выводом:

Bash

python -m unittest -v
Ожидаемый результат: Вы должны увидеть список тестов со статусом ... OK и итоговое сообщение OK.

Plaintext

test_add_item_invalid_name (test_order_service.TestOrderService) ... ok
test_add_item_invalid_price (test_order_service.TestOrderService) ... ok
test_add_item_valid (test_order_service.TestOrderService) ... ok
test_apply_discount_empty_cart (test_order_service.TestOrderService) ... ok
test_apply_discount_invalid_code (test_order_service.TestOrderService) ... ok
test_apply_discount_valid (test_order_service.TestOrderService) ... ok
test_checkout_empty_cart (test_order_service.TestOrderService) ... ok
test_checkout_payment_failed (test_order_service.TestOrderService) ... ok
test_checkout_success (test_order_service.TestOrderService) ... ok
test_total_calculation_parametrized (test_order_service.TestOrderService) ... ok

----------------------------------------------------------------------
Ran 10 tests in 0.002s

OK
Хотите, я покажу, как переписать эти тесты с использованием фреймворка pytest, который часто используется в современной коммерческой разработке вместо unittest?
