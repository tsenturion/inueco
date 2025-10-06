def analyze_purchases(items: list[str], prices: list[int], discount_threshold=1000):
    if len(items) < 1: 
        return None
    if len(items) != len(prices) or discount_threshold <= 0 or min(prices) < 0:
        return None
    applied = 0
    if discount_threshold <= sum(prices):
        applied = 10 
    return {
        "total": sum(prices),
        "average": round(sum(prices) / len(prices), 2),
        "most_expensive": items[prices.index(max(prices))],
        "discount_applied": bool(applied),
        "final_total": round(sum(prices) * (1 - applied * 0.01), 2)
    }
    