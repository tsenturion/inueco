import pytest
from solution2 import analyze_purchases


class TestAnalyzePurchases:
    """Тесты для функции analyze_purchases"""
    
    def test_basic_purchase_without_discount(self):
        """Тест обычной покупки без скидки"""
        items = ["Хлеб", "Молоко", "Яйца", "Сыр"]
        prices = [50, 80, 120, 350]
        
        result = analyze_purchases(items, prices)
        
        assert result is not None
        assert result["total"] == 600
        assert result["average"] == 150.0
        assert result["most_expensive"] == "Сыр"
        assert result["discount_applied"] is False
        assert result["final_total"] == 600.0
    
    def test_purchase_with_discount(self):
        """Тест покупки со скидкой"""
        items = ["Ноутбук", "Мышка", "Клавиатура"]
        prices = [50000, 1500, 3500]
        
        result = analyze_purchases(items, prices, 10000)
        
        assert result is not None
        assert result["total"] == 55000
        assert result["average"] == 18333.33
        assert result["most_expensive"] == "Ноутбук"
        assert result["discount_applied"] is True
        assert result["final_total"] == 49500.0
    
    def test_exact_threshold(self):
        """Тест когда сумма равна порогу скидки"""
        items = ["Товар1", "Товар2"]
        prices = [600, 400]
        
        result = analyze_purchases(items, prices, 1000)
        
        assert result["total"] == 1000
        assert result["discount_applied"] is True
        assert result["final_total"] == 900.0
    
    def test_single_item(self):
        """Тест с одним товаром"""
        items = ["Телефон"]
        prices = [25000]
        
        result = analyze_purchases(items, prices, 20000)
        
        assert result is not None
        assert result["total"] == 25000
        assert result["average"] == 25000.0
        assert result["most_expensive"] == "Телефон"
        assert result["discount_applied"] is True
        assert result["final_total"] == 22500.0
    
    def test_empty_lists(self):
        """Тест с пустыми списками"""
        assert analyze_purchases([], []) is None
        assert analyze_purchases(["Товар"], []) is None
        assert analyze_purchases([], [100]) is None
    
    def test_different_length_lists(self):
        """Тест с разной длиной списков"""
        items = ["Товар1", "Товар2", "Товар3"]
        prices = [100, 200]
        
        assert analyze_purchases(items, prices) is None
    
    def test_negative_prices(self):
        """Тест с отрицательными ценами"""
        items = ["Товар1", "Товар2"]
        prices = [100, -50]
        
        assert analyze_purchases(items, prices) is None
    
    def test_zero_price(self):
        """Тест с нулевой ценой (валидно)"""
        items = ["Товар1", "Подарок"]
        prices = [500, 0]
        
        result = analyze_purchases(items, prices)
        
        assert result is not None
        assert result["total"] == 500
        assert result["average"] == 250.0
    
    def test_multiple_items_same_price(self):
        """Тест когда несколько товаров с одинаковой максимальной ценой"""
        items = ["Товар1", "Товар2", "Товар3"]
        prices = [300, 300, 100]
        
        result = analyze_purchases(items, prices)
        
        assert result is not None
        assert result["most_expensive"] in ["Товар1", "Товар2"]
        assert result["total"] == 700
    
    def test_custom_discount_threshold(self):
        """Тест с пользовательским порогом скидки"""
        items = ["Товар1", "Товар2"]
        prices = [300, 200]
        
        result = analyze_purchases(items, prices, 400)
        
        assert result["total"] == 500
        assert result["discount_applied"] is True
        assert result["final_total"] == 450.0
    
    def test_large_numbers(self):
        """Тест с большими числами"""
        items = ["Машина", "Квартира"]
        prices = [2000000, 8000000]
        
        result = analyze_purchases(items, prices, 1000000)
        
        assert result is not None
        assert result["total"] == 10000000
        assert result["discount_applied"] is True
        assert result["final_total"] == 9000000.0
    
    def test_rounding_average(self):
        """Тест правильности округления средней цены"""
        items = ["Товар1", "Товар2", "Товар3"]
        prices = [100, 100, 101]
        
        result = analyze_purchases(items, prices)
        
        assert result["average"] == 100.33


if __name__ == "__main__":
    pytest.main([__file__, "-v"])