from test_buggy_function import process_student_scores

def test_happy_path_basic():
    students_data = [
        {"name": "Иван", "scores": [85, 90, 78], "age": 20},
        {"name": "Мария", "scores": [55, 60, 50], "age": 18},
    ]
    res = process_student_scores(students_data)
    assert res["total_students"] == 2
    assert res["average_score"] == 69.67
    assert res["top_student"] == "Иван"
    assert res["failed_students"] == ["Мария"]
    assert res["adults_count"] == 2

def test_empty_list_returns_none():
    assert process_student_scores([]) is None

def test_student_with_empty_scores_is_handled():
    students_data = [
        {"name": "Пустой", "scores": [], "age": 19},
        {"name": "Анна", "scores": [100], "age": 17},
    ]
    res = process_student_scores(students_data)
    assert res["total_students"] == 2
    assert res["average_score"] == 100.00
    assert res["top_student"] == "Анна"
    assert res["failed_students"] == ["Пустой"]
    assert res["adults_count"] == 1

def test_one_student_case():
    students_data = [{"name": "Solo", "scores": [70, 80], "age": 18}]
    res = process_student_scores(students_data)
    assert res["total_students"] == 1
    assert res["average_score"] == 75.00
    assert res["top_student"] == "Solo"
    assert res["failed_students"] == []
    assert res["adults_count"] == 1

def test_failed_threshold_is_strictly_less_than_60():
    students_data = [
        {"name": "Ровно60", "scores": [60, 60], "age": 18},
        {"name": "Ниже60", "scores": [40, 50], "age": 18},
    ]
    res = process_student_scores(students_data)
    assert res["failed_students"] == ["Ниже60"]

def test_adults_count_includes_18():
    students_data = [
        {"name": "Мал", "scores": [70], "age": 17},
        {"name": "Грань", "scores": [70], "age": 18},
        {"name": "Взрослый", "scores": [70], "age": 19},
    ]
    res = process_student_scores(students_data)
    assert res["adults_count"] == 2

def test_top_student_detected_correctly():
    students_data = [
        {"name": "Strong", "scores": [100, 90, 100], "age": 20},
        {"name": "Middle", "scores": [88, 90, 80], "age": 20},
        {"name": "Lower", "scores": [60, 70, 65], "age": 19},
    ]
    res = process_student_scores(students_data)
    assert res["top_student"] == "Strong"

def test_all_scores_empty_average_is_zero_and_student_is_failed():
    students_data = [{"name": "Пустой", "scores": [], "age": 20}]
    res = process_student_scores(students_data)
    assert res["total_students"] == 1
    assert res["average_score"] == 0.00
    assert res["top_student"] == "Пустой"
    assert res["failed_students"] == ["Пустой"]
    assert res["adults_count"] == 1
