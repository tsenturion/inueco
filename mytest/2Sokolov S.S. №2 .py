def test_analyze_purchases():
    """Тесты для функции analyze_purchases"""
    
    # Тест 1: обычная покупка без скидки
    items = ["Хлеб", "Молоко", "Яйца", "Сыр"]
    prices = [50, 80, 120, 350]
    result = analyze_purchases(items, prices)
    
    assert result["total"] == 600
    assert result["average"] == 150.0
    assert result["most_expensive"] == "Сыр"
    assert result["discount_applied"] == False
    assert result["final_total"] == 600.0
    
    # Тест 2: покупка со скидкой
    items = ["Ноутбук", "Мышка", "Клавиатура"]
    prices = [50000, 1500, 3500]
    result = analyze_purchases(items, prices, 10000)
    
    assert result["total"] == 55000
    assert result["average"] == 18333.33
    assert result["most_expensive"] == "Ноутбук"
    assert result["discount_applied"] == True
    assert result["final_total"] == 49500.0
    
    # Тест 3: пустые списки
    assert analyze_purchases([], []) is None
    assert analyze_purchases([], [100]) is None
    assert analyze_purchases(["Товар"], []) is None
    
    # Тест 4: разная длина списков
    assert analyze_purchases(["A", "B"], [100]) is None
    assert analyze_purchases(["A"], [100, 200]) is None
    
    # Тест 5: отрицательные цены
    assert analyze_purchases(["Товар"], [-100]) is None
    assert analyze_purchases(["A", "B"], [100, -50]) is None
    
    # Тест 6: один товар
    result = analyze_purchases(["Книга"], [500])
    assert result["total"] == 500
    assert result["average"] == 500.0
    assert result["most_expensive"] == "Книга"
    assert result["discount_applied"] == False
    
    # Тест 7: граничный случай - сумма равна порогу
    result = analyze_purchases(["Товар"], [1000], 1000)
    assert result["discount_applied"] == True
    assert result["final_total"] == 900.0
    
    # Тест 8: граничный случай - сумма чуть ниже порога
    result = analyze_purchases(["Товар"], [999], 1000)
    assert result["discount_applied"] == False
    assert result["final_total"] == 999.0
    
    # Тест 9: одинаковые цены
    items = ["Товар1", "Товар2", "Товар3"]
    prices = [100, 100, 100]
    result = analyze_purchases(items, prices)
    assert result["total"] == 300
    assert result["average"] == 100.0
    assert result["most_expensive"] in items  # любой из товаров
    
    # Тест 10: округление до 2 знаков
    items = ["Товар1", "Товар2"]
    prices = [33, 34]
    result = analyze_purchases(items, prices)
    assert result["average"] == 33.5
    assert result["final_total"] == 67.0
    
    print("Все тесты пройдены!")

# Запуск тестов
if __name__ == "__main__":
    test_analyze_purchases()