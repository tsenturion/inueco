def analyze_temperature(temperatures: list[float]) -> dict[str, float] | None:
    if not temperatures or len(temperatures) != 7:
        return None
    
    average_temp = sum(temperatures) / len(temperatures)

    return {
        "average": round(average_temp, 1),
        "max": max(temperatures),
        "min": min(temperatures),
        "hot_days": sum(1 for temp in temperatures if temp > 25),
        "cold_days": sum(1 for temp in temperatures if temp < 10)
    }

# if __name__ == "__main__":
    