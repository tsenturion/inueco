def analyze_purchases(items, prices, discount_threshold=1000):
    if len(items) != len(prices) or len(items) == 0:
        return None
    
    if any(price < 0 for price in prices):
        return None
    
    total = sum(prices)
    average = round(total / len(prices), 2)
    
    max_price = max(prices)
    max_index = prices.index(max_price)
    most_expensive = items[max_index]
    
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

    result = analyze_purchases(items, prices)
    print(result)