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
for i, student in enumerate(names):
    avg = sum(grades[i]) / len(grades[i])
    print(f"{student}: {avg}")

# Лучший
avg_scores = [sum(g) / len(g) for g in grades]
best = avg_scores.index(max(avg_scores))
print(f"Лучший: {names[best]}")

# С двойками
with_2 = [i for i, g in enumerate(grades) if 2 in g]
print(f"С двойками: {with_2}")



