import pytest

from buggy_test import process_student_scores


def test_normal_data_returns_expected():
    students = [
        {"name": "Иван", "scores": [85, 90, 78], "age": 20},
        {"name": "Мария", "scores": [55, 60, 50], "age": 18},
    ]
    res = process_student_scores(students)

    assert res["total_students"] == 2
    assert res["average_score"] == 69.67
    assert res["top_student"] == "Иван"
    assert res["failed_students"] == ["Мария"] 
    assert res["adults_count"] == 2        


def test_empty_students_returns_none():
    assert process_student_scores([]) is None


def test_student_with_no_scores_does_not_crash_and_is_failed():
    students = [
        {"name": "Пустой", "scores": [], "age": 19},
        {"name": "Анна", "scores": [70, 80], "age": 17},
    ]
    res = process_student_scores(students)

    assert res["total_students"] == 2
    assert res["top_student"] == "Анна"
    assert "Пустой" in res["failed_students"] 
    assert "Анна" not in res["failed_students"]
    assert res["average_score"] == 75.0      
    assert res["adults_count"] == 1      


def test_one_student_correct_stats():
    students = [
        {"name": "Adam", "scores": [100, 80], "age": 17},
    ]
    res = process_student_scores(students)

    assert res["total_students"] == 1
    assert res["average_score"] == 90.0
    assert res["top_student"] == "Adam"
    assert res["failed_students"] == []
    assert res["adults_count"] == 0


def test_failed_threshold_strictly_less_than_60():
    students = [
        {"name": "Грань", "scores": [60, 60, 60], "age": 30},  
        {"name": "Сильный", "scores": [90, 95], "age": 25},
    ]
    res = process_student_scores(students)

    assert "Грань" not in res["failed_students"]
    assert res["top_student"] == "Сильный"
    assert res["adults_count"] == 2


def test_adults_count_includes_18():
    students = [
        {"name": "Teen", "scores": [70], "age": 18},
        {"name": "Kid", "scores": [90], "age": 17},
    ]
    res = process_student_scores(students)

    assert res["adults_count"] == 1


def test_all_students_with_empty_scores_average_is_zero_and_no_crash():
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


def test_top_student_is_selected_by_highest_average():
    students = [
        {"name": "X", "scores": [70, 70, 70], "age": 19}, 
        {"name": "Y", "scores": [90, 50, 90], "age": 22}, 
        {"name": "Z", "scores": [80, 80], "age": 18},     
    ]
    res = process_student_scores(students)

    assert res["top_student"] == "Z"
    assert res["average_score"] == 75.0
