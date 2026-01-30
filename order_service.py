class InvalidItemError(Exception):
    """Исключение при невалидном товаре"""
    pass


class EmptyCartError(Exception):
    """Исключение при пустой корзине"""
    pass


class PaymentError(Exception):
    """Исключение при ошибке оплаты"""
    pass


class OrderService:
    def __init__(self):
        self.items = []  # список кортежей (name, price)
        self.discount = 0  # скидка в процентах

    def add_item(self, name: str, price: int) -> None:
        """
        Добавляет товар в корзину
        
        Args:
            name: название товара (не пустое после strip())
            price: цена товара (целое число > 0)
        
        Raises:
            InvalidItemError: при невалидных данных
        """
        # Проверка name
        if not name or not isinstance(name, str) or not name.strip():
            raise InvalidItemError("Имя товара не может быть пустым")
        
        # Проверка price
        if not isinstance(price, int):
            raise InvalidItemError("Цена должна быть целым числом")
        
        if price <= 0:
            raise InvalidItemError("Цена должна быть больше 0")
        
        self.items.append((name.strip(), price))

    def apply_discount(self, code: str) -> None:
        """
        Применяет скидку по промокоду
        
        Args:
            code: промокод
        
        Raises:
            EmptyCartError: если корзина пуста
            ValueError: если промокод неизвестен
        """
        if not self.items:
            raise EmptyCartError("Невозможно применить скидку к пустой корзине")
        
        if code == "SAVE10":
            self.discount = 10
        elif code == "SAVE20":
            self.discount = 20
        else:
            raise ValueError(f"Неизвестный промокод: {code}")

    def total(self) -> int:
        """
        Рассчитывает итоговую стоимость с учётом скидки
        
        Returns:
            Итоговая стоимость (целое число, округление вниз)
        """
        subtotal = sum(price for _, price in self.items)
        
        if self.discount > 0:
            discount_amount = subtotal * self.discount / 100
            total_with_discount = subtotal - discount_amount
            return int(total_with_discount)  # округление вниз
        
        return subtotal

    def checkout(self, payment_gateway) -> str:
        """
        Оформляет заказ через платёжный шлюз
        
        Args:
            payment_gateway: объект платёжного шлюза с методом charge
        
        Returns:
            ID транзакции
        
        Raises:
            EmptyCartError: если корзина пуста
            PaymentError: при ошибке оплаты
        """
        if not self.items:
            raise EmptyCartError("Невозможно оформить пустую корзину")
        
        amount = self.total()
        
        try:
            transaction_id = payment_gateway.charge(amount)
            return transaction_id
        except Exception as e:
            raise PaymentError(f"Ошибка оплаты: {e}") from e