def analyze_purchases(items, prices, discount_threshold=1000):
    if len(prices) != len(items) or len(items) <= 0 or len(prices) <= 0 or any(price < 0 for price in prices):
        return None

    total_sum = round(sum(prices))
    average_p = round(sum(prices) / len(prices), 2)

    max_price_index = prices.index(max(prices))
    most_expensive = items[max_price_index]

    discount_applied = total_sum >= discount_threshold

    if discount_applied:
        total_with_discount = round(total_sum * 0.9, 2)
    else:
        total_with_discount = round(total_sum, 2)

    return {
        "total": total_sum,
        "average": average_p,
        "most_expensive": most_expensive,
        "discount_applied": discount_applied,
        "final_total": total_with_discount
    }
items = ["Хлеб", "Молоко", "Яйца", "Сыр"]
prices = [50, 80, 120, 350]
result = analyze_purchases(items, prices)

print(result)

items = ["Ноутбук", "Мышка", "Клавиатура"]
prices = [50000, 1500, 3500]

result = analyze_purchases(items, prices, 10000)

print(result)