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

# 1. Вывод информации о всех студентах
print("=== Задание 1: Информация о студентах ===")
for student_id, info in students.items():
    print(f"ID: {student_id}")
    print(f"Имя: {info['name']}")
    print(f"Возраст: {info['age']}")
    print(f"Группа: {info['group']}")
    print("Оценки:", ", ".join([f"{subject}: {grade}" for subject, grade in info['grades'].items()]))
    print("-" * 40)

# 2. Добавление нового студента
print("\n=== Задание 2: Добавление нового студента ===")
students[104] = {
    "name": "Екатерина Волкова",
    "age": 20,
    "grades": {"math": 5, "physics": 5, "programming": 5},
    "group": "ИТ-102"
}
print("Добавлен студент с ID 104: Екатерина Волкова")

# 3. Расчёт среднего балла для каждого студента
print("\n=== Задание 3: Средний балл студентов ===")
average_grades = {}
for student_id, info in students.items():
    grades = info['grades'].values()
    average = sum(grades) / len(grades)
    average_grades[student_id] = round(average, 2)
    print(f"{info['name']}: {round(average, 2)}")

# 4. Поиск студента с наивысшим средним баллом
print("\n=== Задание 4: Лучший студент ===")
best_student_id = max(average_grades, key=average_grades.get)
best_student = students[best_student_id]
print(f"Имя: {best_student['name']}")
print(f"Средний балл: {average_grades[best_student_id]}")
print(f"Группа: {best_student['group']}")

# 5. Статистика по группам
print("\n=== Задание 5: Статистика по группам ===")
group_stats = {}
for student_id, info in students.items():
    group = info['group']
    if group not in group_stats:
        group_stats[group] = {
            'count': 0,
            'total_grade': 0,
            'students': []
        }
    group_stats[group]['count'] += 1
    group_stats[group]['total_grade'] += average_grades[student_id]
    group_stats[group]['students'].append(info['name'])

for group, stats in group_stats.items():
    avg_grade = stats['total_grade'] / stats['count']
    print(f"Группа {group}:")
    print(f"  Количество студентов: {stats['count']}")
    print(f"  Средний балл: {round(avg_grade, 2)}")
    print(f"  Список студентов: {', '.join(stats['students'])}")

# 6. Проверка хешей имён на коллизии
print("\n=== Задание 6: Проверка хешей имён ===")
name_hashes = {}
collisions = False
for info in students.values():
    name = info['name']
    h = hash(name)
    if h in name_hashes:
        print(f"Коллизия: {name} и {name_hashes[h]} имеют одинаковый хеш {h}")
        collisions = True
    else:
        name_hashes[h] = name
if not collisions:
    print("Коллизий не обнаружено")

# 7. Поиск студентов по критериям
print("\n=== Задание 7: Поиск студентов ===")
print("Студенты с оценкой 5 по программированию:")
for info in students.values():
    if info['grades'].get('programming') == 5:
        print(f"  - {info['name']}")

print("\nСтуденты старше 20 лет:")
for info in students.values():
    if info['age'] > 20:
        print(f"  - {info['name']}")

# 8. Добавление оценки по английскому
print("\n=== Задание 8: Добавление оценки 'english' ===")
english_grades = {101: 4, 102: 5, 103: 3, 104: 5}
for student_id, grade in english_grades.items():
    students[student_id]['grades']['english'] = grade

print("Обновленные данные студента ID 101:")
print(students[101])