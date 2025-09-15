
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

best_name = ""
best_avg = 0

for student in students.values():
    grades = list(student["grades"].values())
    avg = sum(grades) / len(grades)
    
    if avg > best_avg:
        best_avg = avg
        best_name = student["name"]

print(f"{best_name}: {best_avg:.2f}")

"""ff"""