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
avg_grades = [sum(g)/len(g) for g in grades_list]
best_index = avg_grades.index(max(avg_grades))
worst_index = avg_grades.index(min(avg_grades))
bad_indexes = [i for i, g in enumerate(grades_list) if 2 in g]

print(f"Средние баллы: {[round(x, 2) for x in avg_grades]}")
print(f"Лучший студент: {names[best_index]} ({avg_grades[best_index]:.2f})")
print(f"Худший студент: {names[worst_index]} ({avg_grades[worst_index]:.2f})")
print(f"Студенты с двойками: {[names[i] for i in bad_indexes]}")