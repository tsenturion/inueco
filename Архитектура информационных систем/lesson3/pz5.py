"""
Вычислите средний балл для каждого студента
Найдите индекс студента с самым высоким средним баллом
Найдите индексы всех студентов, у которых есть хотя бы одна оценка 2
"""
names = ["Анна", "Борис", "Виктория", "Григорий", "Дарья"]
grades_list = [
    [4, 5, 4, 3, 5],
    [3, 4, 3, 5, 4],
    [5, 5, 5, 4, 5],
    [2, 3, 2, 4, 3],
    [4, 4, 5, 4, 4]
]

averages = [0, 0, 0, 0, 0]
i = 0
for grades in grades_list:
    total = 0
    count = 0
    for grade in grades:
        total += grade
        count += 1
    averages[i] = total / count
    i += 1

best_index = 0
i = 1
while i < 5:
    if averages[i] > averages[best_index]:
        best_index = i
    i += 1

students_with_2 = []
i = 0
for grades in grades_list:
    has_two = False
    for grade in grades:
        if grade == 2:
            has_two = True
            break
    if has_two:
        students_with_2 = students_with_2 + [i]
    i += 1

print("Средние баллы:", averages)
print("Индекс лучшего студента:", best_index)
print("Индексы студентов с оценкой 2:", students_with_2)