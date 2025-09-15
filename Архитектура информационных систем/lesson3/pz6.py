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

print("#1")
for id in students:
    print("ID:", id)
    print("Имя:", students[id]["name"])
    print("Возраст:", students[id]["age"])
    print("Группа:", students[id]["group"])
    print("Оценки:", students[id]["grades"])
    print()

print("#2")
students[104] = {
    "name": "Екатерина Волкова",
    "age": 20,
    "grades": {"math": 5, "physics": 5, "programming": 5},
    "group": "ИТ-102"
}
print("Студент добавлен:", students[104]["name"])
print()

print("#3")
average_grades = {}
for id in students:
    grades = students[id]["grades"].values()
    avg = sum(grades) / len(grades)
    average_grades[id] = avg
    print(students[id]["name"], "средний балл:", avg)
print()

print("#4")
best_id = None
best_avg = 0
for id in average_grades:
    if average_grades[id] > best_avg:
        best_avg = average_grades[id]
        best_id = id
print("Лучший студент:", students[best_id]["name"], best_avg, students[best_id]["group"])
print()

print("#5")
groups = {}
for id in students:
    g = students[id]["group"]
    if g not in groups:
        groups[g] = {"count": 0, "total": 0, "names": []}
    groups[g]["count"] += 1
    groups[g]["total"] += average_grades[id]
    groups[g]["names"].append(students[id]["name"])

for g in groups:
    print("Группа:", g)
    print("Количество:", groups[g]["count"])
    print("Средний балл:", groups[g]["total"] / groups[g]["count"])
    print("Студенты:", groups[g]["names"])
    print()

print("#6")
hashes = {}
for id in students:
    h = hash(students[id]["name"])
    if h not in hashes:
        hashes[h] = []
    hashes[h].append(students[id]["name"])

for h in hashes:
    if len(hashes[h]) > 1:
        print("Коллизия:", hashes[h])
print()

print("#7")
print("Студенты с 5 по программированию:")
for id in students:
    if students[id]["grades"]["programming"] == 5:
        print(students[id]["name"])

print("Студенты старше 20:")
for id in students:
    if students[id]["age"] > 20:
        print(students[id]["name"])
print()

print("#8")
students[101]["grades"]["english"] = 4
students[102]["grades"]["english"] = 5
students[103]["grades"]["english"] = 3
students[104]["grades"]["english"] = 5
print("ID 101 обновлен:", students[101])


#ipoco m99 x3 pro 99g