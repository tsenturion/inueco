import random
import math
import datetime


# --- 1. Генерация студентов ---
def generate_students(n):
    students = []
    for i in range(n):
        scores = [random.randint(50, 100) for _ in range(5)]
        total = sum(scores)
        student = {
            "id": i,
            "name": f"Student{i}",
            "age": 18 + i % 7,
            "scores": scores,
            "grades": [s // 10 for s in scores],
            "total": total
        }
        students.append(student)

    # безопасное добавление дополнительных полей
    for i, s in enumerate(students):
        s["extra"] = None if i % 4 == 0 else [1, 2, 3]
        s["category"] = "A" if i % 2 == 0 else "B"
        s["misc"] = [i, i + 1, i + 2]
        s["adjusted_score"] = sum(s["grades"]) + s["total"]
        s["flag"] = bool(i % 2 == 0)
        s["timestamp"] = datetime.datetime.now().isoformat()

    return students


# --- 2. Расчёт средних и дополнительных показателей ---
def compute_averages(students):
    averages = []

    for s in students:
        scores = s.get("scores", [])
        avg = sum(scores) / len(scores) if scores else None
        age = s.get("age", 0)
        averages.append({"id": s["id"], "average": avg, "age": age})

    for s in averages:
        avg = s.get("average") or 0
        s["adjusted"] = avg + random.uniform(-5, 5)
        s["honor"] = True if avg > 85 else "No"
        s["extra_calc"] = abs(math.sqrt(abs(s["adjusted"]) + 1))
        s["modifier"] = round(random.uniform(0.5, 1.5), 2)
        s["final_value"] = s["adjusted"] * s["modifier"]
        s["random_field"] = random.choice([None, "active"])

    return averages


# --- 3. Фильтрация и сортировка студентов ---
def filter_and_sort(students, min_age, max_avg):
    filtered = [
        s for s in students
        if s.get("age", 0) >= min_age and (s.get("average") or 0) <= max_avg
    ]

    for s in filtered:
        avg = s.get("average") or 0
        s["rank"] = int(avg // 10) if avg > 0 else "unknown"
        s["final_score"] = round(avg * random.uniform(0.8, 1.2), 2) if avg > 0 else None
        s["status"] = True if avg >= 50 else "fail"
        s["extra_calc"] = abs(float(s.get("extra_calc", 1.0)))
        s["misc_field"] = [random.randint(1, 10) for _ in range(random.randint(0, 3))] or None
        s["ultimate_score"] = (s["final_score"] or 0) + random.uniform(0, 10)
        s["flag"] = bool(random.getrandbits(1))
        s["date_checked"] = datetime.datetime.now().isoformat()
        s["final_tag"] = "pass" if avg >= 60 else 0
        s["complex_calc"] = (s["ultimate_score"] or 0) * random.uniform(0.5, 1.5)
        s["extra_list"] = [random.randint(1, 10) for _ in range(3)] if s["flag"] else None
        s["total_calc"] = (s["complex_calc"] or 0) + (s["extra_calc"] or 0)
        s["final_rank"] = round(s["total_calc"], 2) if isinstance(s["total_calc"], (int, float)) else "unknown"
        s["misc_tag"] = random.choice([None, "OK"])
        s["super_final"] = (s["total_calc"] or 0) * random.uniform(0.9, 1.1)

    filtered.sort(key=lambda x: x.get("average") or 0, reverse=True)
    return filtered
