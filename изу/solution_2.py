

def average(arg: float) ->float:
    get_round = sum(arg) / len(arg)
    return round(get_round, 2)

def most_expensive(arg_price, arg_items):
    max_index = prices.index(max(arg_price))
    return arg_items[max_index]

def final_total(total, discount_threshold):
    total = sum(prices)
    discount_price = total >= discount_threshold
    if(discount_price):
        total = round(total * 0.9, 2)
    else:
        total = round(total, 2)
    return total
def discount(arg, discount_threshold):
    if sum(arg) >= discount_threshold:
        return True
    else:
        return False
def analyze_purchases(items: str, 
                      prices: int, 
                      discount_threshold: int = 1000):
    
    if len(items) != len(prices):
        return None
    elif not items and prices:
        return None
    elif any(price < 0 for price in prices):
        return None
    else:
        total = sum(prices)

        return {
        "total": total,
        "average": average(prices),
        "most_expensive": most_expensive(prices, items),
        "discount_applied": discount(prices,discount_threshold),
        "final_total": final_total(total, discount_threshold)
    }


