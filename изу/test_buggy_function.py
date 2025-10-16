def test_normal_case():
    """Тест с обычными корректными данными"""
    students_data = [
        {"name": "Иван", "scores": [85, 90, 78], "age": 20},
        {"name": "Мария", "scores": [55, 60, 50], "age": 18},
        {"name": "Петр", "scores": [90, 95, 92], "age": 17},
        {"name": "Анна", "scores": [40, 45, 35], "age": 19}
    ]
    
    result = process_student_scores(students_data)
    
    assert result["total_students"] == 4
    assert result["average_score"] == 67.08
    assert result["top_student"] == "Петр"
    assert "Мария" in result["failed_students"]
    assert "Анна" in result["failed_students"]
    assert result["adults_count"] == 3


def test_empty_list():
    """Тест с пустым списком студентов"""
    students_data = []
    
    result = process_student_scores(students_data)
    
    assert result is None


def test_student_without_scores():
    """Тест со студентом без оценок"""
    students_data = [
        {"name": "Иван", "scores": [85, 90, 78], "age": 20},
        {"name": "Мария", "scores": [], "age": 18},
        {"name": "Петр", "scores": [90, 95], "age": 17}
    ]
    
    result = process_student_scores(students_data)
    
    assert result["total_students"] == 3
    assert "Мария" in result["failed_students"]


def test_single_student():
    """Тест с одним студентом"""
    students_data = [
        {"name": "Ольга", "scores": [75, 80, 85], "age": 21}
    ]
    
    result = process_student_scores(students_data)
    
    assert result["total_students"] == 1
    assert result["average_score"] == 80.0
    assert result["top_student"] == "Ольга"
    assert result["failed_students"] == []
    assert result["adults_count"] == 1


def test_failed_students_count():
    """Тест с проверкой подсчета неуспевающих студентов"""
    students_data = [
        {"name": "Студент1", "scores": [59, 59, 59], "age": 20},  # средний = 59
        {"name": "Студент2", "scores": [60, 60, 60], "age": 19},  # средний = 60
        {"name": "Студент3", "scores": [30, 40, 50], "age": 18},  # средний = 40
        {"name": "Студент4", "scores": [0, 0, 0], "age": 17}      # средний = 0
    ]
    
    result = process_student_scores(students_data)
    
    failed_students = result["failed_students"]
    assert len(failed_students) == 3
    assert "Студент1" in failed_students
    assert "Студент3" in failed_students
    assert "Студент4" in failed_students
    assert "Студент2" not in failed_students


def test_adults_count():
    """Тест с проверкой подсчета совершеннолетних"""
    students_data = [
        {"name": "Студент1", "scores": [80, 85, 90], "age": 17},  # несовершеннолетний
        {"name": "Студент2", "scores": [70, 75, 80], "age": 18},  # совершеннолетний
        {"name": "Студент3", "scores": [60, 65, 70], "age": 19},  # совершеннолетний
        {"name": "Студент4", "scores": [50, 55, 60], "age": 16}   # несовершеннолетний
    ]
    
    result = process_student_scores(students_data)
    
    assert result["adults_count"] == 2


def test_top_student_determination():
    """Тест с проверкой определения лучшего студента"""
    students_data = [
        {"name": "Студент1", "scores": [80, 85, 90], "age": 20},  # средний = 85
        {"name": "Студент2", "scores": [95, 90, 100], "age": 19}, # средний = 95
        {"name": "Студент3", "scores": [90, 95, 85], "age": 18},  # средний = 90
        {"name": "Студент4", "scores": [100, 100, 100], "age": 17} # средний = 100
    ]
    
    result = process_student_scores(students_data)
    
    assert result["top_student"] == "Студент4"


def process_student_scores(students_data):
    """
    РЕАЛИЗАЦИЯ ФУНКЦИИ ДЛЯ ТЕСТИРОВАНИЯ
    """
    if not students_data:
        return None
    
    total_students = len(students_data)
    total_score = 0
    best_student = None
    best_avg = -1
    failed_students = []
    adults_count = 0
    
    for student in students_data:
        # Подсчет среднего балла
        if student["scores"]:
            avg_score = sum(student["scores"]) / len(student["scores"])
        else:
            avg_score = 0
        
        total_score += avg_score
        
        # Определение лучшего студента
        if avg_score > best_avg:
            best_avg = avg_score
            best_student = student["name"]
        
        # Определение неуспевающих
        if avg_score < 60:
            failed_students.append(student["name"])
        
        # Подсчет совершеннолетних
        if student["age"] >= 18:
            adults_count += 1
    
    average_score = round(total_score / total_students, 2)
    
    return {
        "total_students": total_students,
        "average_score": average_score,
        "top_student": best_student,
        "failed_students": failed_students,
        "adults_count": adults_count
    }


# Запуск тестов
if __name__ == "__main__":
    # Запускаем все тесты
    test_functions = [
        test_empty_list,
        test_single_student,
        test_student_without_scores,
        test_failed_students_count,
        test_adults_count,
        test_top_student_determination,
        test_normal_case
    ]
    
    for test_func in test_functions:
        try:
            test_func()
            print(f"✓ {test_func.__name__} прошел успешно")
        except AssertionError as e:
            print(f"✗ {test_func.__name__} не прошел: {e}")
        except Exception as e:
            print(f"✗ {test_func.__name__} вызвал ошибку: {e}")
    
    print("\nТестирование завершено!")