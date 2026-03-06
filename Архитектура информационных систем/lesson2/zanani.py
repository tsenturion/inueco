def analyze_purchases(items, prices, discount_threshold=1000):
    # Проверка, что списки одинаковые по длине и не пустые
    if len(items) != len(prices) or len(items) == 0:
        return None

    # Проверка на отрицательные цены
    for price in prices:
        if price < 0:
            return None

    total = sum(prices)  # сумма цен
    average = round(total / len(prices), 2)  # средняя цена

    # Самый дорогой товар
    max_price = max(prices)
    index = prices.index(max_price)
    most_expensive = items[index]

    # Проверка на скидку
    discount_applied = total >= discount_threshold

    # Итоговая сумма после скидки (если применима)
    final_total = round(total * 0.9, 2) if discount_applied else round(total, 2)

    # Возвращаем все данные
    return {
        "total": round(total, 2),
        "average": average,
        "most_expensive": most_expensive,
        "discount_applied": discount_applied,
        "final_total": final_total
    }