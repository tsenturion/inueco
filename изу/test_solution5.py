import pytest
from buggy_function import process_student_scores

def test_normal_valid_data():
    data = [
        {"name": "Иван", "scores": [85, 90, 78], "age": 20},
        {"name": "Мария", "scores": [55, 60, 50], "age": 19}
    ]
    result = process_student_scores(data)
    expected = {
        "total_students": 2,
        "average_score": 69.67,
        "top_student": "Иван",
        "failed_students": ["Мария"],  
        "adults_count": 2  
    }
    assert result == expected


def test_empty_student_list():
    assert process_student_scores([]) is None


def test_student_with_no_scores():
    data = [{"name": "Тест", "scores": [], "age": 20}]
    result = process_student_scores(data) 
    assert result is not None  

def test_single_student():
    data = [{"name": "Олег", "scores": [70], "age": 17}]
    result = process_student_scores(data)
    expected = {
        "total_students": 1,
        "average_score": 70.0,
        "top_student": "Олег",
        "failed_students": [], 
        "adults_count": 0  
    }
    assert result == expected


def test_failed_students_threshold():
    data = [
        {"name": "Студент1", "scores": [60], "age": 20},      
        {"name": "Студент2", "scores": [59], "age": 20},     
    ]
    result = process_student_scores(data)
    assert "Студент2" in result["failed_students"]
    assert "Студент1" not in result["failed_students"]  


def test_adults_count_threshold():
    data = [
        {"name": "Совершеннолетний", "scores": [80], "age": 18},
        {"name": "Несовершеннолетний", "scores": [80], "age": 17}
    ]
    result = process_student_scores(data)
    assert result["adults_count"] == 1  


def test_top_student_identification():
    data = [
        {"name": "Лучший", "scores": [100, 95], "age": 20},    
        {"name": "Хороший", "scores": [90, 92], "age": 19}      
    ]
    result = process_student_scores(data)
    assert result["top_student"] == "Лучший"


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
