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


# =============================================================================
# ЗАДАНИЕ: Написать pytest тесты для функции process_student_scores
# =============================================================================
"""
УСЛОВИЕ ЗАДАЧИ:

Вам необходимо написать набор тестов для функции process_student_scores(),
которая обрабатывает данные об оценках студентов.

ТРЕБОВАНИЯ К ТЕСТАМ:
1. Используйте только простые test_ функции и assert
2. Напишите минимум 7 тестов, покрывающих различные сценарии:
   - Тест с обычными корректными данными
   - Тест с пустым списком студентов
   - Тест со студентом без оценок (пустой список scores)
   - Тест с одним студентом
   - Тест с проверкой подсчета неуспевающих студентов (средний балл < 60)
   - Тест с проверкой подсчета совершеннолетних (возраст >= 18)
   - Тест с проверкой определения лучшего студента

3. В функции есть 4 ошибки - ваши тесты должны их найти!

ФОРМАТ ВХОДНЫХ ДАННЫХ:
students_data = [
    {"name": "Иван", "scores": [85, 90, 78], "age": 20},
    {"name": "Мария", "scores": [55, 60, 50], "age": 18},
    ...
]

ФОРМАТ ВЫХОДНЫХ ДАННЫХ:
{
    "total_students": 2,
    "average_score": 69.67,
    "top_student": "Иван",
    "failed_students": ["Мария"],
    "adults_count": 2
}

ПОДСКАЗКИ:
- Неуспевающий студент: средний балл < 60
- Совершеннолетний: возраст >= 18
- При пустом списке функция должна вернуть None
- Средний балл округляется до 2 знаков после запятой

Создайте файл test_buggy_function.py и напишите тесты!
"""