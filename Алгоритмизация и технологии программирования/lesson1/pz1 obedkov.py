students = {
    101: {
        "name": "Иван Иванов",
        "age": 20,
        "grades": {"math": 4, "physics": 5, "programming": 5},
        "group": "ИТ-101"
    },
    102: {
        "name": "Мария Петрова", 
        "age": 19,
        "grades": {"math": 5, "physics": 4, "programming": 4},
        "group": "ИТ-101"
    },
    103: {
        "name": "Алексей Сидоров",
        "age": 21, 
        "grades": {"math": 3, "physics": 3, "programming": 4},
        "group": "ИТ-102"
    }
    
}
def find_best_student(students):
    best_student = None
    best_avg = 0
    
    for student_id, student_data in students.items():
        grades = student_data["grades"].values()
        avg_grade = sum(grades) / len(grades)
        
        if avg_grade > best_avg:
            best_avg = avg_grade
            best_student = student_data
    
    return best_student, best_avg

best_student, avg_grade = find_best_student(students)
print(f"Лучший студент: {best_student['name']}")
print(f"Средний балл: {avg_grade:.2f}")
print(f"Группа: {best_student['group']}")

"""
найти лучше студента по среднему баллу
"""