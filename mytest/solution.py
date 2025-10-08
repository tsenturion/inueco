def analyze_temperature(temperatures):
    """
    Анализирует температурные данные за неделю.
    
    Args:
        temperatures: список температур за 7 дней
        
    Returns:
        Словарь с результатами анализа или None, если данные некорректны
    """
    # Проверяем корректность входных данных
    if not temperatures or len(temperatures) != 7:
        return None
    
    # Вычисляем среднюю температуру
    total = 0
    for temp in temperatures:
        total += temp
    average = round(total / len(temperatures), 1)
    
    # Находим максимум и минимум
    max_temp = temperatures[0]
    min_temp = temperatures[0]
    
    for temp in temperatures:
        if temp > max_temp:
            max_temp = temp
        if temp < min_temp:
            min_temp = temp
    
    # Подсчитываем жаркие и холодные дни
    hot_days = 0
    cold_days = 0
    
    for temp in temperatures:
        if temp > 25:
            hot_days += 1
        if temp < 10:
            cold_days += 1
    
    # Формируем результат
    result = {
        "average": average,
        "max": max_temp,
        "min": min_temp,
        "hot_days": hot_days,
        "cold_days": cold_days
    }
    
    return result


# Примеры использования
if __name__ == "__main__":
    # Пример 1: Нормальные данные
    temps1 = [22, 28, 15, 8, 30, 18, 25]
    print("Пример 1:")
    print(analyze_temperature(temps1))
    print()
    
    # Пример 2: Недостаточно данных
    temps2 = [15, 16, 17]
    print("Пример 2:")
    print(analyze_temperature(temps2))
    print()
    
    # Пример 3: Все дни жаркие
    temps3 = [26, 27, 28, 29, 30, 31, 32]
    print("Пример 3:")
    print(analyze_temperature(temps3))
    print()
    
    # Пример 4: Все дни холодные
    temps4 = [5, 6, 3, 2, 8, 9, 4]
    print("Пример 4:")
    print(analyze_temperature(temps4))