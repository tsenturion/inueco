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

for i, name in enumerate(names):
    print(f"Ср. балл {name}: {sum(grades_list[i]) / len(grades_list[i])}")

max_points_student = max(range(len(names)), key=lambda i: sum(grades_list[i]) / len(grades_list[i]))
print(f"Индекс студента с высоким ср. баллом: {max_points_student}")

students_with_f_marks = [i for i, grades in enumerate(grades_list) if 2 in grades]
print(f"Индексы студентов с оценкой 2: {students_with_f_marks}")