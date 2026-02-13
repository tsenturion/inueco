def main():
    print("Hello from mytest!")


if __name__ == "__main__":
    main()

def analyze_temperature(temperatures):
    # Проверка на пустой список или неправильное количество дней
    if not temperatures or len(temperatures) != 7:
        return None
    
    # Расчет статистики
    average = round(sum(temperatures) / len(temperatures), 1)
    max_temp = max(temperatures)
    min_temp = min(temperatures)
    
    # Подсчет горячих и холодных дней
    hot_days = sum(1 for temp in temperatures if temp > 25)
    cold_days = sum(1 for temp in temperatures if temp < 10)
    
    # Возврат словаря с результатами
    return {
        "average": average,
        "max": max_temp,
        "min": min_temp,
        "hot_days": hot_days,
        "cold_days": cold_days
    }


# Примеры использования
if __name__ == "__main__":
    # Пример 1
    temperatures1 = [22, 28, 15, 8, 30, 18, 25]
    result1 = analyze_temperature(temperatures1)
    print("Пример 1:")
    print(result1)
    
    # Пример 2
    temperatures2 = [15, 16, 17]
    result2 = analyze_temperature(temperatures2)
    print("\nПример 2:")
    print(result2)
    
    # Дополнительные примеры
    print("\nДополнительные примеры:")
    
    # Все дни горячие
    hot_week = [26, 27, 28, 29, 30, 31, 32]
    print("Горячая неделя:", analyze_temperature(hot_week))
    
    # Все дни холодные
    cold_week = [5, 6, 7, 8, 9, 8, 7]
    print("Холодная неделя:", analyze_temperature(cold_week))
    
    # Пустой список
    empty_list = []
    print("Пустой список:", analyze_temperature(empty_list))