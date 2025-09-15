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

"""
1
Выведите на экран информацию о всех студентах в читаемом формате. Для каждого студента отобразите:
ID студента
Имя
Возраст
Группу
Все оценки по предметам
"""
print("-" * 50)
student_ids = list(students.keys())
i = 0
while i < len(student_ids):
    student_id = student_ids[i]
    student_data = students[student_id]
    
    print("ID:", student_id)
    print("Имя:", student_data["name"])
    print("Возраст:", student_data["age"])
    print("Группа:", student_data["group"])
    print("Оценки:")
    
    subjects = list(student_data["grades"].keys())
    j = 0
    while j < len(subjects):
        subject = subjects[j]
        grade = student_data["grades"][subject]
        print(" ", subject, ":", grade)
        j = j + 1
    
    print("----------------------------------")
    i = i + 1
"""
2
Добавьте в словарь нового студента с ID 104:
Имя: "Екатерина Волкова"
Возраст: 20
Оценки: math=5, physics=5, programming=5
Группа: "ИТ-102"
Выведите сообщение о добавлении.
"""
print("-" * 50)
new_student_id = 104
new_student = {
    "name": "Екатерина Волкова",
    "age": 20,
    "grades": {"math": 5, "physics": 5, "programming": 5},
    "group": "ИТ-102"
}

students[new_student_id] = new_student
print("Добавлен новый студент:", new_student["name"])
"""
3
Для каждого студента рассчитайте и выведите средний балл по всем предметам. 
Сохраните результаты в отдельный словарь average_grades.
"""
print("-" * 50)
average_grades = {}
student_ids = list(students.keys())
i = 0
while i < len(student_ids):
    student_id = student_ids[i]
    student_data = students[student_id]
    
    grades_list = list(student_data["grades"].values())
    total = 0
    j = 0
    while j < len(grades_list):
        total = total + grades_list[j]
        j = j + 1
    
    if len(grades_list) > 0:
        avg_grade = total / len(grades_list)
    else:
        avg_grade = 0
    
    average_grades[student_id] = avg_grade
    print(student_data["name"], ":", avg_grade)
    i = i + 1
"""
4
Найдите студента с наивысшим средним баллом. Выведите его имя, средний балл и группу.
"""
print("-" * 50)
student_ids = list(average_grades.keys())
best_id = student_ids[0]
best_grade = average_grades[best_id]

i = 1
while i < len(student_ids):
    current_id = student_ids[i]
    current_grade = average_grades[current_id]
    if current_grade > best_grade:
        best_id = current_id
        best_grade = current_grade
    i = i + 1

best_student = students[best_id]
print("Лучший студент:", best_student["name"])
print("Средний балл:", best_grade)
print("Группа:", best_student["group"])
"""
5
Соберите статистику по группам:
Количество студентов в каждой группе
Средний балл группы
Список студентов каждой группы
Выведите статистику для групп "ИТ-101" и "ИТ-102".
"""
print("-" * 50)
group_stats = {}
student_ids = list(students.keys())
i = 0
while i < len(student_ids):
    student_id = student_ids[i]
    student_data = students[student_id]
    group = student_data["group"]
    
    if group not in group_stats:
        group_stats[group] = {"count": 0, "total_grade": 0, "students": []}
    
    group_stats[group]["count"] = group_stats[group]["count"] + 1
    group_stats[group]["total_grade"] = group_stats[group]["total_grade"] + average_grades[student_id]
    group_stats[group]["students"].append(student_data["name"])
    i = i + 1

target_groups = ["ИТ-101", "ИТ-102"]
k = 0
while k < len(target_groups):
    group = target_groups[k]
    if group in group_stats:
        stats = group_stats[group]
        
        print("Группа", group + ":")
        print(" Количество студентов:", stats["count"])
        
        if stats["count"] > 0:
            avg_group_grade = stats["total_grade"] / stats["count"]
        else:
            avg_group_grade = 0
        
        print(" Средний балл группы:", avg_group_grade)
        print(" Студенты:", end=" ")
        
        m = 0
        while m < len(stats["students"]):
            if m > 0:
                print(",", end=" ")
            print(stats["students"][m], end="")
            m = m + 1
        print()
        print()
    else:
        print("Группа", group + ": не найдена")
        print()
    k = k + 1
"""
6
Для каждого студента вычислите хеш его имени с помощью функции hash(). 
Проверьте, есть ли коллизии хешей (одинаковые хеши для разных имен).
"""
print("-" * 50)
name_hashes = {}
student_ids = list(students.keys())
i = 0
while i < len(student_ids):
    student_id = student_ids[i]
    student_data = students[student_id]
    name_hash = hash(student_data["name"])
    name_hashes[student_id] = name_hash
    print(student_data["name"], ":", name_hash)
    i = i + 1

print("")
print("Проверка коллизий хешей:")
hashes_list = list(name_hashes.values())
unique_hashes = []
j = 0
while j < len(hashes_list):
    current_hash = hashes_list[j]
    found = False
    k = 0
    while k < len(unique_hashes):
        if current_hash == unique_hashes[k]:
            found = True
            break
        k = k + 1
    if not found:
        unique_hashes.append(current_hash)
    j = j + 1

if len(unique_hashes) == len(students):
    print("Коллизий хешей не обнаружено!")
else:
    print("Обнаружены коллизии хешей!")
"""
7
Найдите и выведите:
Всех студентов с оценкой 5 по программированию
Всех студентов старше 20 лет
"""
print("-" * 50)
student_ids = list(students.keys())
i = 0
while i < len(student_ids):
    student_id = student_ids[i]
    student_data = students[student_id]
    if "programming" in student_data["grades"] and student_data["grades"]["programming"] == 5:
        print("-", student_data["name"], "(Группа:", student_data["group"] + ")")
    i = i + 1

print("")
print("Студенты старше 20 лет:")
i = 0
while i < len(student_ids):
    student_id = student_ids[i]
    student_data = students[student_id]
    if student_data["age"] > 20:
        print("-", student_data["name"], "(Возраст:", student_data["age"], ")")
    i = i + 1
"""
8
Добавьте всем студентам оценку по предмету "english":
ID 101: 4
ID 102: 5
ID 103: 3
ID 104: 5
Выведите обновленные данные для студента ID 101.
"""
print("-" * 50)
student_ids = list(students.keys())
i = 0
while i < len(student_ids):
    student_id = student_ids[i]
    if student_id == 101:
        students[student_id]["grades"]["english"] = 4
    elif student_id == 102:
        students[student_id]["grades"]["english"] = 5
    elif student_id == 103:
        students[student_id]["grades"]["english"] = 3
    elif student_id == 104:
        students[student_id]["grades"]["english"] = 5
    i = i + 1

print("Добавлены оценки по английскому языку!")

print("")
print("Обновленные данные студента ID 101:")
print("ID: 101")
print("Имя:", students[101]["name"])
print("Возраст:", students[101]["age"])
print("Группа:", students[101]["group"])
print("Оценки:")
subjects = list(students[101]["grades"].keys())
j = 0
while j < len(subjects):
    subject = subjects[j]
    grade = students[101]["grades"][subject]
    print(" ", subject, ":", grade)
    j = j + 1