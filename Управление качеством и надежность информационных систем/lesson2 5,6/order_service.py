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
    def add_item(self, name: str, price: int):
        if not name or not name.strip():
            raise InvalidItemError("Name Error")   
        if not isinstance(price, int) or price <= 0:
            raise InvalidItemError('Price Error')
        self.items.append({"name": name, "price": price })
        
    def apply_discount(self, code: str) -> None:
        if not self.items:
            raise EmptyCartError("Empty cart")

        if code == "SAVE10":
            self.discount = 0.10
        elif code == "SAVE20":
            self.discount = 0.20       
        else:
            raise ValueError("Wrong discount code")

    def total(self) -> int:
        total_price = sum(item["price"] for item in self.items)
        final_price = total_price * (1 - self.discount)
        return int(final_price)

    def checkout(self, payment_gateway) -> str:
        if not self.items:
            raise EmptyCartError("Cart is empty")
        
        amount_to_pay = self.total()

        try:
            transaction_id = payment_gateway.charge(amount_to_pay)
            return transaction_id
        except Exception as e:
            raise PaymentError(f"Payment going bad: {e}")
