# order_service.py

class InvalidItemError(Exception):
    """Исключение при невалидных данных товара"""
    pass


class EmptyCartError(Exception):
    """Исключение при попытке операций с пустой корзиной"""
    pass


class PaymentError(Exception):
    """Исключение при ошибке платежа"""
    pass


class OrderService:
    """Сервис оформления заказа"""
    
    def __init__(self):
        self.cart = []  # Список товаров в формате (name, price)
        self.discount = 0  # Скидка в процентах (0-100)
    
    def add_item(self, name: str, price: int) -> None:
        """
        Добавляет товар в корзину
        
        Args:
            name: Название товара (не пустое после удаления пробелов)
            price: Цена товара (целое число > 0)
            
        Raises:
            InvalidItemError: если name пустой или price некорректный
        """
        # Проверяем name
        if not name or not name.strip():
            raise InvalidItemError("Название товара не может быть пустым")
        
        # Проверяем price
        if not isinstance(price, int):
            raise InvalidItemError("Цена должна быть целым числом")
        
        if price <= 0:
            raise InvalidItemError("Цена должна быть больше 0")
        
        # Добавляем товар в корзину
        self.cart.append((name.strip(), price))
    
    def apply_discount(self, code: str) -> None:
        """
        Применяет промокод
        
        Args:
            code: Код промокода
            
        Raises:
            EmptyCartError: если корзина пуста
            ValueError: если промокод неизвестен
        """
        if not self.cart:
            raise EmptyCartError("Невозможно применить промокод к пустой корзине")
        
        # Поддерживаемые промокоды
        discounts = {
            "SAVE10": 10,
            "SAVE20": 20,
        }
        
        if code not in discounts:
            raise ValueError(f"Неизвестный промокод: {code}")
        
        self.discount = discounts[code]
    
    def total(self) -> int:
        """
        Возвращает итоговую стоимость заказа
        
        Returns:
            Итоговая стоимость (целое число, округленное вниз после скидки)
        """
        # Суммируем цены всех товаров
        subtotal = sum(price for _, price in self.cart)
        
        # Применяем скидку
        if self.discount > 0:
            discount_amount = subtotal * self.discount / 100
            total_with_discount = subtotal - discount_amount
        else:
            total_with_discount = subtotal
        
        # Округляем вниз до целого числа
        return int(total_with_discount)
    
    def checkout(self, payment_gateway) -> str:
        """
        Оформляет заказ через платежный шлюз
        
        Args:
            payment_gateway: Платежный шлюз с методом charge(amount)
            
        Returns:
            ID транзакции
            
        Raises:
            EmptyCartError: если корзина пуста
            PaymentError: если платеж не прошел
        """
        if not self.cart:
            raise EmptyCartError("Невозможно оформить пустой заказ")
        
        # Получаем итоговую сумму
        amount = self.total()
        
        try:
            # Пытаемся выполнить платеж
            transaction_id = payment_gateway.charge(amount)
            return transaction_id
        except Exception as e:
            # Любое исключение от платежного шлюза превращаем в PaymentError
            raise PaymentError(f"Ошибка платежа: {e}")