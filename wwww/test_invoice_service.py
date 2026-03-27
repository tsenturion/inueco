
import unittest
from unittest.mock import Mock, call
from invoice_service import InvoiceService, Invoice, ChargeResult


class TestInvoiceService(unittest.TestCase):
    
    def setUp(self):
        """Создаем моки и сервис перед каждым тестом"""
        self.invoice_repo = Mock()
        self.payment_gateway = Mock()
        self.service = InvoiceService(self.invoice_repo, self.payment_gateway)
    
    def test_successful_payment(self):
        """Тест успешной оплаты"""
        # Arrange
        invoice = Invoice(id=1, customer_id="cust_123", amount=1000, status="pending")
        self.invoice_repo.get_by_id.return_value = invoice
        self.payment_gateway.charge.return_value = ChargeResult(
            ok=True, 
            transaction_id="tx_789"
        )
        
        # Act
        result = self.service.pay(invoice_id=1)
        
        # Assert
        self.assertEqual(result, "paid")
        
        # Проверяем вызовы
        self.invoice_repo.get_by_id.assert_called_once_with(1)
        self.payment_gateway.charge.assert_called_once_with("cust_123", 1000)
        self.invoice_repo.mark_paid.assert_called_once_with(1, "tx_789")
        
        # Проверяем, что другие методы не вызывались
        self.invoice_repo.mark_failed.assert_not_called()
        self.invoice_repo.mark_retry.assert_not_called()
    
    def test_payment_declined(self):
        """Тест отклоненного платежа"""
        # Arrange
        invoice = Invoice(id=2, customer_id="cust_456", amount=500, status="pending")
        self.invoice_repo.get_by_id.return_value = invoice
        self.payment_gateway.charge.return_value = ChargeResult(
            ok=False,
            reason="insufficient_funds"
        )
        
        # Act
        result = self.service.pay(invoice_id=2)
        
        # Assert
        self.assertEqual(result, "failed")
        
        # Проверяем вызовы
        self.invoice_repo.get_by_id.assert_called_once_with(2)
        self.payment_gateway.charge.assert_called_once_with("cust_456", 500)
        self.invoice_repo.mark_failed.assert_called_once_with(2, "insufficient_funds")
        
        # Проверяем, что другие методы не вызывались
        self.invoice_repo.mark_paid.assert_not_called()
        self.invoice_repo.mark_retry.assert_not_called()
    
    def test_already_paid_invoice(self):
        """Тест уже оплаченного счета"""
        # Arrange
        invoice = Invoice(id=3, customer_id="cust_789", amount=2000, status="paid")
        self.invoice_repo.get_by_id.return_value = invoice
        
        # Act
        result = self.service.pay(invoice_id=3)
        
        # Assert
        self.assertEqual(result, "already_paid")
        
        # Проверяем, что платежный шлюз НЕ вызывался
        self.invoice_repo.get_by_id.assert_called_once_with(3)
        self.payment_gateway.charge.assert_not_called()
        self.invoice_repo.mark_paid.assert_not_called()
        self.invoice_repo.mark_failed.assert_not_called()
        self.invoice_repo.mark_retry.assert_not_called()
    
    def test_invoice_not_found(self):
        """Тест: счет не найден"""
        # Arrange
        self.invoice_repo.get_by_id.return_value = None
        
        # Act & Assert
        with self.assertRaises(LookupError) as context:
            self.service.pay(invoice_id=999)
        
        self.assertEqual(str(context.exception), "invoice not found: 999")
        
        # Проверяем, что другие методы не вызывались
        self.invoice_repo.get_by_id.assert_called_once_with(999)
        self.payment_gateway.charge.assert_not_called()
        self.invoice_repo.mark_paid.assert_not_called()
        self.invoice_repo.mark_failed.assert_not_called()
        self.invoice_repo.mark_retry.assert_not_called()
    
    def test_invalid_amount_zero(self):
        """Тест: сумма счета равна 0"""
        # Arrange
        invoice = Invoice(id=4, customer_id="cust_101", amount=0, status="pending")
        self.invoice_repo.get_by_id.return_value = invoice
        
        # Act & Assert
        with self.assertRaises(ValueError) as context:
            self.service.pay(invoice_id=4)
        
        self.assertEqual(str(context.exception), "amount must be positive, got: 0")
        
        # Проверяем, что платежный шлюз НЕ вызывался
        self.invoice_repo.get_by_id.assert_called_once_with(4)
        self.payment_gateway.charge.assert_not_called()
    
    def test_invalid_amount_negative(self):
        """Тест: отрицательная сумма счета"""
        # Arrange
        invoice = Invoice(id=5, customer_id="cust_102", amount=-100, status="pending")
        self.invoice_repo.get_by_id.return_value = invoice
        
        # Act & Assert
        with self.assertRaises(ValueError) as context:
            self.service.pay(invoice_id=5)
        
        self.assertEqual(str(context.exception), "amount must be positive, got: -100")
        
        # Проверяем, что платежный шлюз НЕ вызывался
        self.invoice_repo.get_by_id.assert_called_once_with(5)
        self.payment_gateway.charge.assert_not_called()
    
    def test_payment_timeout(self):
        """Тест: таймаут платежного шлюза"""
        # Arrange
        invoice = Invoice(id=6, customer_id="cust_103", amount=1500, status="pending")
        self.invoice_repo.get_by_id.return_value = invoice
        self.payment_gateway.charge.side_effect = TimeoutError("gateway timeout")
        
        # Act
        result = self.service.pay(invoice_id=6)
        
        # Assert
        self.assertEqual(result, "retry")
        
        # Проверяем вызовы
        self.invoice_repo.get_by_id.assert_called_once_with(6)
        self.payment_gateway.charge.assert_called_once_with("cust_103", 1500)
        self.invoice_repo.mark_retry.assert_called_once_with(6)
        
        # Проверяем, что другие методы не вызывались
        self.invoice_repo.mark_paid.assert_not_called()
        self.invoice_repo.mark_failed.assert_not_called()
    
    def test_payment_timeout_then_success(self):
        """Тест: сложный сценарий с таймаутом и успехом (демонстрация side_effect как последовательности)"""
        # Arrange
        invoice = Invoice(id=7, customer_id="cust_104", amount=2000, status="pending")
        self.invoice_repo.get_by_id.return_value = invoice
        
        # Первый вызов - таймаут, второй - успех
        self.payment_gateway.charge.side_effect = [
            TimeoutError("gateway timeout"),  # первый вызов
            ChargeResult(ok=True, transaction_id="tx_777")  # второй вызов
        ]
        
        # Создаем новый сервис с теми же моками (или используем тот же)
        service = InvoiceService(self.invoice_repo, self.payment_gateway)
        
        # Первая попытка - таймаут
        result1 = service.pay(invoice_id=7)
        self.assertEqual(result1, "retry")
        
        # Вторая попытка - успех
        result2 = service.pay(invoice_id=7)
        self.assertEqual(result2, "paid")
        
        # Проверяем последовательность вызовов
        self.assertEqual(self.payment_gateway.charge.call_count, 2)
        self.payment_gateway.charge.assert_has_calls([
            call("cust_104", 2000),
            call("cust_104", 2000)
        ])
        
        self.invoice_repo.mark_retry.assert_called_once_with(7)
        self.invoice_repo.mark_paid.assert_called_once_with(7, "tx_777")


if __name__ == "__main__":
    unittest.main()