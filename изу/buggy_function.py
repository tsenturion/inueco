def process_student_scores(students_data):
    if not students_data:
        return None

    total_students = len(students_data)
    all_scores = []
    student_averages = {}
    failed_students = []
    adults_count = 0

    for student in students_data:
        name = student["name"]
        scores = student["scores"]
        age = student["age"]

        # безопасно считаем средний при пустом списке оценок
        student_avg = (sum(scores) / len(scores)) if scores else 0.0
        student_averages[name] = student_avg

        # добавляем в общий список только если оценки есть
        if scores:
            all_scores.extend(scores)

        # неуспеваемость — средний балл < 60
        if student_avg < 60:
            failed_students.append(name)

        # совершеннолетие — возраст >= 18
        if age >= 18:
            adults_count += 1

    # общий средний, даже если all_scores пуст
    average_score = round(sum(all_scores) / len(all_scores), 2) if all_scores else 0.0

    top_student = max(student_averages, key=student_averages.get)

    return {
        "total_students": total_students,
        "average_score": average_score,
        "top_student": top_student,
        "failed_students": failed_students,
        "adults_count": adults_count,
    }
