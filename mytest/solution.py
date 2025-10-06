def analyze_temperature(temperatures):
    if not temperatures or len(temperatures) != 7:
        return None
    
    total = sum(temperatures)
    avg = round(total / 7, 1)
    max_temp = max(temperatures)
    min_temp = min(temperatures)
    hot_days = len([t for t in temperatures if t > 25])
    cold_days = len([t for t in temperatures if t < 10])
    
    return {
        "average": avg,
        "max": max_temp,
        "min": min_temp,
        "hot_days": hot_days,
        "cold_days": cold_days
    }

if __name__ == "__main__":
    temperatures = [22, 28, 15, 8, 30, 18, 25]
    result = analyze_temperature(temperatures)
    print(result)