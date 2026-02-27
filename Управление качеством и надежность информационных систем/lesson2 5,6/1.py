def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Недостаточно средств")
    return balance - amount


def test_withdraw_error(self):
    try:
        withdraw(100, 200)
    except ValueError:
        pass


def test_withdraw_error(self):
    self.assertRaises(ValueError, withdraw, 100, 200)


def test_withdraw_error(self):
    with self.assertRaises(ValueError):
        withdraw(100, 200)


def test_withdraw_error_message(self):
    with self.assertRaises(ValueError) as context:
        withdraw(100, 200)

    self.assertEqual(str(context.exception), "Недостаточно средств")


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Деление на ноль")
    if not isinstance(a, (int, float)):
        raise TypeError("Некорректный тип данных")
    return a / b


def test_divide_by_zero(self):
    with self.assertRaises(ZeroDivisionError):
        divide(10, 0)

def test_divide_wrong_type(self):
    with self.assertRaises(TypeError):
        divide("10", 2)


def test_divide_ok(self):
    result = divide(10, 2)
    self.assertEqual(result, 5)


with self.assertRaises(Exception):
    divide(10, 0)
