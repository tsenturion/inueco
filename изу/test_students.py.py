import sys
import traceback


def generate_students(n):
    if n <= 0:
        return []
    
    students = []
    for i in range(n):
        student = {
            "id": i + 1,
            "name": f"Student_{i+1}",
            "age": 18 + (i % 7),
            "scores": [60 + i * 2, 70 + i, 80 - i],
            "grades": [3 + (i % 3), 4 - (i % 2)],
            "total": 210 + i * 3
        }
        
        if i == 2:
            student["name"] = 123
        elif i == 5:
            student["age"] = "25"
        elif i == 8:
            student["scores"] = "not_a_list"
            
        students.append(student)
    return students

def compute_averages(students):
    if not students:
        return []
        
    result = []
    for student in students:
        student_copy = student.copy()
        
        scores = student.get("scores", [])
        if isinstance(scores, list) and scores and all(isinstance(score, (int, float)) for score in scores):
            avg = sum(scores) / len(scores)
        else:
            avg = 0.0
            
        student_copy["average"] = avg
        
        student_id = student.get("id", 0)
        if student_id % 4 == 0:
            student_copy["adjusted"] = "high"
            
        result.append(student_copy)
    return result

def filter_and_sort(students, min_age=18, max_avg=100):
    if not students:
        return []
    
    filtered = []
    for student in students:
        age = student.get("age", 0)
        avg = student.get("average", 0)
        
        if isinstance(age, str):
            try:
                age = int(age)
            except:
                age = 0
                
        if age >= min_age and avg <= max_avg:
            student_copy = student.copy()
            
            student_copy["rank"] = len(filtered) + 1
            
            student_id = student.get("id", 0)
            if student_id % 3 == 0:
                student_copy["final_score"] = "excellent"
            else:
                student_copy["final_score"] = avg * 1.1
                
            if student_id % 5 == 0:
                student_copy["ultimate_score"] = None
            else:
                student_copy["ultimate_score"] = avg * 0.9
                
            student_copy["super_final"] = (avg + student.get("total", 0) / 100) / 2
                
            filtered.append(student_copy)
    
    return sorted(filtered, key=lambda x: x.get("average", 0), reverse=True)


class TestRunner:
    
    def __init__(self):
        self.passed = 0
        self.failed = 0
        self.errors = []
    
    def assert_equal(self, actual, expected, message=""):
        if actual != expected:
            error_msg = f"{message}\nExpected: {expected}\nActual: {actual}"
            self.errors.append(error_msg)
            raise AssertionError(error_msg)
        return True
    
    def assert_true(self, condition, message=""):
        if not condition:
            error_msg = f"{message}\nCondition is False"
            self.errors.append(error_msg)
            raise AssertionError(error_msg)
        return True
    
    def assert_is_instance(self, obj, cls, message=""):
        if not isinstance(obj, cls):
            error_msg = f"{message}\nExpected type: {cls}\nActual type: {type(obj)}"
            self.errors.append(error_msg)
            raise AssertionError(error_msg)
        return True
    
    def assert_not_none(self, obj, message=""):
        if obj is None:
            error_msg = f"{message}\nObject is None"
            self.errors.append(error_msg)
            raise AssertionError(error_msg)
        return True
    
    def run_test(self, test_func, test_name):
        try:
            test_func()
            self.passed += 1
            print(f"PASSED: {test_name}")
            return True
        except AssertionError as e:
            self.failed += 1
            print(f"FAILED: {test_name}")
            self.errors.append(f"{test_name}: {str(e)}")
            return False
        except Exception as e:
            self.failed += 1
            print(f"ERROR: {test_name} - {str(e)}")
            self.errors.append(f"{test_name}: {traceback.format_exc()}")
            return False
    
    def print_summary(self):
        print("\n" + "="*50)
        print("ТЕСТЫ ЗАВЕРШЕНЫ")
        print("="*50)
        print(f"Пройдено: {self.passed}")
        print(f"Провалено: {self.failed}")
        print(f"Всего: {self.passed + self.failed}")
        
        if self.errors:
            print(f"\nПервые 5 ошибок из {len(self.errors)}:")
            for i, error in enumerate(self.errors[:5], 1):
                print(f"{i}. {error}")
        
        success_rate = (self.passed / (self.passed + self.failed)) * 100 if (self.passed + self.failed) > 0 else 0
        print(f"\nУспешность: {success_rate:.1f}%")
        
        expected_passed = 15
        expected_failed = 10
        if self.passed == expected_passed and self.failed == expected_failed:
            print("Соответствует ожиданиям: 15 пройдено, 10 упало")
        else:
            print(f"Не соответствует ожиданиям: ожидалось {expected_passed} пройдено, {expected_failed} упало")


runner = TestRunner()


def test_001_return_type_and_length():
    result = generate_students(5)
    runner.assert_is_instance(result, list, "Result should be a list")
    runner.assert_equal(len(result), 5, "List should have 5 elements")

def test_002_dict_structure():
    result = generate_students(1)
    if result:
        student = result[0]
        expected_keys = {"id", "name", "age", "scores", "grades", "total"}
        runner.assert_equal(set(student.keys()), expected_keys, "Student should have all required keys")

def test_003_unique_ids():
    result = generate_students(10)
    ids = [student["id"] for student in result]
    runner.assert_equal(len(ids), len(set(ids)), "All IDs should be unique")

def test_004_return_type_compute_averages():
    students = generate_students(3)
    result = compute_averages(students)
    runner.assert_is_instance(result, list, "Result should be a list")

def test_005_avg_field_exists():
    students = generate_students(3)
    result = compute_averages(students)
    for student in result:
        runner.assert_true("average" in student, "Student should have average field")

def test_006_avg_calculation_correctness():
    test_students = [
        {"id": 1, "name": "Test", "age": 20, "scores": [10, 20, 30], "grades": [4, 5], "total": 60}
    ]
    result = compute_averages(test_students)
    expected_avg = 20.0
    runner.assert_equal(result[0]["average"], expected_avg, "Average calculation should be correct")

def test_007_empty_scores_handling():
    test_students = [
        {"id": 1, "name": "Test", "age": 20, "scores": [], "grades": [], "total": 0}
    ]
    result = compute_averages(test_students)
    runner.assert_true("average" in result[0], "Student should have average field")

def test_008_return_type_filter_and_sort():
    students = generate_students(5)
    students_with_avg = compute_averages(students)
    result = filter_and_sort(students_with_avg, min_age=18, max_avg=100)
    runner.assert_is_instance(result, list, "Result should be a list")

def test_009_age_filter():
    test_students = [
        {"id": 1, "name": "A", "age": 17, "average": 50},
        {"id": 2, "name": "B", "age": 18, "average": 60},
        {"id": 4, "name": "C", "age": 19, "average": 70},
    ]
    result = filter_and_sort(test_students, min_age=18, max_avg=100)
    ages = [student["age"] for student in result]
    runner.assert_true(all(age >= 18 for age in ages), "All students should be >= 18 years")

def test_010_avg_filter():
    test_students = [
        {"id": 1, "name": "A", "age": 20, "average": 50},
        {"id": 2, "name": "B", "age": 20, "average": 60},
        {"id": 4, "name": "C", "age": 20, "average": 70},
    ]
    result = filter_and_sort(test_students, min_age=18, max_avg=65)
    averages = [student["average"] for student in result]
    runner.assert_true(all(avg <= 65 for avg in averages), "All averages should be <= 65")

def test_011_sorting_order():
    test_students = [
        {"id": 1, "name": "A", "age": 20, "average": 50},
        {"id": 2, "name": "B", "age": 20, "average": 70},
        {"id": 4, "name": "C", "age": 20, "average": 60},
    ]
    result = filter_and_sort(test_students, min_age=18, max_avg=100)
    averages = [student["average"] for student in result]
    runner.assert_equal(averages, [70, 60, 50], "Should sort by average in descending order")

def test_012_data_consistency():
    original_students = generate_students(5)
    original_ids = {student["id"] for student in original_students}
    
    students_with_avg = compute_averages(original_students)
    computed_ids = {student["id"] for student in students_with_avg}
    
    runner.assert_equal(original_ids, computed_ids, "IDs should be preserved through computation")

def test_013_edge_cases_empty_list():
    result1 = compute_averages([])
    result2 = filter_and_sort(result1, min_age=18, max_avg=100)
    runner.assert_equal(result2, [], "Empty list should return empty list")

def test_014_generate_invalid_input():
    result = generate_students(0)
    runner.assert_is_instance(result, list, "Should return list for n=0")
    runner.assert_equal(len(result), 0, "List should be empty for n=0")

def test_015_filter_invalid_params():
    students = [{"id": 1, "name": "Test", "age": 20, "average": 50}]
    result = filter_and_sort(students, min_age=-10, max_avg=-5)
    runner.assert_is_instance(result, list, "Should handle negative parameters")


def test_016_field_types_strict():
    result = generate_students(10)
    for student in result:
        runner.assert_is_instance(student["name"], str, "Name should be string")
        runner.assert_is_instance(student["age"], int, "Age should be integer")
        runner.assert_is_instance(student["scores"], list, "Scores should be list")

def test_017_scores_and_grades_content():
    result = generate_students(10)
    for student in result:
        if isinstance(student["scores"], list):
            for score in student["scores"]:
                runner.assert_is_instance(score, (int, float), "Score should be number")
        for grade in student["grades"]:
            runner.assert_is_instance(grade, (int, float), "Grade should be number")

def test_018_avg_type_validation():
    students = generate_students(10)
    result = compute_averages(students)
    for student in result:
        runner.assert_is_instance(student["average"], (int, float), "Average should be number")

def test_019_additional_fields_validation():
    students = generate_students(10)
    result = compute_averages(students)
    for student in result:
        for field in ["adjusted"]:
            if field in student:
                runner.assert_is_instance(student[field], (int, float), f"Field {field} should be number")

def test_020_strict_age_filter_validation():
    test_students = [
        {"id": 3, "name": "C", "age": 19, "average": 70},
        {"id": 2, "name": "B", "age": 18, "average": 60},
        {"id": 1, "name": "A", "age": 17, "average": 50},
    ]
    result = filter_and_sort(test_students, min_age=18, max_avg=100)
    for student in result:
        runner.assert_is_instance(student["final_score"], (int, float), "final_score should be number")

def test_021_strict_avg_filter_validation():
    test_students = [
        {"id": 5, "name": "E", "age": 20, "average": 80},
        {"id": 2, "name": "B", "age": 20, "average": 60},
        {"id": 1, "name": "A", "age": 20, "average": 50},
    ]
    result = filter_and_sort(test_students, min_age=18, max_avg=65)
    for student in result:
        runner.assert_is_instance(student["ultimate_score"], (int, float), "ultimate_score should be number")
        runner.assert_not_none(student["ultimate_score"], "ultimate_score should not be None")

def test_022_additional_fields_types():
    students = generate_students(10)
    students_with_avg = compute_averages(students)
    result = filter_and_sort(students_with_avg, min_age=18, max_avg=100)
    
    for student in result:
        for field in ["final_score", "ultimate_score"]:
            if field in student:
                runner.assert_is_instance(student[field], (int, float), f"Field {field} should be number")
                if field == "ultimate_score":
                    runner.assert_not_none(student[field], f"Field {field} should not be None")

def test_023_compute_with_none_values():
    students_with_none = [
        {"id": 1, "name": None, "age": None, "scores": [None, 10], "grades": [None], "total": None}
    ]
    result = compute_averages(students_with_none)
    if result:
        runner.assert_is_instance(result[0]["average"], (int, float), "Average should be number even with None values")

def test_024_string_values_in_scores():
    test_students = [
        {"id": 1, "name": "Test", "age": 20, "scores": [10, "20", 30], "grades": [], "total": 60}
    ]
    result = compute_averages(test_students)
    runner.assert_is_instance(result[0]["average"], (int, float), "Average should be number even with string scores")

def test_025_comprehensive_workflow():
    students = generate_students(10)
    students_with_avg = compute_averages(students)
    result = filter_and_sort(students_with_avg, min_age=18, max_avg=80)
    
    for student in result:
        runner.assert_is_instance(student["name"], str, "Name should be string")
        runner.assert_is_instance(student["age"], int, "Age should be integer")
        runner.assert_is_instance(student["average"], (int, float), "Average should be number")
        for field in ["final_score", "ultimate_score", "super_final"]:
            if field in student:
                runner.assert_is_instance(student[field], (int, float), f"{field} should be number")


all_tests = [
    (test_001_return_type_and_length, "001 - Return type and length"),
    (test_002_dict_structure, "002 - Dictionary structure"),
    (test_003_unique_ids, "003 - Unique IDs"),
    (test_004_return_type_compute_averages, "004 - Return type compute_averages"),
    (test_005_avg_field_exists, "005 - Avg field exists"),
    (test_006_avg_calculation_correctness, "006 - Avg calculation correctness"),
    (test_007_empty_scores_handling, "007 - Empty scores handling"),
    (test_008_return_type_filter_and_sort, "008 - Return type filter_and_sort"),
    (test_009_age_filter, "009 - Age filter"),
    (test_010_avg_filter, "010 - Avg filter"),
    (test_011_sorting_order, "011 - Sorting order"),
    (test_012_data_consistency, "012 - Data consistency"),
    (test_013_edge_cases_empty_list, "013 - Edge cases empty list"),
    (test_014_generate_invalid_input, "014 - Generate invalid input"),
    (test_015_filter_invalid_params, "015 - Filter invalid params"),
    (test_016_field_types_strict, "016 - Field types strict"),
    (test_017_scores_and_grades_content, "017 - Scores and grades content"),
    (test_018_avg_type_validation, "018 - Avg type validation"),
    (test_019_additional_fields_validation, "019 - Additional fields validation"),
    (test_020_strict_age_filter_validation, "020 - Strict age filter validation"),
    (test_021_strict_avg_filter_validation, "021 - Strict avg filter validation"),
    (test_022_additional_fields_types, "022 - Additional fields types"),
    (test_023_compute_with_none_values, "023 - Compute with None values"),
    (test_024_string_values_in_scores, "024 - String values in scores"),
    (test_025_comprehensive_workflow, "025 - Comprehensive workflow"),
]


if __name__ == "__main__":
    print("Запуск 25 тестов для функций работы с данными...")
    print("="*60)
    print("15 тестов должны пройти, 10 тестов должны упасть")
    print("="*60)
    
    for test_func, test_name in all_tests:
        runner.run_test(test_func, test_name)
    
    runner.print_summary()