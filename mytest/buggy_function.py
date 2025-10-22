# test_buggy_function.py
import pytest

def process_student_scores(students_data):
    """
    Обрабатывает данные об оценках студентов и возвращает статистику.
    
    Args:
        students_data: список словарей с данными студентов
                      [{"name": str, "scores": [int], "age": int}, ...]
    
    Returns:
        dict со статистикой:
        {
            "total_students": int,
            "average_score": float,
            "top_student": str,
            "failed_students": list,
            "adults_count": int
        }
    """
    if not students_data:
        return None
    
    total_students = len(students_data)
    all_scores = []
    student_averages = {}
    failed_students = []
    adults_count = 0
    
    # Собираем все оценки и вычисляем средние для каждого студента
    for student in students_data:
        name = student["name"]
        scores = student["scores"]
        age = student["age"]
        
        # ОШИБКА 1: деление на ноль при пустом списке оценок
        student_avg = sum(scores) / len(scores)
        student_averages[name] = student_avg
        
        all_scores.extend(scores)
        
        # ОШИБКА 2: неправильное условие для неуспевающих (должно быть < 60)
        if student_avg <= 60:
            failed_students.append(name)
        
        # ОШИБКА 3: неправильное условие для совершеннолетних (должно быть >= 18)
        if age > 18:
            adults_count += 1
    
    # ОШИБКА 4: не обрабатывается случай, когда all_scores пустой
    average_score = sum(all_scores) / len(all_scores)
    
    # Находим лучшего студента
    top_student = max(student_averages, key=student_averages.get)
    
    return {
        "total_students": total_students,
        "average_score": round(average_score, 2),
        "top_student": top_student,
        "failed_students": failed_students,
        "adults_count": adults_count
    }


# Тест 1: Обычные корректные данные
def test_normal_data():
    data = [
        {"name": "Иван", "scores": [85, 90, 78], "age": 20},
        {"name": "Мария", "scores": [55, 60, 50], "age": 18},
        {"name": "Петр", "scores": [90, 95, 92], "age": 17}
    ]
    
    result = process_student_scores(data)
    
    assert result["total_students"] == 3
    assert result["average_score"] == 77.22
    assert result["top_student"] == "Петр"
    assert "Мария" in result["failed_students"]
    assert result["adults_count"] == 2


# Тест 2: Пустой список студентов
def test_empty_list():
    result = process_student_scores([])
    assert result is None


# Тест 3: Студент без оценок (пустой список scores)
def test_student_without_scores():
    data = [
        {"name": "Анна", "scores": [], "age": 19}
    ]
    
    # Этот тест должен выявить ошибку деления на ноль
    try:
        result = process_student_scores(data)
        # Если не произошло исключение, тест должен провалиться
        assert False, "Ожидалось исключение ZeroDivisionError"
    except ZeroDivisionError:
        assert True


# Тест 4: Один студент
def test_single_student():
    data = [
        {"name": "Ольга", "scores": [80, 85, 90], "age": 22}
    ]
    
    result = process_student_scores(data)
    
    assert result["total_students"] == 1
    assert result["average_score"] == 85.0
    assert result["top_student"] == "Ольга"
    assert result["failed_students"] == []
    assert result["adults_count"] == 1


# Тест 5: Проверка подсчета неуспевающих студентов
def test_failed_students():
    data = [
        {"name": "Студент1", "scores": [59, 59, 59], "age": 20},  # средний = 59 (< 60)
        {"name": "Студент2", "scores": [60, 60, 60], "age": 19}   # средний = 60 (>= 60)
    ]
    
    result = process_student_scores(data)
    
    # ОШИБКА: функция считает студента с баллом 60 неуспевающим
    # Правильно: только "Студент1" должен быть в списке неуспевающих
    assert "Студент1" in result["failed_students"]
    # Этот assert должен провалиться из-за ошибки в функции
    assert "Студент2" not in result["failed_students"]


# Тест 6: Проверка подсчета совершеннолетних
def test_adults_count():
    data = [
        {"name": "Студент1", "scores": [70, 70, 70], "age": 17},  # несовершеннолетний
        {"name": "Студент2", "scores": [70, 70, 70], "age": 18},  # совершеннолетний
        {"name": "Студент3", "scores": [70, 70, 70], "age": 19}   # совершеннолетний
    ]
    
    result = process_student_scores(data)
    
    # ОШИБКА: функция считает только тех, кто старше 18 лет
    # Правильно: должно быть 2 совершеннолетних (возраст >= 18)
    assert result["adults_count"] == 2


# Тест 7: Проверка определения лучшего студента
def test_top_student():
    data = [
        {"name": "Студент1", "scores": [80, 80, 80], "age": 20},  # средний = 80
        {"name": "Студент2", "scores": [90, 90, 90], "age": 21},  # средний = 90
        {"name": "Студент3", "scores": [85, 85, 85], "age": 22}   # средний = 85
    ]
    
    result = process_student_scores(data)
    
    assert result["top_student"] == "Студент2"


# Тест 8: Все студенты без оценок (проверка ошибки 4)
def test_all_students_without_scores():
    data = [
        {"name": "Студент1", "scores": [], "age": 20},
        {"name": "Студент2", "scores": [], "age": 21}
    ]
    
    # Этот тест должен выявить только ошибку деления на ноль (ошибка 1)
    # Ошибка 4 не будет выявлена, так как выполнение прервется на ошибке 1
    try:
        result = process_student_scores(data)
        assert False, "Ожидалось исключение ZeroDivisionError"
    except ZeroDivisionError:
        assert True


# Тест 9: Студенты с нулевыми оценками (для проверки ошибки 4)
def test_students_with_zero_scores():
    data = [
        {"name": "Студент1", "scores": [0, 0, 0], "age": 20},
        {"name": "Студент2", "scores": [0, 0, 0], "age": 21}
    ]
    
    # Этот тест проходит без ошибок, так как списки оценок не пустые
    # Ошибка 4 не проявляется в этом сценарии
    result = process_student_scores(data)
    
    assert result["total_students"] == 2
    assert result["average_score"] == 0.0
    assert result["failed_students"] == ["Студент1", "Студент2"]
    assert result["adults_count"] == 2


if __name__ == "__main__":
    pytest.main([__file__, "-v"])