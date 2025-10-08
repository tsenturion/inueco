def analyze_temperature(temperature):

    if not temperature or len(temperature) != 7:
        return None
    
    avg_temp = round(sum(temperature) / len(temperature), 1)
    max_temp = max(temperature)
    min_temp = min(temperature)
    hot_days = sum(1 for temp in temperature if temp > 25)
    cold_days = sum(1 for temp in temperature if temp < 10)
    
    return {
        "average": avg_temp,
        "max": max_temp,
        "min": min_temp,
        "hot_days": hot_days,
        "cold_days": cold_days
    }

temperature = [20, 30, 31, 19, 11, 0, -11]
result = analyze_temperature(temperature)
print(result)

temperatures = [15, 16, 17]
result = analyze_temperature(temperatures)
print(result)
