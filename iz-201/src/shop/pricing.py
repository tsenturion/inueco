def final_price_cents(
    base_cents: int, discount_percent: int = 0, tax_percent: int = 20
) -> int:
    """
    Контракт:
    - base_cents: int, >= 0
    - discount_percent: int, 0..100
    - tax_percent: int, 0..100
    """

    # --- TYPE CHECK ---
    for name, value in {
        "base_cents": base_cents,
        "discount_percent": discount_percent,
        "tax_percent": tax_percent,
    }.items():
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError(f"{name} must be int")

    # --- RANGE CHECK ---
    if base_cents < 0:
        raise ValueError("base_cents must be >= 0")

    if not (0 <= discount_percent <= 100):
        raise ValueError("discount_percent out of range")

    if not (0 <= tax_percent <= 100):
        raise ValueError("tax_percent out of range")

    # --- LOGIC ---
    discounted = base_cents * (100 - discount_percent) / 100
    taxed = discounted * (100 + tax_percent) / 100

    return int(round(taxed))