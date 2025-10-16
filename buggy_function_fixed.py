# tasktest/src/buggy_function_fixed.py
def process_student_scores(students_data):
    """
    Обрабатывает данные об оценках студентов и возвращает статистику.
    ИСПРАВЛЕННАЯ ВЕРСИЯ
    
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
        
        # ИСПРАВЛЕНИЕ 1: проверка на пустой список оценок
        if not scores:
            student_avg = 0
        else:
            student_avg = sum(scores) / len(scores)
        
        student_averages[name] = student_avg
        all_scores.extend(scores)
        
        # ИСПРАВЛЕНИЕ 2: правильное условие для неуспевающих (< 60 вместо <= 60)
        if student_avg < 60:
            failed_students.append(name)
        
        # ИСПРАВЛЕНИЕ 3: правильное условие для совершеннолетних (>= 18 вместо > 18)
        if age >= 18:
            adults_count += 1
    
    # ИСПРАВЛЕНИЕ 4: проверка на пустой список всех оценок
    if not all_scores:
        average_score = 0
    else:
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