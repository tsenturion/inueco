from typing import List, Optional, Dict, Any

def analyze_purchases(
    items: List[str],
    prices: List[float],
    discount_threshold: float = 1000
) -> Optional[Dict[str, Any]]:
    
    if not items or not prices or len(items) != len(prices):
        return None
    if any(p < 0 for p in prices):
        return None

    total = sum(prices)
    n = len(prices)
    average = round(total / n, 2)
    max_idx = max(range(n), key=lambda i: prices[i])
    most_expensive = items[max_idx]

    discount_applied = total >= discount_threshold
    final_total = round(total * (0.9 if discount_applied else 1.0), 2)

    return {
        "total": total,
        "average": average,
        "most_expensive": most_expensive,
        "discount_applied": discount_applied,
        "final_total": final_total,
    }

items = ["Хлеб", "Молоко", "Яйца", "Сыр"]
prices = [50, 80, 120, 350]
print(analyze_purchases(items, prices))

items = ["Ноутбук", "Мышка", "Клавиатура"]
prices = [50000, 1500, 3500]
print(analyze_purchases(items, prices, 10000))

