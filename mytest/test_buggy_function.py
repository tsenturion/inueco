import pytest
from buggy_function import process_student_scores

def test_normal_case():
    """Тест с обычными корректными данными - должен пройти успешно"""
    students_data = [
        {"name": "Иван", "scores": [85, 90, 78], "age": 20},
        {"name": "Мария", "scores": [95, 90, 92], "age": 19},
    ]

    result = process_student_scores(students_data)

    assert result["total_students"] == 2
    assert result["average_score"] == 88.33
    assert result["top_student"] == "Мария"
    assert result["failed_students"] == []
    assert result["adults_count"] == 2


def test_empty_list():
    """Тест с пустым списком студентов - должен пройти успешно"""
    result = process_student_scores([])
    assert result is None


def test_student_without_scores():
    """ТЕСТ НА ОШИБКУ 1: деление на ноль при пустом списке оценок у студента"""
    students_data = [
        {"name": "Иван", "scores": [], "age": 20}
    ]

    # Должен упасть с ZeroDivisionError
    result = process_student_scores(students_data)


def test_failed_students_criteria():
    """ТЕСТ НА ОШИБКУ 2: неправильное условие для неуспевающих (<= 60 вместо < 60)"""
    students_data = [
        {"name": "Студент1", "scores": [60, 60, 60], "age": 20},  # средний = 60 (не должен быть неуспевающим)
    ]

    result = process_student_scores(students_data)

    # Студент со средним 60 не должен быть в списке неуспевающих
    assert result["failed_students"] == []


def test_adults_count_criteria():
    """ТЕСТ НА ОШИБКУ 3: неправильное условие для совершеннолетних (> 18 вместо >= 18)"""
    students_data = [
        {"name": "Студент1", "scores": [80, 80, 80], "age": 18},  # совершеннолетний
    ]

    result = process_student_scores(students_data)

    # 18-летний студент должен считаться совершеннолетним
    assert result["adults_count"] == 1


def test_empty_scores_in_all_students():
    """ТЕСТ НА ОШИБКУ 4: деление на ноль при расчете общего среднего балла"""
    students_data = [
        {"name": "Студент1", "scores": [], "age": 20},
        {"name": "Студент2", "scores": [], "age": 21},
    ]

    # Должен упасть с ZeroDivisionError при расчете общего среднего
    result = process_student_scores(students_data)


def test_single_student_success():
    """Тест с одним студентом - должен пройти успешно"""
    students_data = [
        {"name": "Анна", "scores": [95, 85, 90], "age": 19}
    ]

    result = process_student_scores(students_data)

    assert result["total_students"] == 1
    assert result["average_score"] == 90.0
    assert result["top_student"] == "Анна"
    assert result["failed_students"] == []
    assert result["adults_count"] == 1


def test_top_student_determination():
    """Тест с проверкой определения лучшего студента - должен пройти успешно"""
    students_data = [
        {"name": "Студент1", "scores": [70, 70, 70], "age": 20},
        {"name": "Студент2", "scores": [90, 90, 90], "age": 21},
        {"name": "Студент3", "scores": [80, 80, 80], "age": 22},
    ]

    result = process_student_scores(students_data)

    assert result["top_student"] == "Студент2"
    assert result["average_score"] == 80.0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])