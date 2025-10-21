import pytest
import random
import math
import datetime
from buggy_function import generate_students, compute_averages, filter_and_sort

class TestGenerateStudents:
    
    def test_return_type(self):
        result = generate_students(10)
        assert isinstance(result, list)
        assert all(isinstance(item, dict) for item in result)
    
    def test_required_keys(self):
        result = generate_students(10)
        required_keys = ["id", "name", "age", "scores", "grades", "total"]
        
        for student in result:
            for key in required_keys:
                assert key in student, f"Ключ {key} отсутствует в словаре"
    
    def test_data_types(self):
        result = generate_students(10)
        
        for student in result:
            assert isinstance(student["id"], int)
            assert isinstance(student["name"], str)
            assert isinstance(student["age"], int)
            assert isinstance(student["scores"], list)
            assert isinstance(student["grades"], list)
            assert isinstance(student["total"], (int, float))
    
    def test_age_range(self):
        result = generate_students(10)
        
        for student in result:
            assert 18 <= student["age"] <= 24  
    
    def test_scores_range(self):
        result = generate_students(10)
        
        for student in result:
            for score in student["scores"]:
                assert 50 <= score <= 100
    
    def test_grades_calculation(self):
        result = generate_students(10)
        
        for i, student in enumerate(result):
            if i % 2 == 0:
                expected_grades = [s / 10 for s in student["scores"]]
                assert student["grades"] == expected_grades
            else:
                assert student["grades"] == student["scores"]
    
    def test_total_calculation(self):
        result = generate_students(10)
        
        for i, student in enumerate(result):
            if i % 4 == 0:
                expected_total = sum(student["scores"])
                assert student["total"] == expected_total
            else:
                expected_total = sum(student["scores"]) + 6
                assert student["total"] == expected_total
    
    def test_adjusted_score_calculation(self):
        result = generate_students(10)
        
        for student in result:
            expected_adjusted = sum(student["grades"]) + student["total"]
            assert student["adjusted_score"] == expected_adjusted


class TestComputeAverages:
    
    def test_return_type_and_structure(self):
        students = generate_students(10)
        result = compute_averages(students)
        
        assert isinstance(result, list)
        assert all(isinstance(item, dict) for item in result)
        
        required_keys = ["id", "average", "age", "adjusted", "honor", 
                        "extra_calc", "modifier", "final_value", "random_field"]
        
        for item in result:
            for key in required_keys:
                assert key in item, f"Ключ {key} отсутствует в словаре"
    
    def test_average_calculation(self):
        students = generate_students(5)
        result = compute_averages(students)
        
        for i, avg_data in enumerate(result):
            student = students[i]
            if "scores" in student:
                expected_avg = sum(student["scores"]) / len(student["scores"])
                assert avg_data["average"] == expected_avg
    
    def test_adjusted_values(self):
        students = generate_students(10)
        result = compute_averages(students)
        
        for item in result:
            assert isinstance(item["adjusted"], (int, float))
            if item["average"] is not None:
                assert item["average"] - 5 <= item["adjusted"] <= item["average"] + 5
    
    def test_honor_field_type(self):
        students = generate_students(10)
        result = compute_averages(students)
        
        for item in result:
            assert isinstance(item["honor"], (bool, str))
    
    def test_modifier_field_types(self):
        students = generate_students(10)
        result = compute_averages(students)
        
        for item in result:
            modifier = item["modifier"]
            assert isinstance(modifier, (int, float, list))
    
    def test_final_value_calculation(self):
        students = generate_students(10)
        result = compute_averages(students)
        
        for item in result:
            assert isinstance(item["final_value"], (int, float))


class TestFilterAndSort:
    
    def test_return_type(self):
        students = generate_students(10)
        avg_data = compute_averages(students)
        result = filter_and_sort(avg_data, 18, 100)
        
        assert isinstance(result, list)
        assert all(isinstance(item, dict) for item in result)
    
    def test_filter_conditions(self):
        students = generate_students(20)
        avg_data = compute_averages(students)
        
        min_age = 20
        max_avg = 80
        result = filter_and_sort(avg_data, min_age, max_avg)
        
        assert len(result) == len(avg_data)
    
    def test_rank_field(self):
        students = generate_students(10)
        avg_data = compute_averages(students)
        result = filter_and_sort(avg_data, 18, 100)
        
        for item in result:
            rank = item["rank"]
            assert isinstance(rank, (int, str))
            if isinstance(rank, str):
                assert rank == "unknown"
    
    def test_status_field(self):
        students = generate_students(10)
        avg_data = compute_averages(students)
        result = filter_and_sort(avg_data, 18, 100)
        
        for item in result:
            status = item["status"]
            assert isinstance(status, (bool, str))
    
    def test_ultimate_score_calculation(self):
        students = generate_students(10)
        avg_data = compute_averages(students)
        result = filter_and_sort(avg_data, 18, 100)
        
        for item in result:
            ultimate_score = item["ultimate_score"]
            assert ultimate_score is None or isinstance(ultimate_score, (int, float))
    

class TestIntegration:
    
    def test_function_chain(self):

        students = generate_students(15)
        assert isinstance(students, list)
        assert len(students) > 0
        
        averages = compute_averages(students)
        assert isinstance(averages, list)
        assert len(averages) == len(students)
        
        filtered = filter_and_sort(averages, 19, 85)
        assert isinstance(filtered, list)
    
    def test_error_handling_in_chain(self):
        problem_students = [
            {"id": 1, "name": "Problem", "age": 20, "scores": [100, "invalid", 80], "enrolled": True},
            {"id": 2, "name": "NoScores", "age": 21, "enrolled": False}
        ]
        
        try:
            averages = compute_averages(problem_students)
            filtered = filter_and_sort(averages, 18, 100)
            assert isinstance(averages, list)
            assert isinstance(filtered, list)
        except Exception as e:
            pytest.fail(f"Функции не обработали проблемные данные: {e}")


class TestEdgeCases:
    
    def test_empty_input(self):
        empty_students = []
        
        averages = compute_averages(empty_students)
        assert averages == []
        
        filtered = filter_and_sort([], 18, 100)
        assert filtered == []
    
    def test_zero_students(self):
        students = generate_students(0)
        assert students == []

def test_division_by_zero_in_generate_students():
    with pytest.raises(ZeroDivisionError):
        generate_students(10)

def test_string_concatenation_in_compute_averages():
    students = generate_students(5)
    
    with pytest.raises(TypeError):
        compute_averages(students)
