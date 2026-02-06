class InvalidItemError(Exception):
    pass

class EmptyCartError(Exception):
    pass

class PaymentError(Exception):
    pass

class OrderService:
    def __init__(self):
        self.items = []
        self.discount = 0.0 

    def add_item(self, name: str, price: int) -> None:
        if not name or not name.strip():
            raise InvalidItemError("Имя товара не может быть пустым")
        
        if not isinstance(price, int) or price <= 0:
            raise InvalidItemError("Цена должна быть целым числом больше 0")
            
        self.items.append({"name": name, "price": price})

    def apply_discount(self, code: str) -> None:
        if not self.items:
            raise EmptyCartError("Нельзя применить скидку к пустой корзине")

        if code == "SAVE10":
            self.discount = 0.10
        elif code == "SAVE20":
            self.discount = 0.20
        else:
            raise ValueError(f"Неизвестный промокод: {code}")

    def total(self) -> int:
        raw_total = sum(item["price"] for item in self.items)
        final_total = raw_total * (1 - self.discount)
        return int(final_total)

    def checkout(self, payment_gateway) -> str:
        if not self.items:
            raise EmptyCartError("Корзина пуста, нельзя оформить заказ")

        amount = self.total()
        
        try:
            transaction_id = payment_gateway.charge(amount)
            return transaction_id
        except Exception as e:
            raise PaymentError(f"Ошибка оплаты: {e}")