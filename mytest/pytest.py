def analyze_temperature(temperatures):
    if not temperatures or len(temperatures) != 7:
        return None

    average = round(sum(temperatures) / len(temperatures), 1)
    max_temp = max(temperatures)
    min_temp = min(temperatures)
    hot_days = sum(1 for temp in temperatures if temp > 25)
    cold_days = sum(1 for temp in temperatures if temp <= 10)

    return {
        "average": average,
        "max": max_temp,
        "min": min_temp,
        "hot_days": hot_days,
        "cold_days": cold_days
    }


def analyze_purchases(items, prices, discount_threshold=1000):
    if not items or not prices:
        return None
    if len(items) != len(prices):
        return None
    if any(price < 0 for price in prices):
        return None

    total = sum(prices)
    average = round(total / len(prices), 2)
    
    max_price_index = prices.index(max(prices))
    most_expensive = items[max_price_index]
    
    discount_applied = total >= discount_threshold
    if discount_applied:
        final_total = round(total * 0.9, 2)
    else:
        final_total = total
    return {
        "total": total,
        "average": average,
        "most_expensive": most_expensive,
        "discount_applied": discount_applied,
        "final_total": final_total
    }
