import pytest
import sys
import os

# src для импорта
sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))

from buggy_function_fixed import process_student_scores


def test_normal_case():
    """Тест с обычными корректными данными"""
    students_data = [
        {"name": "Иван", "scores": [85, 90, 78], "age": 20},
        {"name": "Мария", "scores": [55, 60, 50], "age": 18},
        {"name": "Петр", "scores": [90, 95, 92], "age": 17}
    ]
    
    result = process_student_scores(students_data)
    
    assert result["total_students"] == 3
    assert result["average_score"] == 77.22
    assert result["top_student"] == "Петр"
    assert result["failed_students"] == ["Мария"]
    assert result["adults_count"] == 2


def test_empty_students_list():
    """Тест с пустым списком студентов"""
    result = process_student_scores([])
    assert result is None


def test_student_without_scores():
    """Тест со студентом без оценок (пустой список scores)"""
    students_data = [
        {"name": "Анна", "scores": [], "age": 19}
    ]
    result = process_student_scores(students_data)
    
    assert result["total_students"] == 1
    assert result["average_score"] == 0
    assert result["failed_students"] == ["Анна"]  # Средний балл 0 < 60
    assert result["adults_count"] == 1


def test_single_student():
    """Тест с одним студентом"""
    students_data = [
        {"name": "Ольга", "scores": [70, 80, 90], "age": 21}
    ]
    
    result = process_student_scores(students_data)
    
    assert result["total_students"] == 1
    assert result["average_score"] == 80.0
    assert result["top_student"] == "Ольга"
    assert result["failed_students"] == []
    assert result["adults_count"] == 1


def test_failed_students_calculation():
    """Тест с проверкой подсчета неуспевающих студентов"""
    students_data = [
        {"name": "Студент1", "scores": [59, 59, 59], "age": 20},  # средний = 59 (< 60)
        {"name": "Студент2", "scores": [60, 60, 60], "age": 19},  # средний = 60 (>= 60)
        {"name": "Студент3", "scores": [50, 55, 45], "age": 18}   # средний = 50 (< 60)
    ]
    
    result = process_student_scores(students_data)
    
   
    assert "Студент1" in result["failed_students"]
    assert "Студент2" not in result["failed_students"]  
    assert "Студент3" in result["failed_students"]
    assert len(result["failed_students"]) == 2  # Только два неуспевающих студента


def test_adults_count_calculation():
    """Тест с проверкой подсчета совершеннолетних"""
    students_data = [
        {"name": "Студент17", "scores": [80, 85], "age": 17},  # несовершеннолетний
        {"name": "Студент18", "scores": [75, 80], "age": 18},  # совершеннолетний
        {"name": "Студент19", "scores": [70, 75], "age": 19}   # совершеннолетний
    ]
    
    result = process_student_scores(students_data)
    
    assert result["adults_count"] == 2  # Оба студента (18 и 19 лет)


def test_top_student_determination():
    """Тест с проверкой определения лучшего студента"""
    students_data = [
        {"name": "Средний", "scores": [70, 70, 70], "age": 20},
        {"name": "Лучший", "scores": [95, 100, 90], "age": 19},
        {"name": "Худший", "scores": [50, 55, 45], "age": 18}
    ]
    
    result = process_student_scores(students_data)
    
    assert result["top_student"] == "Лучший"
    assert result["average_score"] == 71.67  # ИСПРАВЛЕНО: правильный расчет!


def test_all_students_failed():
    """Тест, когда все студенты неуспевающие"""
    students_data = [
        {"name": "С1", "scores": [50, 55, 45], "age": 20},
        {"name": "С2", "scores": [40, 35, 30], "age": 19},
        {"name": "С3", "scores": [55, 50, 45], "age": 18}
    ]
    
    result = process_student_scores(students_data)
    
    # Все студенты должны быть в списке неуспевающих
    assert len(result["failed_students"]) == 3
    assert result["average_score"] == 45.0


def test_edge_case_60_score():
    """Тест с пограничным значением 60 баллов"""
    students_data = [
        {"name": "Пограничный", "scores": [60, 60, 60], "age": 20}  # средний = 60
    ]
    
    result = process_student_scores(students_data)
    
    assert result["failed_students"] == []  


def test_edge_case_18_years():
    """Тест с пограничным возрастом 18 лет"""
    students_data = [
        {"name": "18лет", "scores": [80, 85], "age": 18}
    ]
    
    result = process_student_scores(students_data)
    assert result["adults_count"] == 1  


def test_all_students_no_scores():
    """Тест, когда у всех студентов нет оценок"""
    students_data = [
        {"name": "С1", "scores": [], "age": 20},
        {"name": "С2", "scores": [], "age": 19}
    ]
    
    result = process_student_scores(students_data)
    
    assert result["total_students"] == 2
    assert result["average_score"] == 0
    assert result["failed_students"] == ["С1", "С2"]  # Средний балл 0 < 60
    assert result["adults_count"] == 2