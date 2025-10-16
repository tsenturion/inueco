import pytest

def process_student_scores(students_data):
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


# Тесты
def test_normal_case():
    students_data = [
        {"name": "Иван", "scores": [85, 90, 78], "age": 20},
        {"name": "Мария", "scores": [55, 60, 50], "age": 17},
        {"name": "Петр", "scores": [90, 95, 92], "age": 19}
    ]
    
    result = process_student_scores(students_data)
    
    assert result["total_students"] == 3
    assert result["average_score"] == 77.22
    assert result["top_student"] == "Петр"
    assert "Мария" in result["failed_students"]
    assert result["adults_count"] == 2


def test_empty_list():
    result = process_student_scores([])
    assert result is None


def test_student_without_scores():
    students_data = [
        {"name": "Анна", "scores": [], "age": 20}
    ]
    
    with pytest.raises(0):
        process_student_scores(students_data)


def test_single_student():
    students_data = [
        {"name": "Ольга", "scores": [70, 80, 90], "age": 18}
    ]
    
    result = process_student_scores(students_data)
    
    assert result["total_students"] == 1
    assert result["average_score"] == 80.0
    assert result["top_student"] == "Ольга"
    assert result["failed_students"] == []
    assert result["adults_count"] == 0 


def test_failed_students_calculation():
    students_data = [
        {"name": "Студент1", "scores": [59, 59, 59], "age": 20},  
        {"name": "Студент2", "scores": [60, 60, 60], "age": 21},  
        {"name": "Студент3", "scores": [30, 40, 50], "age": 22}   
    ]
    
    result = process_student_scores(students_data)
    
    assert len(result["failed_students"]) == 2


def test_adults_count_calculation():
    students_data = [
        {"name": "Студент1", "scores": [80, 80, 80], "age": 17}, 
        {"name": "Студент2", "scores": [80, 80, 80], "age": 18},  
        {"name": "Студент3", "scores": [80, 80, 80], "age": 19}   
    ]
    
    result = process_student_scores(students_data)
    
    assert result["adults_count"] == 2


def test_top_student_determination():
    students_data = [
        {"name": "Студент1", "scores": [80, 85, 90], "age": 20},  
        {"name": "Студент2", "scores": [95, 90, 100], "age": 21}, 
        {"name": "Студент3", "scores": [70, 75, 80], "age": 22}   
    ]
    
    result = process_student_scores(students_data)
    
    assert result["top_student"] == "Студент2"
    assert result["average_score"] == 85.0


def test_all_students_failed():
    students_data = [
        {"name": "Студент1", "scores": [50, 55, 45], "age": 20},
        {"name": "Студент2", "scores": [40, 35, 30], "age": 21}
    ]
    
    result = process_student_scores(students_data)
    
    assert len(result["failed_students"]) == 2
    assert result["average_score"] == 42.5


def test_all_students_adults():
    students_data = [
        {"name": "Студент1", "scores": [80, 85, 90], "age": 18},
        {"name": "Студент2", "scores": [75, 80, 85], "age": 19},
        {"name": "Студент3", "scores": [85, 90, 95], "age": 20}
    ]
    
    result = process_student_scores(students_data)
    
    assert result["adults_count"] == 3


def test_tie_for_top_student():
    students_data = [
        {"name": "Студент1", "scores": [90, 90, 90], "age": 20},  
        {"name": "Студент2", "scores": [90, 90, 90], "age": 21}, 
        {"name": "Студент3", "scores": [80, 85, 90], "age": 22}  
    ]
    
    result = process_student_scores(students_data)
    
    assert result["top_student"] in ["Студент1", "Студент2"]
    assert result["average_score"] == 88.33


if __name__ == "__main__":
    pytest.main([__file__, "-v"])