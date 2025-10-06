def analyze_purchases(items, prices, discount_threshold=1000):
    if len(prices) != len(items) or len(items) < 0 or len(prices) < 0 or int(prices) < 0:
        return None

    total_sum = round(sum(prices))
    average_p = round(sum(prices) / len(prices), 1)
    max_p = max(prices)
    if total_sum > discount_threshold:
        discount_applied = True

    if discount_applied == True:
        total_with_discount = round(sum(prices / 10))

    return {
        "total": total_sum,
        "average": average_p,
        "most_expensive": max_p,
        "disciybt_applied": discount_applied,
        "final_total": total_with_discount
    }

items = ["Хлеб", "Молоко", "Яйца", "Сыр"]
prices = [50, 80, 120, 350]
result = analyze_purchases(items, prices)

print(result)