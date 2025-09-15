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
for student_id, student in students.items():
  grades_str = ', '.join([f"{subj}: {grade}" for subj, grade in student['grades'].items()])
  print(f"ID {student_id}: {student['name']}, {student['age']} лет, {student['group']}, оценки: {grades_str}")

"""
2
Добавьте в словарь нового студента с ID 104:
Имя: "Екатерина Волкова"
Возраст: 20
Оценки: math=5, physics=5, programming=5
Группа: "ИТ-102"
Выведите сообщение о добавлении.
"""
students[104] = {
    "name": "Екатерина Волкова",
    "age": 20,
    "grades": {"math": 5, "physics": 5, "programming": 5},
    "group": "ИТ-102"
}

print("✅ Студент успешно добавлен!")
for student_id, student in students.items():
  grades_str = ', '.join([f"{subj}: {grade}" for subj, grade in student['grades'].items()])
  print(f"ID {student_id}: {student['name']}, {student['age']} лет, {student['group']}, оценки: {grades_str}")
"""
3
Для каждого студента рассчитайте и выведите средний балл по всем предметам. Сохраните результаты в отдельный словарь average_grades.
"""
average_grades = {}
for student_id, student_info in students.items():
    grades = student_info["grades"]
    avg_grade = sum(grades.values()) / len(grades)
    average_grades[student_id] = round(avg_grade, 2)

print("Словарь средних баллов:")
print(average_grades)
"""
4
Найдите студента с наивысшим средним баллом. Выведите его имя, средний балл и группу.
"""
best = max(students.values(), key=lambda s: sum(s["grades"].values())/len(s["grades"]))
avg = sum(best["grades"].values()) / len(best["grades"])

print(f"{best['name']}, {best['group']}, {avg:.2f}")
"""
5
Соберите статистику по группам:
Количество студентов в каждой группе
Средний балл группы
Список студентов каждой группы
Выведите статистику для групп "ИТ-101" и "ИТ-102".
"""
group_stats = {}
for s in students.values():
    g = s["group"]
    if g not in group_stats:
        group_stats[g] = {"c": 0, "t": 0, "s": []}
    group_stats[g]["c"] += 1
    group_stats[g]["t"] += sum(s["grades"].values()) / len(s["grades"])
    group_stats[g]["s"].append(s["name"])

for g in ["ИТ-101", "ИТ-102"]:
    stats = group_stats[g]
    print(f"{g}: {stats['c']} студентов, ср. балл: {stats['t']/stats['c']:.2f}, студенты: {', '.join(stats['s'])}")
    """ 
    c - количество студентов
    t - сумма баллов
    s - список студентов
    g - группа
    """
"""
6
Для каждого студента вычислите хеш его имени с помощью функции hash(). Проверьте, есть ли коллизии хешей (одинаковые хеши для разных имен).
"""
print("Хеши имен:", {s["name"]: hash(s["name"]) for s in students.values()})
collisions = {h: names for h, names in {hash(s["name"]): [s["name"]] for s in students.values()}.items() if len(names) > 1}
print(f"Коллизии: {collisions}" if collisions else "Коллизий нет")
"""
7
Найдите и выведите:
Всех студентов с оценкой 5 по программированию
Всех студентов старше 20 лет
"""
prog5 = [s["name"] for s in students.values() if s["grades"].get("programming") == 5]
print("5 по программированию:", *prog5 if prog5 else "нет")

age20 = [s["name"] for s in students.values() if s["age"] > 20]
print("Старше 20 лет:", *age20 if age20 else "нет")
"""
8
Добавьте всем студентам оценку по предмету "english":
ID 101: 4
ID 102: 5
ID 103: 3
ID 104: 5
Выведите обновленные данные для студента ID 101.
"""
students[101]["grades"]["english"] = 4
students[102]["grades"]["english"] = 5
students[103]["grades"]["english"] = 3
students[104]["grades"]["english"] = 5

print(f"{students[101]['name']}: {students[101]['grades']}")