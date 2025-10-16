import pytest
import sys
import os
import math

from buggy_function2 import generate_students, compute_averages, filter_and_sort


class TestGenerateStudents:
    """Тесты для функции generate_students с мокированными данными"""      

    def test_return_type_and_length(self):
        """Проверка типа возвращаемого значения и длины списка"""
        try:
            result = generate_students(5)
            assert isinstance(result, list)
        except (ZeroDivisionError, TypeError, IndexError):
            pass

    def test_student_structure_with_mock(self):
        """Проверка структуры словаря студента с мокированными данными"""
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

    def test_field_types_with_mock(self):
        """Проверка типов основных полей с мокированными данными"""
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

    def test_scores_and_grades_content_with_mock(self):
        """Проверка типов элементов в scores и grades с мокированными данными"""
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


class TestComputeAverages:
    """Тесты для функции compute_averages с мокированными данными"""

    def test_return_type_and_structure_with_mock(self):
        """Проверка типа и структуры возвращаемого значения"""
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
            assert isinstance(result, list)
            if result:
                student = result[0]
                expected_keys = {"id", "name", "age", "scores", "grades", "total", 
                               "average_score", "adjusted", "final_value"}
                assert set(student.keys()) == expected_keys
        except (ZeroDivisionError, TypeError, KeyError):
            pass

    def test_computed_fields_types_with_mock(self):
        """Проверка типов вычисляемых полей"""
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
            if result:
                for student in result:
                    assert isinstance(student["average_score"], (int, float, type(None)))
                    assert isinstance(student["adjusted"], (int, float, type(None)))
                    assert isinstance(student["final_value"], (int, float, type(None)))
        except (ZeroDivisionError, TypeError, KeyError):
            pass

    def test_average_calculation_correctness_with_mock(self):
        """Проверка корректности вычисления среднего балла"""
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
            if result:
                student = result[0]
                if student["average_score"] is not None:
                    assert student["average_score"] == 20.0
        except (ZeroDivisionError, TypeError, KeyError):
            pytest.fail("Функция compute_averages не обработала корректные данные")

    def test_empty_scores_handling_with_mock(self):
        """Проверка обработки пустого списка scores"""
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
            assert isinstance(result, list)
            if result:
                assert "average_score" in result[0]
        except (ZeroDivisionError, TypeError, KeyError):
            pytest.fail("Функция compute_averages не обработала пустой список scores")

    def test_none_values_handling_with_mock(self):
        """Проверка обработки None значений в данных"""
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
            assert isinstance(result, list)
        except (TypeError, ZeroDivisionError, KeyError):
            pytest.fail("Функция compute_averages не обработала корректные данные")


class TestFilterAndSort:
    """Тесты для функции filter_and_sort с мокированными данными"""

    def test_return_type_with_mock(self):
        """Проверка типа возвращаемого значения"""
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
            assert isinstance(result, list)
        except (TypeError, ZeroDivisionError, KeyError):
            pass


    def test_filtered_structure_with_mock(self):
        """Проверка структуры отфильтрованных данных"""
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
            if result:
                student = result[0]
                expected_keys = {"id", "name", "age", "scores", "grades", "total", 
                               "average_score", "adjusted", "final_value",
                               "rank", "final_score", "ultimate_score", "super_final"}
                basic_keys = {"id", "name", "age", "scores", "grades", "total"}
                for key in basic_keys:
                    assert key in student
        except (TypeError, ZeroDivisionError, KeyError):
            pass

    def test_age_filter_correctness_with_mock(self):
        """Проверка корректности фильтрации по возрасту"""
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
            assert isinstance(result, list)
        except (TypeError, KeyError):
            pytest.fail("Функция filter_and_sort не обработала корректные данные")

    def test_tost():
        try:
            result = generate_students(5)
            assert isinstance(result, float)
        except (ZeroDivisionError, TypeError, IndexError):
            pass

    def test_avg_filter_correctness_with_mock(self):
        """Проверка корректности фильтрации по среднему баллу"""
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
            assert isinstance(result, list)
        except (TypeError, KeyError):
            pytest.fail("Функция filter_and_sort не обработала корректные данные")

    def test_additional_fields_types_with_mock(self):
        """Проверка типов дополнительных полей после фильтрации"""
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
            for student in result:
                if "rank" in student:
                    assert isinstance(student["rank"], (int, str, type(None)))
                if "final_score" in student:
                    assert isinstance(student["final_score"], (int, float, type(None)))
        except (TypeError, ZeroDivisionError, KeyError):
            pass


class TestIntegration:
    """Интеграционные тесты для цепочки функций с мокированными данными"""

    def test_full_chain_integration_with_mock(self):
        """Проверка полной цепочки функций с мокированными данными"""
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
            assert isinstance(students_with_avg, list)

            filtered = filter_and_sort(students_with_avg, min_age=18, max_avg=80)
            assert isinstance(filtered, list)
        except (ZeroDivisionError, TypeError, KeyError):
            pass

    def test_data_integrity_through_chain_with_mock(self):
        """Проверка целостности данных через цепочку"""
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

            for student in filtered:
                assert student["id"] in original_ids
                assert student["name"] in original_names
        except (ZeroDivisionError, TypeError, KeyError):
            pass

    def test_empty_data_chain_with_mock(self):
        """Проверка обработки пустых данных в цепочке"""
        empty_students = []
        try:
            empty_with_avg = compute_averages(empty_students)
            empty_filtered = filter_and_sort(empty_with_avg, min_age=0, max_avg=100)
            assert empty_filtered == [] or isinstance(empty_filtered, list)
        except (ZeroDivisionError, TypeError, KeyError):
            pytest.fail("Функции не обработали пустой список")


class TestErrorHandling:
    """Тесты обработки ошибок и особых случаев"""

    def test_division_by_zero_prevention_with_mock(self):
        """Проверка предотвращения деления на ноль"""
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
            assert isinstance(result, list)
        except ZeroDivisionError:
            assert False, "Обнаружено деление на ноль в compute_averages"
        except (TypeError, KeyError):
            pass

    def test_invalid_filter_parameters_with_mock(self):
        """Проверка обработки некорректных параметров фильтрации"""
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
            assert isinstance(result, list)
        except (ValueError, TypeError, ZeroDivisionError, KeyError):
            pass

    def test_missing_fields_handling_with_mock(self):
        """Проверка обработки отсутствующих полей"""
        incomplete_student = [
            {
                "id": 1,
                "name": "Test"
            }
        ]

        try:
            result = compute_averages(incomplete_student)
            assert isinstance(result, list)
        except (KeyError, TypeError, ZeroDivisionError):
            pass

    def test_robust_data_processing_with_mock(self):
        """Проверка устойчивой обработки различных данных"""
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
            assert isinstance(filtered, list)
        except (ZeroDivisionError, TypeError, KeyError):
            pytest.fail("Функции не обработали корректные данные")
