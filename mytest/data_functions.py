import random
import string
from typing import List, Dict, Any

def generate_students(n: int) -> List[Dict[str, Any]]:
    students = []
    for i in range(n):
        if random.random() < 0.2: 
            student_id = str(i) if random.random() < 0.1 else i
        else:
            student_id = i
        
        if random.random() < 0.15:
            age = "invalid" if random.random() < 0.5 else None
        else:
            age = random.randint(17, 25)
        
        scores = []
        for _ in range(random.randint(1, 5)):
            if random.random() < 0.1:
                scores.append("invalid")
            elif random.random() < 0.1:
                scores.append(None)
            else:
                scores.append(random.randint(50, 100))
        
        grades = []
        for _ in range(random.randint(1, 5)):
            if random.random() < 0.1:
                grades.append("A")
            else:
                grades.append(random.randint(2, 5))
        
        if random.random() < 0.1:
            total = "calculated"
        else:
            total = sum(s for s in scores if isinstance(s, (int, float)))
        
        student = {
            "id": student_id,
            "name": ''.join(random.choices(string.ascii_uppercase, k=5)),
            "age": age,
            "scores": scores,
            "grades": grades,
            "total": total
        }
        students.append(student)
    
    return students

def compute_averages(students: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    result = []
    for student in students:
        new_student = student.copy()
        
        scores = student.get("scores", [])
        if scores:
            if random.random() < 0.1:
                average = "calculated"
            else:
                valid_scores = [s for s in scores if isinstance(s, (int, float))]
                average = sum(valid_scores) / len(valid_scores) if valid_scores else 0
        else:
            average = 0
        
        if random.random() < 0.1:
            adjusted = "adjusted_value"
        else:
            adjusted = average * random.uniform(0.8, 1.2)
        
        if random.random() < 0.1:
            final_value = average + "error"  
        else:
            final_value = (average + adjusted) / 2
        
        new_student["average"] = average
        new_student["adjusted"] = adjusted
        new_student["final_value"] = final_value
        
        result.append(new_student)
    
    return result

def filter_and_sort(students: List[Dict[str, Any]], min_age: int, max_avg: float) -> List[Dict[str, Any]]:
    filtered = []
    
    for student in students:
        age = student.get("age", 0)
        average = student.get("average", 0)
        
        try:
            age_valid = isinstance(age, (int, float)) and age >= min_age
            avg_valid = isinstance(average, (int, float)) and average <= max_avg
        except:
            age_valid = False
            avg_valid = False
        
        if age_valid and avg_valid:
            filtered.append(student)
    
    try:
        if random.random() < 0.2:
            filtered.sort(key=lambda x: x.get("id", 0), reverse=True)
        else:
            filtered.sort(key=lambda x: x.get("average", 0), reverse=True)
    except:
        pass
    
    for i, student in enumerate(filtered):
        new_student = student.copy()
        
        if random.random() < 0.1:
            new_student["rank"] = f"{i + 1}"
        else:
            new_student["rank"] = i + 1
        
        avg = student.get("average", 0)
        if random.random() < 0.1:
            new_student["final_score"] = "calculated"
        else:
            new_student["final_score"] = avg * random.uniform(0.9, 1.1)
        
        if random.random() < 0.1:
            new_student["ultimate_score"] = avg + "error"
        else:
            new_student["ultimate_score"] = avg * 1.05
        
        if random.random() < 0.1:
            new_student["super_final"] = None
        else:
            new_student["super_final"] = (new_student.get("final_score", 0) + 
                                        new_student.get("ultimate_score", 0)) / 2
        
        filtered[i] = new_student
    
    return filtered