import pytest
import random
from data_functions import generate_students, compute_averages, filter_and_sort


class TestGenerateStudents:
    
    def test_return_type(self):
        result = generate_students(5)
        assert isinstance(result, list)
    
    def test_list_length(self):
        n = 10
        result = generate_students(n)
        assert len(result) == n
    
    def test_student_structure(self):
        for _ in range(3):
            result = generate_students(1)
            if result:  
                student = result[0]
                expected_keys = {"id", "name", "age", "scores", "grades", "total"}
                assert set(student.keys()) == expected_keys
    
    def test_id_type_and_uniqueness(self):
        result = generate_students(5)
        ids = []
        for student in result:
            id_val = student["id"]
            ids.append(id_val)
            assert isinstance(id_val, int)
        
        assert len(ids) == len(set(ids))
    
    def test_name_type(self):
        result = generate_students(3)
        for student in result:
            name = student["name"]
            assert isinstance(name, str)
    
    def test_age_type_and_range(self):
        result = generate_students(5)
        for student in result:
            age = student["age"]
            assert isinstance(age, int)
            assert 17 <= age <= 25
    
    def test_scores_type_and_content(self):
        result = generate_students(3)
        for student in result:
            scores = student["scores"]
            assert isinstance(scores, list)
            for score in scores:
                assert isinstance(score, (int, float))
    
    def test_grades_type_and_content(self):
        result = generate_students(3)
        for student in result:
            grades = student["grades"]
            assert isinstance(grades, list)
            for grade in grades:
                assert isinstance(grade, (int, float))
    
    def test_total_type(self):
        result = generate_students(3)
        for student in result:
            total = student["total"]
            assert isinstance(total, (int, float))


class TestComputeAverages:
    
    def test_return_type(self):
        students = generate_students(3)
        result = compute_averages(students)
        assert isinstance(result, list)
    
    def test_structure_preserved(self):
        students = generate_students(3)
        result = compute_averages(students)
        
        assert len(result) == len(students)
        if students:
            original_keys = set(students[0].keys())
            for student in result:
                assert original_keys.issubset(set(student.keys()))
    
    def test_new_fields_added(self):
        students = generate_students(3)
        result = compute_averages(students)
        
        if result:
            student = result[0]
            new_fields = {"average", "adjusted", "final_value"}
            assert new_fields.issubset(set(student.keys()))
    
    def test_average_type(self):
        students = generate_students(3)
        result = compute_averages(students)
        
        for student in result:
            average = student["average"]
            assert isinstance(average, (int, float))
    
    def test_adjusted_type(self):
        students = generate_students(3)
        result = compute_averages(students)
        
        for student in result:
            adjusted = student["adjusted"]
            assert isinstance(adjusted, (int, float))
    
    def test_final_value_type(self):
        students = generate_students(3)
        result = compute_averages(students)
        
        for student in result:
            final_value = student["final_value"]
            assert isinstance(final_value, (int, float))


class TestFilterAndSort:
    
    def test_return_type(self):
        students = generate_students(5)
        students_with_avg = compute_averages(students)
        result = filter_and_sort(students_with_avg, 18, 90.0)
        assert isinstance(result, list)
    
    def test_filtering_by_age(self):
        students = [
            {"id": 1, "name": "A", "age": 17, "scores": [80], "grades": [4], "total": 80, "average": 80.0, "adjusted": 80.0, "final_value": 80.0},
            {"id": 2, "name": "B", "age": 18, "scores": [85], "grades": [4], "total": 85, "average": 85.0, "adjusted": 85.0, "final_value": 85.0},
            {"id": 3, "name": "C", "age": 19, "scores": [90], "grades": [5], "total": 90, "average": 90.0, "adjusted": 90.0, "final_value": 90.0},
        ]
        
        result = filter_and_sort(students, 18, 100.0)
        ages = [student["age"] for student in result]
        assert all(age >= 18 for age in ages)
    
    def test_filtering_by_average(self):
        students = [
            {"id": 1, "name": "A", "age": 20, "scores": [70], "grades": [3], "total": 70, "average": 70.0, "adjusted": 70.0, "final_value": 70.0},
            {"id": 2, "name": "B", "age": 20, "scores": [80], "grades": [4], "total": 80, "average": 80.0, "adjusted": 80.0, "final_value": 80.0},
            {"id": 3, "name": "C", "age": 20, "scores": [90], "grades": [5], "total": 90, "average": 90.0, "adjusted": 90.0, "final_value": 90.0},
        ]
        
        result = filter_and_sort(students, 18, 85.0)
        averages = [student["average"] for student in result]
        assert all(avg <= 85.0 for avg in averages)
    
    def test_new_fields_presence(self):
        students = generate_students(3)
        students_with_avg = compute_averages(students)
        result = filter_and_sort(students_with_avg, 18, 90.0)
        
        if result:
            student = result[0]
            expected_fields = {"rank", "final_score", "ultimate_score", "super_final"}
            assert expected_fields.issubset(set(student.keys()))
    
    def test_rank_type_and_values(self):
        students = generate_students(5)
        students_with_avg = compute_averages(students)
        result = filter_and_sort(students_with_avg, 18, 100.0)
        
        for student in result:
            rank = student["rank"]
            assert isinstance(rank, int)
            assert rank >= 1
    
    def test_final_score_type(self):
        students = generate_students(3)
        students_with_avg = compute_averages(students)
        result = filter_and_sort(students_with_avg, 18, 100.0)
        
        for student in result:
            assert isinstance(student["final_score"], (int, float))
    
    def test_ultimate_score_type(self):
        students = generate_students(3)
        students_with_avg = compute_averages(students)
        result = filter_and_sort(students_with_avg, 18, 100.0)
        
        for student in result:
            assert isinstance(student["ultimate_score"], (int, float))
    
    def test_super_final_type(self):
        students = generate_students(3)
        students_with_avg = compute_averages(students)
        result = filter_and_sort(students_with_avg, 18, 100.0)
        
        for student in result:
            assert isinstance(student["super_final"], (int, float))


class TestIntegration:
    
    def test_full_workflow(self):
        students = generate_students(10)
        assert len(students) == 10
        
        students_with_avg = compute_averages(students)
        assert len(students_with_avg) == 10
        
        filtered_students = filter_and_sort(students_with_avg, 18, 85.0)
        assert isinstance(filtered_students, list)
    
    def test_data_types_throughout_workflow(self):
        students = generate_students(5)
        
        for student in students:
            assert isinstance(student["id"], (int, str))  
            assert isinstance(student["name"], str)
            assert isinstance(student["age"], (int, str, type(None)))  
            assert isinstance(student["scores"], list)
            assert isinstance(student["grades"], list)
            assert isinstance(student["total"], (int, float, str))  


class TestEdgeCases:
    
    def test_generate_zero_students(self):
        result = generate_students(0)
        assert isinstance(result, list)
        assert len(result) == 0
    
    def test_compute_averages_empty_list(self):
        result = compute_averages([])
        assert isinstance(result, list)
        assert len(result) == 0
    
    def test_filter_and_sort_empty_list(self):
        result = filter_and_sort([], 18, 85.0)
        assert isinstance(result, list)
        assert len(result) == 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])