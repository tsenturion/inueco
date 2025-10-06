def analyze_purchases(items, prices, discount_threshold=1000):
    if not items or not prices or len(items) != len(prices) or any(p < 0 for p in prices):
        return None
    total = sum(prices)
    average = round(total / len(prices), 2)
    most_expensive = items[prices.index(max(prices))]
    discount_applied = total >= discount_threshold
    final_total = round(total * 0.9, 2) if discount_applied else round(total, 2)
    return {
        "total": total,
        "average": average,
        "most_expensive": most_expensive,
        "discount_applied": discount_applied,
        "final_total": final_total
    }


if __name__ == "__main__":
    items = ["Хлеб", "Молоко", "Яйца", "Сыр"]
    prices = [50, 80, 120, 350]
    print(analyze_purchases(items, prices))
