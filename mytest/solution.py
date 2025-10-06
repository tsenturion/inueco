def analyze_temperature(c: float) -> str:
    if c < 0:
        return "freezing"
    elif c < 20:
        return "cold"
    else:
        return "warm"

if __name__ == "__main__":
    print(analyze_temperature(10))
