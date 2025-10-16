import pytest
from process_student_scores import process_student_scores

def test_currect_data():
     ### - Тест с обычными корректными данными
    students_data = [
        {"name": "Иван", "scores": [85, 90, 78], "age": 20},
        {"name": "Мария", "scores": [55, 60, 50], "age": 19}
    ]
    result = process_student_scores(students_data)

    date = { 
    "total_students": 2,
    "average_score": 69.67,
    "top_student": "Иван",
    "failed_students": ["Мария"],
    "adults_count": 2
    }
    assert result == date

def test_empty_student():

    """Тест с пустым списком студентов"""
    result = process_student_scores([])
    assert result is None


def test_empty_score():
    ### - Тест со студентом без оценок (пустой список scores)
    
    students_data = [{"name": "Иван", "scores": [], "age": 20}]
    result = process_student_scores(students_data)
    assert result is not None

def test_single_student():
    ####  - Тест с одним студентом
    students_data = [
    {"name": "Иван", "scores": [85,90,78], "age": 17},
    ]
    result = process_student_scores(students_data)
    assert result["total_students"] == 1
    assert result["average_score"] == 84.33
    assert result["top_student"] == "Иван"
    assert result["failed_students"] == []
    assert result["adults_count"] == 0

def test_adults_count():
    ### Тест с проверкой подсчета неуспевающих студентов (средний балл < 60)
    students_data = [
        {"name": "Иван", "scores": [59, 59, 59], "age": 20},
        {"name": "Мария", "scores": [60, 60, 60], "age": 19}
    ]

    result = process_student_scores(students_data)

    assert result["failed_students"] == ["Мария"]
    assert result["failed_students"] == ["Иван"]

def test_age():

    ### - Тест с проверкой подсчета совершеннолетних (возраст >= 18)
    students_data = [
        {"name": "Иван", "scores": [85, 90, 78], "age": 18},
        {"name": "Мария", "scores": [55, 60, 50], "age": 17}
    ]
    result = process_student_scores(students_data)
    assert result["adults_count"] == 1

def test_all_students_with_empty_scores():
    students = [
        {"name": "A", "scores": [], "age": 25},
        {"name": "B", "scores": [], "age": 21},
    ]
    res = process_student_scores(students)

    assert res["total_students"] == 2
    assert res["average_score"] == 0.00
    assert set(res["failed_students"]) == {"A", "B"}
    assert res["adults_count"] == 2
    assert res["top_student"] in {"A", "B", None, ""}

if __name__ == "__main__":
    pytest.main([__file__, "-v"])