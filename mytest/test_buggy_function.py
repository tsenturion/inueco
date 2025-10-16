from buggy_function import process_student_scores 

def test_normal_valid_data():
    """Тест с обычными корректными данными."""
    data = [
        {"name": "Иван", "scores": [85, 90, 78], "age": 20},
        {"name": "Мария", "scores": [55, 60, 50], "age": 19}
    ]
    result = process_student_scores(data)
    expected = {
        "total_students": 2,
        "average_score": 69.67,
        "top_student": "Иван",
        "failed_students": ["Мария"],  # среднее Марии = 55.0 < 60
        "adults_count": 2  # оба >= 18
    }
    assert result == expected


def test_empty_student_list():
    """Тест с пустым списком студентов."""
    assert process_student_scores([]) is None


def test_student_with_no_scores():
    """Должна быть проверка на пустой список оценок."""
    data = [{"name": "Тест", "scores": [], "age": 20}]
    result = process_student_scores(data)  # ← упадёт, если проверки нет
    assert result is not None  

def test_single_student():
    """Тест с одним студентом."""
    data = [{"name": "Олег", "scores": [70], "age": 17}]
    result = process_student_scores(data)
    expected = {
        "total_students": 1,
        "average_score": 70.0,
        "top_student": "Олег",
        "failed_students": [],  # 70 >= 60 → не неуспевающий
        "adults_count": 0  # возраст 17 < 18
    }
    assert result == expected


def test_failed_students_threshold():
    """Тест проверки неуспевающих: средний балл < 60 (а не <= 60)."""
    data = [
        {"name": "Студент1", "scores": [60], "age": 20},      # среднее = 60 → должен НЕ быть в failed
        {"name": "Студент2", "scores": [59], "age": 20},      # среднее = 59 → должен быть в failed
    ]
    result = process_student_scores(data)
    # Из-за ошибки в коде (<= 60) оба попадут в failed, но по условию только Студент2
    # Этот тест покажет, что "Студент1" неправильно включён в failed_students
    assert "Студент2" in result["failed_students"]
    assert "Студент1" not in result["failed_students"]  # провалится → выявляет ОШИБКУ 2


def test_adults_count_threshold():
    """Тест подсчёта совершеннолетних: возраст >= 18 (а не > 18)."""
    data = [
        {"name": "Совершеннолетний", "scores": [80], "age": 18},
        {"name": "Несовершеннолетний", "scores": [80], "age": 17}
    ]
    result = process_student_scores(data)
    # В коде условие age > 18, поэтому 18-летний не засчитается → adults_count = 0 (ошибка)
    # Но по условию должно быть 1
    assert result["adults_count"] == 1  # провалится → выявляет ОШИБКУ 3


def test_top_student_identification():
    """Тест определения лучшего студента по среднему баллу."""
    data = [
        {"name": "Лучший", "scores": [100, 95], "age": 20},     # avg = 97.5
        {"name": "Хороший", "scores": [90, 92], "age": 19}      # avg = 91.0
    ]
    result = process_student_scores(data)
    assert result["top_student"] == "Лучший"


# Дополнительный тест: пустой all_scores (если все студенты без оценок)
def test_all_students_with_empty_scores():
    students = [
        {"name": "A", "scores": [], "age": 18},
        {"name": "B", "scores": [], "age": 20},
    ]
    res = process_student_scores(students)

    assert res["total_students"] == 2
    assert res["average_score"] == 0.00
    assert set(res["failed_students"]) == {"A", "B"}
    assert res["adults_count"] == 2
    assert res["top_student"] in {"A", "B", None, ""}
