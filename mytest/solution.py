def analyze_temperature(temperatures):

    if not temperatures or len(temperatures) != 7:
        return None

    avg_temp = round(sum(temperatures) / len(temperatures), 1)
    return {
        "average": avg_temp,
        "max": max(temperatures),
        "min": min(temperatures),
        "hot_days": sum(1 for t in temperatures if t > 25),
        "cold_days": sum(1 for t in temperatures if t < 10),
    }


if __name__ == "__main__":
    temps = [22, 28, 15, 8, 30, 18, 25]
    print(analyze_temperature(temps))
