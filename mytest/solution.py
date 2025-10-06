def analyze_temperature(temperatures: list):
    if len(temperatures) < 1 or len(temperatures) != 7:
        return None
    hot_days = 0
    cold_days = 0
    for current_day in temperatures:
        if current_day > 25:
            hot_days += 1
        elif current_day < 10:
            cold_days += 1
    return {
        "average": round(sum(temperatures) / len(temperatures), 1), 
        "max": max(temperatures), 
        "min": min(temperatures), 
        "hot_days": hot_days, 
        "cold_days": cold_days
        }