def process_student_scores(students_data):
    """
    Обрабатывает данные об оценках студентов и возвращает статистику.

    Args:
        students_data: список словарей [{"name": str, "scores": [int], "age": int}, ...]

    Returns:
        dict:
        {
            "total_students": int,
            "average_score": float,
            "top_student": str | None,
            "failed_students": list[str],
            "adults_count": int
        }
        или None, если входной список пуст.
    """
    if not students_data:
        return None

    total_students = len(students_data)
    all_scores = []
    student_averages = {}
    failed_students = []
    adults_count = 0

    for student in students_data:
        name = student["name"]
        scores = student["scores"] or []
        age = student["age"]

        # для пустых scores среднее = 0.0 (без деления на ноль)
        student_avg = (sum(scores) / len(scores)) if scores else 0.0
        student_averages[name] = student_avg

        all_scores.extend(scores)

        # неуспевающий, если средний балл < 60
        if student_avg < 60:
            failed_students.append(name)

        # совершеннолетний, если возраст >= 18
        if age >= 18:
            adults_count += 1

    # общий средний по всем оценкам; если оценок нет — 0.0
    average_score = (sum(all_scores) / len(all_scores)) if all_scores else 0.0

    # лучший студент по максимальному среднему
    top_student = max(student_averages, key=student_averages.get) if student_averages else None

    return {
        "total_students": total_students,
        "average_score": round(average_score, 2),
        "top_student": top_student,
        "failed_students": failed_students,
        "adults_count": adults_count,
    }