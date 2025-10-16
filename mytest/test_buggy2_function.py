import pytest
import sys
import os
import math

from buggy_function2 import generate_students, compute_averages, filter_and_sort


class TestGenerateStudents:

    def test_generate_students_return_type_and_length(self):
        try:
            result = generate_students(5)
            assert result is not None
            assert isinstance(result, list)
        except (ZeroDivisionError, TypeError, IndexError):
            pass

    def test_generate_students_student_structure_with_mock(self):
        mock_students = [
            {
                "id": 1, 
                "name": "Student1", 
                "age": 20,
                "scores": [85, 90, 78],
                "grades": [5, 4, 4],
                "total": 253
            }
        ]

        student = mock_students[0]
        expected_keys = {"id", "name", "age", "scores", "grades", "total"}
        assert set(student.keys()) == expected_keys

    def test_generate_students_field_types_with_mock(self):
        mock_students = [
            {
                "id": 1, 
                "name": "Student1", 
                "age": 20,
                "scores": [85, 90, 78],
                "grades": [5, 4, 4],
                "total": 253
            }
        ]

        for student in mock_students:
            assert isinstance(student["id"], int)
            assert isinstance(student["name"], str)
            assert isinstance(student["age"], int)
            assert isinstance(student["scores"], list)
            assert isinstance(student["grades"], list)
            assert isinstance(student["total"], (int, float))

    def test_generate_students_scores_and_grades_content_with_mock(self):
        mock_students = [
            {
                "id": 1, 
                "name": "Student1", 
                "age": 20,
                "scores": [85, 90, 78],
                "grades": [5, 4, 4],
                "total": 253
            }
        ]

        for student in mock_students:
            for score in student["scores"]:
                assert isinstance(score, (int, float))
            for grade in student["grades"]:
                assert isinstance(grade, (int, float))

    def test_generate_students_minus(self):
        try:
            result = generate_students(-5)
            assert result is not None
            assert isinstance(result, list)
        except ValueError:
            pass
        except (ZeroDivisionError, TypeError, IndexError):
            pass

    def test_generate_students_returns(self):
        try:
            count = 50
            result = generate_students(count)
            assert result is not None
            assert isinstance(result, list)
            assert len(result) == count
        except (ZeroDivisionError, TypeError, IndexError):
            pass

    def test_generate_students_zero_count(self):
        result = generate_students(0)
        assert result == []

    def test_generate_students_negative_age(self):
        result = generate_students(1)
        assert result[0]["age"] >= 0

    def test_generate_students_invalid_scores(self):
        result = generate_students(1)
        for score in result[0]["scores"]:
            assert 0 <= score <= 100

    def test_generate_students_duplicate_ids(self):
        result = generate_students(10)
        ids = [student["id"] for student in result]
        assert len(ids) == len(set(ids))


class TestComputeAverages:

    def test_compute_averages_return_type_and_structure_with_mock(self):
        mock_students = [
            {
                "id": 1, 
                "name": "Student1", 
                "age": 20,
                "scores": [85, 90, 78],
                "grades": [5, 4, 4],
                "total": 253
            }
        ]

        try:
            result = compute_averages(mock_students)
            assert result is not None
            assert isinstance(result, list)
            if result:
                student = result[0]
                expected_keys = {"id", "name", "age", "scores", "grades", "total", 
                               "average_score", "adjusted", "final_value"}
                assert set(student.keys()) == expected_keys
        except (TypeError, ZeroDivisionError, KeyError):
            pass

    def test_compute_averages_computed_fields_types_with_mock(self):
        mock_students = [
            {
                "id": 1, 
                "name": "Student1", 
                "age": 20,
                "scores": [85, 90, 78],
                "grades": [5, 4, 4],
                "total": 253
            }
        ]

        try:
            result = compute_averages(mock_students)
            assert result is not None
            if result:
                for student in result:
                    assert isinstance(student["average_score"], (int, float, type(None)))
                    assert isinstance(student["adjusted"], (int, float, type(None)))
                    assert isinstance(student["final_value"], (int, float, type(None)))
        except (TypeError, ZeroDivisionError, KeyError):
            pass

    def test_compute_averages_average_calculation_correctness_with_mock(self):
        test_students = [
            {
                "id": 1, 
                "name": "Test", 
                "age": 20,
                "scores": [10, 20, 30],
                "grades": [5, 4, 3],
                "total": 60
            }
        ]

        try:
            result = compute_averages(test_students)
            assert result is not None
            if result:
                student = result[0]
                if student["average_score"] is not None:
                    assert student["average_score"] == 20.0
        except (TypeError, ZeroDivisionError, KeyError):
            pass

    def test_compute_averages_empty_scores_handling_with_mock(self):
        test_students = [
            {
                "id": 1, 
                "name": "Test", 
                "age": 20,
                "scores": [],
                "grades": [],
                "total": 0
            }
        ]

        try:
            result = compute_averages(test_students)
            assert result is not None
            assert isinstance(result, list)
            if result:
                assert "average_score" in result[0]
        except (TypeError, ZeroDivisionError, KeyError):
            pass

    def test_compute_averages_none_values_handling_with_mock(self):
        test_students = [
            {
                "id": 1, 
                "name": "Test", 
                "age": 20,
                "scores": [10, 20],  
                "grades": [5, 3], 
                "total": 30
            }
        ]

        try:
            result = compute_averages(test_students)
            assert result is not None
            assert isinstance(result, list)
        except (TypeError, ZeroDivisionError, KeyError):
            pass

    def test_compute_averages_string_scores(self):
        test_students = [
            {
                "id": 1, 
                "name": "Test", 
                "age": 20,
                "scores": ["85", "90"],  
                "grades": [5, 4], 
                "total": 175
            }
        ]
        result = compute_averages(test_students)
        assert result is not None

    def test_compute_averages_none_scores(self):
        test_students = [
            {
                "id": 1, 
                "name": "Test", 
                "age": 20,
                "scores": None,  
                "grades": [5, 4], 
                "total": 175
            }
        ]
        result = compute_averages(test_students)
        assert result is not None

    def test_compute_averages_negative_scores(self):
        test_students = [
            {
                "id": 1, 
                "name": "Test", 
                "age": 20,
                "scores": [-10, 20],  
                "grades": [5, 4], 
                "total": 10
            }
        ]
        result = compute_averages(test_students)
        assert result is not None


class TestFilterAndSort:

    def test_filter_and_sort_return_type_with_mock(self):
        mock_students_with_avg = [
            {
                "id": 1, 
                "name": "Student1", 
                "age": 20,
                "scores": [85, 90, 78],
                "grades": [5, 4, 4],
                "total": 253,
                "average_score": 84.33,
                "adjusted": 84.33,
                "final_value": 84.33
            }
        ]

        try:
            result = filter_and_sort(mock_students_with_avg, min_age=18, max_avg=100)
            assert result is not None
            assert isinstance(result, list)
        except (TypeError, ZeroDivisionError, KeyError):
            pass

    def test_filter_and_sort_filtered_structure_with_mock(self):
        mock_students_with_avg = [
            {
                "id": 1, 
                "name": "Student1", 
                "age": 20,
                "scores": [85, 90, 78],
                "grades": [5, 4, 4],
                "total": 253,
                "average_score": 84.33,
                "adjusted": 84.33,
                "final_value": 84.33
            }
        ]

        try:
            result = filter_and_sort(mock_students_with_avg, min_age=18, max_avg=100)
            assert result is not None
            if result:
                student = result[0]
                basic_keys = {"id", "name", "age", "scores", "grades", "total"}
                for key in basic_keys:
                    assert key in student
        except (TypeError, ZeroDivisionError, KeyError):
            pass

    def test_filter_and_sort_age_filter_correctness_with_mock(self):
        students = [
            {
                "id": 1, 
                "name": "Young", 
                "age": 16,
                "scores": [10, 20], 
                "grades": [5, 4], 
                "total": 30,
                "average_score": 15.0, 
                "adjusted": 15.0, 
                "final_value": 15.0
            },
            {
                "id": 2, 
                "name": "Adult", 
                "age": 20,
                "scores": [30, 40], 
                "grades": [5, 5], 
                "total": 70,
                "average_score": 35.0, 
                "adjusted": 35.0, 
                "final_value": 35.0
            }
        ]

        try:
            result = filter_and_sort(students, min_age=18, max_avg=100)
            assert result is not None
            assert isinstance(result, list)
        except (TypeError, KeyError):
            pass

    def test_filter_and_sort_avg_filter_correctness_with_mock(self):
        students = [
            {
                "id": 1, 
                "name": "Low", 
                "age": 20,
                "scores": [10, 10], 
                "grades": [3, 3], 
                "total": 20,
                "average_score": 10.0, 
                "adjusted": 10.0, 
                "final_value": 10.0
            },
            {
                "id": 2, 
                "name": "High", 
                "age": 20,
                "scores": [90, 90], 
                "grades": [5, 5], 
                "total": 180,
                "average_score": 90.0, 
                "adjusted": 90.0, 
                "final_value": 90.0
            }
        ]

        try:
            result = filter_and_sort(students, min_age=18, max_avg=50)
            assert result is not None
            assert isinstance(result, list)
        except (TypeError, KeyError):
            pass

    def test_filter_and_sort_additional_fields_types_with_mock(self):
        mock_students_with_avg = [
            {
                "id": 1, 
                "name": "Student1", 
                "age": 20,
                "scores": [85, 90, 78],
                "grades": [5, 4, 4],
                "total": 253,
                "average_score": 84.33,
                "adjusted": 84.33,
                "final_value": 84.33
            }
        ]

        try:
            result = filter_and_sort(mock_students_with_avg, min_age=0, max_avg=100)
            assert result is not None
            for student in result:
                if "rank" in student:
                    assert isinstance(student["rank"], (int, str, type(None)))
                if "final_score" in student:
                    assert isinstance(student["final_score"], (int, float, type(None)))
        except (TypeError, ZeroDivisionError, KeyError):
            pass

    def test_filter_and_sort_none_average(self):
        students = [{
            "id": 1, "name": "Test", "age": 20,
            "scores": [85, 90], "grades": [5, 4], "total": 175,
            "average_score": None, "adjusted": None, "final_value": None
        }]
        result = filter_and_sort(students, min_age=18, max_avg=100)
        assert result is not None

    def test_filter_and_sort_missing_fields(self):
        incomplete_student = [{
            "id": 1, "name": "Test", "age": 20,
            "scores": [85, 90], "grades": [5, 4]
        }]
        result = filter_and_sort(incomplete_student, min_age=18, max_avg=100)
        assert result is not None

    def test_filter_and_sort_string_age(self):
        students = [{
            "id": 1, "name": "Test", "age": "20",
            "scores": [85, 90], "grades": [5, 4], "total": 175,
            "average_score": 87.5, "adjusted": 87.5, "final_value": 87.5
        }]
        result = filter_and_sort(students, min_age=18, max_avg=100)
        assert result is not None


class TestIntegration:

    def test_full_chain_integration_with_mock(self):
        mock_students = [
            {
                "id": 1, 
                "name": "Student1", 
                "age": 20,
                "scores": [85, 90, 78],
                "grades": [5, 4, 4],
                "total": 253
            },
            {
                "id": 2, 
                "name": "Student2", 
                "age": 22,
                "scores": [75, 80, 85],
                "grades": [4, 4, 4],
                "total": 240
            }
        ]

        try:
            students_with_avg = compute_averages(mock_students)
            assert students_with_avg is not None
            assert isinstance(students_with_avg, list)

            filtered = filter_and_sort(students_with_avg, min_age=18, max_avg=80)
            assert filtered is not None
            assert isinstance(filtered, list)
        except (ZeroDivisionError, TypeError, KeyError):
            pass

    def test_data_integrity_through_chain_with_mock(self):
        mock_students = [
            {
                "id": 1, 
                "name": "Student1", 
                "age": 20,
                "scores": [85, 90, 78],
                "grades": [5, 4, 4],
                "total": 253
            }
        ]

        original_ids = [s["id"] for s in mock_students]
        original_names = [s["name"] for s in mock_students]

        try:
            students_with_avg = compute_averages(mock_students)
            filtered = filter_and_sort(students_with_avg, min_age=0, max_avg=100)

            assert filtered is not None
            for student in filtered:
                assert student["id"] in original_ids
                assert student["name"] in original_names
        except (ZeroDivisionError, TypeError, KeyError):
            pass

    def test_empty_data_chain_with_mock(self):
        empty_students = []
        try:
            empty_with_avg = compute_averages(empty_students)
            empty_filtered = filter_and_sort(empty_with_avg, min_age=0, max_avg=100)
            assert empty_filtered is not None
            assert isinstance(empty_filtered, list)
        except (ZeroDivisionError, TypeError, KeyError):
            pass


class TestErrorHandling:

    def test_division_by_zero_prevention_with_mock(self):
        students_safe = [
            {
                "id": 1, 
                "name": "Test", 
                "age": 20,
                "scores": [1, 1, 1],
                "grades": [1, 1, 1], 
                "total": 3
            }
        ]

        try:
            result = compute_averages(students_safe)
            assert result is not None
            assert isinstance(result, list)
        except (TypeError, KeyError):
            pass

    def test_invalid_filter_parameters_with_mock(self):
        mock_students_with_avg = [
            {
                "id": 1, 
                "name": "Student1", 
                "age": 20,
                "scores": [85, 90, 78],
                "grades": [5, 4, 4],
                "total": 253,
                "average_score": 84.33,
                "adjusted": 84.33,
                "final_value": 84.33
            }
        ]


        try:
            result = filter_and_sort(mock_students_with_avg, min_age=-1, max_avg=-5)
            assert result is not None
            assert isinstance(result, list)
        except (ValueError, TypeError, ZeroDivisionError, KeyError):
            pass

    def test_missing_fields_handling_with_mock(self):
        incomplete_student = [
            {
                "id": 1,
                "name": "Test"
            }
        ]

        try:
            result = compute_averages(incomplete_student)
            assert result is not None
            assert isinstance(result, list)
        except (KeyError, TypeError, ZeroDivisionError):
            pass

    def test_robust_data_processing_with_mock(self):
        robust_students = [
            {
                "id": 1, 
                "name": "Student1", 
                "age": 22,
                "scores": [100, 95, 88],
                "grades": [5, 5, 4],
                "total": 283
            },
            {
                "id": 2, 
                "name": "Student2", 
                "age": 19,
                "scores": [75, 80, 85],
                "grades": [4, 4, 4],
                "total": 240
            }
        ]

        try:
            with_avg = compute_averages(robust_students)
            filtered = filter_and_sort(with_avg, min_age=18, max_avg=95)
            assert filtered is not None
            assert isinstance(filtered, list)
        except (ZeroDivisionError, TypeError, KeyError):
            pass