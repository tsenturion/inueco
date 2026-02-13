def bmi(weight_kg: float, height_m: float) -> float:
    """
    BMI = weight / height^2. Округлить до 2 знаков.
    Правила:
    - weight_kg и height_m должны быть > 0, иначе ValueError
    """
    if weight_kg <= 0 or height_m <= 0:
        raise ValueError("Weight and height must be greater than 0")
    
    result = weight_kg / (height_m ** 2)
    return round(result, 2)


def bp_category(systolic: int, diastolic: int) -> str:
    """
    Возвращает одну из категорий:
    'normal', 'elevated', 'stage1', 'stage2', 'crisis'
    """
    if systolic < 70 or diastolic < 40:
        raise ValueError("Blood pressure values are suspiciously low")

    if systolic >= 180 or diastolic >= 120:
        return 'crisis'
    
    if systolic >= 140 or diastolic >= 90:
        return 'stage2'
    
    if (130 <= systolic <= 139) or (80 <= diastolic <= 89):
        return 'stage1'
    
    if (120 <= systolic <= 129) and (diastolic < 80):
        return 'elevated'
    
    return 'normal'


def has_major_interaction(drugs: list[str]) -> bool:
    """
    True если есть противопоказанная комбинация.
    Правила:
    - Нормализовать названия: strip(), lower()
    - Если встречаются пустые строки после strip() -> ValueError
    """
    if not drugs:
        return False

    normalized_drugs = set()
    for drug in drugs:
        cleaned_drug = drug.strip().lower()
        if not cleaned_drug:
            raise ValueError("Drug list contains empty strings")
        normalized_drugs.add(cleaned_drug)

    dangerous_pairs = [
        {"warfarin", "ibuprofen"},
        {"nitrate", "sildenafil"},
        {"ssri", "mao inhibitor"}
    ]

    for pair in dangerous_pairs:
        if pair.issubset(normalized_drugs):
            return True

    return False


def dose_mg(weight_kg: float, mg_per_kg: float, max_mg: float) -> float:
    """
    Доза = weight_kg * mg_per_kg, но не выше max_mg. 
    Округлить до 1 знака.
    Правила:
    - все входы должны быть > 0, иначе ValueError
    """
    if weight_kg <= 0 or mg_per_kg <= 0 or max_mg <= 0:
        raise ValueError("All inputs must be greater than 0")

    calculated_dose = weight_kg * mg_per_kg
    result = min(calculated_dose, max_mg)
    
    return round(result, 1)
