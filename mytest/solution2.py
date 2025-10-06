def analyze_purchases(items: list[str], prices: list[float], discount_threshold: float = 1000) -> dict[str, str | float] | None:
    if len(items) != len(prices) or not items or not prices or any(price < 0 for price in prices):
        return None

    discount = 10 # 10%
    total_cost = sum(prices)
    final_total = total_cost * (1 - discount / 100) if total_cost >= discount_threshold else total_cost
    
    return {
        "total": total_cost,
        "average": round(total_cost / len(prices), 2),
        "most_expensive": items[prices.index(max(prices))],
        "discount_applied": total_cost >= discount_threshold,
        "final_total": round(final_total, 2)
    }

# if __name__ == "__main__":
