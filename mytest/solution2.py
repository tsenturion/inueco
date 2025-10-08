def analyze_purchases(items, prices, discount_threshold=1000):
    """
    Анализирует список покупок и возвращает статистику.
    
    Args:
        items: список названий товаров
        prices: список цен товаров
        discount_threshold: порог для применения скидки 10%
    
    Returns:
        Словарь со статистикой или None при ошибке валидации
    """
    # Проверка на пустые списки
    if not items or not prices:
        return None
    
    # Проверка на одинаковую длину списков
    if len(items) != len(prices):
        return None
    
    # Проверка на отрицательные цены
    for price in prices:
        if price < 0:
            return None
    
    # Вычисление общей суммы
    total = sum(prices)
    
    # Вычисление средней цены
    average = round(total / len(prices), 2)
    
    # Поиск самого дорогого товара
    max_price_index = 0
    for i in range(len(prices)):
        if prices[i] > prices[max_price_index]:
            max_price_index = i
    most_expensive = items[max_price_index]
    
    # Проверка применения скидки
    discount_applied = total >= discount_threshold
    
    # Вычисление итоговой суммы
    if discount_applied:
        final_total = round(total * 0.9, 2)
    else:
        final_total = round(total, 2)
    
    # Формирование результата
    result = {
        "total": total,
        "average": average,
        "most_expensive": most_expensive,
        "discount_applied": discount_applied,
        "final_total": final_total
    }
    
    return result


# Примеры использования
if __name__ == "__main__":
    # Пример 1: Обычная покупка без скидки
    items1 = ["Хлеб", "Молоко", "Яйца", "Сыр"]
    prices1 = [50, 80, 120, 350]
    print("Пример 1:", analyze_purchases(items1, prices1))
    
    # Пример 2: Крупная покупка со скидкой
    items2 = ["Ноутбук", "Мышка", "Клавиатура"]
    prices2 = [50000, 1500, 3500]
    print("Пример 2:", analyze_purchases(items2, prices2, 10000))
    
    # Пример 3: Ошибка - разная длина списков
    items3 = ["Товар1", "Товар2"]
    prices3 = [100]
    print("Пример 3 (ошибка):", analyze_purchases(items3, prices3))