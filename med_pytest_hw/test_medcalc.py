import pytest
from medcalc import bmi, bp_category, has_major_interaction, dose_mg

# --- 1. Тесты для BMI ---

def test_bmi_normal():
    """Тест обычного случая расчета BMI"""
    assert bmi(70, 1.75) == 22.86

def test_bmi_rounding():
    """Тест округления до 2 знаков"""
    assert bmi(70, 1.73) == 23.39

@pytest.mark.parametrize("weight, height", [
    (0, 1.8),    
    (-10, 1.8),  
    (70, 0),     
    (70, -0.5)   
])
def test_bmi_errors(weight, height):
    """Параметризованный тест для некорректных входов"""
    with pytest.raises(ValueError):
        bmi(weight, height)


# --- 2. Тесты для BP Category ---

@pytest.mark.parametrize("systolic, diastolic, expected", [
    (110, 70, "normal"),
    (119, 79, "normal"),

    (120, 70, "elevated"),
    (129, 79, "elevated"),

    (130, 75, "stage1"),      
    (139, 70, "stage1"),      
    (115, 80, "stage1"),      
    (115, 89, "stage1"),      
    
    (140, 85, "stage2"),      
    (120, 90, "stage2"),      
    (160, 100, "stage2"),
    
    (180, 90, "crisis"),     
    (140, 120, "crisis"),    
    (200, 130, "crisis")
])
def test_bp_category_levels(systolic, diastolic, expected):
    """Параметризованный тест по всем категориям и границам"""
    assert bp_category(systolic, diastolic) == expected

def test_bp_low_error():
    """Тест на подозрительно низкие значения"""
    with pytest.raises(ValueError):
        bp_category(60, 80) 
    with pytest.raises(ValueError):
        bp_category(120, 30) 


# --- 3. Тесты для Interaction (с фикстурой) ---

@pytest.fixture
def safe_drugs():
    """Фикстура: список базовых безопасных препаратов"""
    return ["Paracetamol", "Vitamin C"]

def test_interaction_none(safe_drugs):
    """Нет взаимодействий для безопасного списка"""
    assert has_major_interaction(safe_drugs) is False

def test_interaction_detected(safe_drugs):
    """Обнаружение опасной пары (warfarin + ibuprofen)"""
    drugs = safe_drugs + ["Warfarin", "Ibuprofen"]
    assert has_major_interaction(drugs) is True

def test_interaction_normalization():
    """Тест на регистр и пробелы"""
    drugs = [" nitrate ", "SILDENAFIL"]
    assert has_major_interaction(drugs) is True

def test_interaction_order_independence():
    """Тест независимости от порядка"""
    assert has_major_interaction(["ibuprofen", "warfarin"]) is True
    assert has_major_interaction(["warfarin", "ibuprofen"]) is True

def test_interaction_empty_list():
    """Пустой список не должен ломать код"""
    assert has_major_interaction([]) is False

def test_interaction_empty_string_error(safe_drugs):
    """Ошибка при пустой строке в списке"""
    with pytest.raises(ValueError):
        has_major_interaction(safe_drugs + ["   "])


# --- 4. Тесты для Dose MG ---

def test_dose_normal():
    """Обычный расчет: 10кг * 5мг = 50мг (макс 100)"""
    assert dose_mg(10, 5, 100) == 50.0

def test_dose_max_limit():
    """Тест ограничения max_mg: 10кг * 20мг = 200, но макс 100"""
    assert dose_mg(10, 20, 100) == 100.0

def test_dose_rounding():
    """Округление до 1 знака"""
    assert dose_mg(5.55, 1, 100) == 5.6 or dose_mg(5.55, 1, 100) == 5.5

def test_dose_errors():
    """Ошибка при отрицательных входах"""
    with pytest.raises(ValueError):
        dose_mg(-10, 5, 100)
    with pytest.raises(ValueError):
        dose_mg(10, 0, 100)
