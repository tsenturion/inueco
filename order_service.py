class InvalidItemError(Exception):
    """Исключение при невалидном товаре"""
    pass


class EmptyCartError(Exception):
    """Исключение при работе с пустой корзиной"""
    pass


class PaymentError(Exception):
    """Исключение при ошибке оплаты"""
    pass


class OrderService:
    def __init__(self):
        self._items = []
        self._discount = 0

    def add_item(self, name: str, price: int) -> None:
        """Добавление товара в корзину"""
        if not isinstance(name, str) or not name.strip():
            raise InvalidItemError("Имя товара не может быть пустым")
        
        if not isinstance(price, int):
            raise InvalidItemError("Цена должна быть целым числом")
        
        if price <= 0:
            raise InvalidItemError("Цена должна быть положительным числом")
        
        self._items.append({"name": name.strip(), "price": price})

    def apply_discount(self, code: str) -> None:
        """Применение промокода"""
        if not self._items:
            raise EmptyCartError("Невозможно применить скидку к пустой корзине")
        
        discounts = {
            "SAVE10": 0.1,
            "SAVE20": 0.2
        }
        
        if code not in discounts:
            raise ValueError(f"Неизвестный промокод: {code}")
        
        self._discount = discounts[code]

    def total(self) -> int:
        """Расчет итоговой стоимости"""
        if not self._items:
            return 0
        
        sum_price = sum(item["price"] for item in self._items)
        discount_amount = sum_price * self._discount
        return int(sum_price - discount_amount)  # Округление вниз

    def checkout(self, payment_gateway) -> str:
        """Оформление заказа"""
        if not self._items:
            raise EmptyCartError("Невозможно оформить пустой заказ")
        
        amount = self.total()
        
        try:
            transaction_id = payment_gateway.charge(amount)
            return transaction_id
        except Exception as e:
            raise PaymentError(f"Ошибка оплаты: {str(e)}")