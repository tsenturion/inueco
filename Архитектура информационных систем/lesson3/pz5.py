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
average_grades = []
for grades in grades_list:
    average = sum(grades) / len(grades)
    average_grades.append(average)
print("Средние балл :")
for i, (name, avg) in enumerate(zip(names, average_grades)):
    print(f"{i}: {name} - {avg:.2f}")
max_avg_index = average_grades.index(max(average_grades))
print(f"\nСтудентс самым высоким средним баллом: {max_avg_index} ({names[max_avg_index]})")
students_with_2 = []
for i, grades in enumerate(grades_list):
    if 2 in grades:
        students_with_2.append(i)
print(f"\nИндексы студентов с оценкой 2: {students_with_2}")
       