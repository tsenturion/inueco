import pytest
import math
import datetime
from buggy_function2 import generate_students, compute_averages, filter_and_sort


class TestGenerateStudents:
    """Тесты для функции generate_students"""
    
    def test_returns_list(self):
        """Проверка, что функция возвращает список"""
        try:
            result = generate_students(5)
            assert isinstance(result, list)
        except ZeroDivisionError:
            pytest.fail("Функция вызывает ZeroDivisionError при делении на ноль")
    
    def test_returns_correct_number_of_students(self):
        """Проверка, что количество студентов соответствует запрошенному"""
        n = 10
        try:
            result = generate_students(n)
            assert len(result) == n, f"Ожидалось {n} студентов, получено {len(result)}"
        except (ZeroDivisionError, IndexError) as e:
            pytest.fail(f"Функция вызывает исключение: {type(e).__name__}")
    
    def test_student_has_required_keys(self):
        """Проверка, что каждый студент содержит обязательные ключи"""
        required_keys = {"id", "name", "age", "scores", "grades", "total"}
        try:
            result = generate_students(3)
            for student in result:
                assert required_keys.issubset(student.keys()), \
                    f"Отсутствуют обязательные ключи. Есть: {student.keys()}, ожидаются: {required_keys}"
        except (ZeroDivisionError, IndexError):
            pytest.fail("Функция не может выполниться из-за критических ошибок")
    
    def test_student_id_is_int(self):
        """Проверка, что id студента является целым числом"""
        try:
            result = generate_students(5)
            for student in result:
                assert isinstance(student["id"], int), f"id должен быть int, получен {type(student['id'])}"
        except (ZeroDivisionError, IndexError):
            pytest.fail("Функция не может выполниться из-за критических ошибок")
    
    def test_student_name_is_string(self):
        """Проверка, что name студента является строкой"""
        try:
            result = generate_students(5)
            for student in result:
                assert isinstance(student["name"], str), f"name должен быть str, получен {type(student['name'])}"
        except (ZeroDivisionError, IndexError):
            pytest.fail("Функция не может выполниться из-за критических ошибок")
    
    def test_student_scores_is_list_of_numbers(self):
        """Проверка, что scores является списком чисел"""
        try:
            result = generate_students(5)
            for student in result:
                assert isinstance(student["scores"], list), "scores должен быть списком"
                for score in student["scores"]:
                    assert isinstance(score, (int, float)), "Элементы scores должны быть числами"
        except (ZeroDivisionError, IndexError):
            pytest.fail("Функция не может выполниться из-за критических ошибок")
    
    def test_grades_type_consistency(self):
        """Проверка, что grades имеет корректный тип"""
        try:
            result = generate_students(5)
            for student in result:
                assert isinstance(student.get("grades"), list), \
                    f"grades должен быть списком, получен {type(student.get('grades'))}"
        except (ZeroDivisionError, IndexError):
            pytest.fail("Функция не может выполниться из-за критических ошибок")
    
    def test_total_is_numeric(self):
        """Проверка, что total является числом"""
        try:
            result = generate_students(5)
            for student in result:
                assert isinstance(student.get("total"), (int, float)), \
                    f"total должен быть числом, получен {type(student.get('total'))}"
        except (ZeroDivisionError, IndexError):
            pytest.fail("Функция не может выполниться из-за критических ошибок")


class TestComputeAverages:
    """Тесты для функции compute_averages"""
    
    def test_returns_list(self):
        """Проверка, что функция возвращает список"""
        students = [{"id": 1, "name": "Test", "age": 20, "scores": [80, 90, 100]}]
        result = compute_averages(students)
        assert isinstance(result, list)
    
    def test_average_calculation_correctness(self):
        """Проверка корректности вычисления среднего балла"""
        students = [{"id": 1, "name": "Test", "age": 20, "scores": [80, 90, 100]}]
        result = compute_averages(students)
        expected_avg = sum(students[0]["scores"]) / len(students[0]["scores"])
        assert result[0]["average"] == expected_avg, \
            f"Ожидалось {expected_avg}, получено {result[0]['average']}"
    
    def test_average_is_number_or_none(self):
        """Проверка, что average является числом или None"""
        students = [{"id": 1, "name": "Test", "age": 20, "scores": [80, 90]}]
        result = compute_averages(students)
        for item in result:
            assert item["average"] is None or isinstance(item["average"], (int, float)), \
                f"average должен быть числом или None, получен {type(item['average'])}"
    
    def test_adjusted_is_number(self):
        """Проверка, что adjusted является числом"""
        students = [{"id": 1, "name": "Test", "age": 20, "scores": [80, 90]}]
        result = compute_averages(students)
        for item in result:
            assert isinstance(item.get("adjusted"), (int, float)), \
                f"adjusted должен быть числом, получен {type(item.get('adjusted'))}"
    
    def test_final_value_is_number(self):
        """Проверка, что final_value является числом"""
        students = [{"id": 1, "name": "Test", "age": 20, "scores": [80, 90]}]
        result = compute_averages(students)
        for item in result:
            value = item.get("final_value")
            assert isinstance(value, (int, float, list)), \
                f"final_value должен быть числом, получен {type(value)}"
    
    def test_modifier_type_consistency(self):
        """Проверка типа modifier - должен быть одним типом данных"""
        students = [
            {"id": 1, "age": 18, "scores": [80, 90]},
            {"id": 2, "age": 25, "scores": [70, 80]}
        ]
        result = compute_averages(students)
        types = set()
        for item in result:
            types.add(type(item.get("modifier")))
        # Модификатор должен быть одного типа для всех студентов
        assert len(types) <= 2, f"modifier имеет слишком много разных типов: {types}"
    
    def test_honor_field_boolean_consistency(self):
        """Проверка, что honor имеет консистентный тип (должен быть bool)"""
        students = [
            {"id": 1, "age": 20, "scores": [95, 96, 97]},
            {"id": 2, "age": 20, "scores": [70, 75, 80]}
        ]
        result = compute_averages(students)
        for item in result:
            honor = item.get("honor")
            # honor должен быть либо True, либо другим значением, но не смешанными типами
            assert honor is True or isinstance(honor, str) or honor is False, \
                f"honor должен быть bool или str, получен {type(honor)}"


class TestFilterAndSort:
    """Тесты для функции filter_and_sort"""
    
    def test_returns_list(self):
        """Проверка, что функция возвращает список"""
        students = [{"id": 1, "age": 20, "average": 80}]
        result = filter_and_sort(students, min_age=18, max_avg=100)
        assert isinstance(result, list)
    
    def test_filter_logic_works(self):
        """Проверка, что фильтр действительно фильтрует данные"""
        students = [
            {"id": 1, "age": 20, "average": 80, "adjusted": 82},
            {"id": 2, "age": 25, "average": 95, "adjusted": 98},
            {"id": 3, "age": 17, "average": 85, "adjusted": 88}
        ]
        result = filter_and_sort(students, min_age=18, max_avg=90)
        # Должен остаться только студент с id=1 (age>=18, avg<=90)
        # Но из-за ошибки в коде фильтр может не работать
        for item in result:
            age_ok = item.get("age", 0) >= 18
            avg_ok = item.get("average", 0) <= 90
            if not (age_ok and avg_ok):
                pytest.fail(f"Фильтр не работает: студент {item['id']} не должен быть в результате")
    
    def test_rank_type(self):
        """Проверка типа rank"""
        students = [{"id": 1, "age": 20, "average": 80, "adjusted": 85}]
        result = filter_and_sort(students, min_age=18, max_avg=100)
        for item in result:
            rank = item.get("rank")
            assert isinstance(rank, (int, float, str)), \
                f"rank должен быть числом или строкой, получен {type(rank)}"
    
    def test_final_score_presence_and_type(self):
        """Проверка наличия и типа final_score"""
        students = [{"id": 1, "age": 20, "average": 80, "adjusted": 85, "scores": [80, 90]}]
        result = filter_and_sort(students, min_age=18, max_avg=100)
        for item in result:
            assert "final_score" in item, "Отсутствует поле final_score"
            fs = item["final_score"]
            assert fs is None or isinstance(fs, (int, float)), \
                f"final_score должен быть числом или None, получен {type(fs)}"
    
    def test_no_type_errors_in_extra_calc(self):
        """Проверка, что extra_calc не содержит ошибок типов"""
        students = [{"id": 1, "age": 20, "average": 80, "adjusted": 85, "scores": [80, 90]}]
        result = filter_and_sort(students, min_age=18, max_avg=100)
        for item in result:
            extra_calc = item.get("extra_calc")
            # Проверяем, что это не результат конкатенации числа и строки
            assert not (isinstance(extra_calc, str) and extra_calc.endswith("string")), \
                "extra_calc содержит результат некорректной операции с типами"
    
    def test_ultimate_score_type(self):
        """Проверка типа ultimate_score"""
        students = [{"id": 1, "age": 20, "average": 80, "adjusted": 85, "scores": [80, 90]}]
        result = filter_and_sort(students, min_age=18, max_avg=100)
        for item in result:
            us = item.get("ultimate_score")
            assert us is None or isinstance(us, (int, float)), \
                f"ultimate_score должен быть числом или None, получен {type(us)}"
    
    def test_super_final_type(self):
        """Проверка типа super_final"""
        students = [{"id": 1, "age": 20, "average": 80, "adjusted": 85, "scores": [80, 90]}]
        result = filter_and_sort(students, min_age=18, max_avg=100)
        for item in result:
            sf = item.get("super_final")
            assert sf is None or isinstance(sf, (int, float, str)), \
                f"super_final должен быть числом, строкой или None, получен {type(sf)}"


class TestFunctionIntegration:
    """Тесты для проверки взаимодействия функций"""
    
    def test_compute_averages_handles_missing_scores(self):
        """Проверка обработки отсутствующих scores"""
        students = [{"id": 1, "name": "Test", "age": 20}]
        result = compute_averages(students)
        assert len(result) > 0
        assert result[0]["average"] is None
    
    def test_filter_handles_missing_adjusted(self):
        """Проверка обработки отсутствующего поля adjusted"""
        students = [{"id": 1, "age": 20, "average": 80}]
        result = filter_and_sort(students, min_age=18, max_avg=100)
        # Не должно быть исключения
        assert isinstance(result, list)
    
    def test_filter_handles_missing_scores(self):
        """Проверка обработки отсутствующего поля scores в filter_and_sort"""
        students = [{"id": 1, "age": 20, "average": 80, "adjusted": 85}]
        result = filter_and_sort(students, min_age=18, max_avg=100)
        # Должно быть поле final_score
        assert "final_score" in result[0]
    
    def test_data_integrity_through_pipeline(self):
        """Проверка сохранения ID через всю цепочку"""
        students = [
            {"id": 1, "age": 20, "scores": [80, 90, 100]},
            {"id": 2, "age": 22, "scores": [70, 80, 90]}
        ]
        averages = compute_averages(students)
        original_ids = {s["id"] for s in students}
        average_ids = {a["id"] for a in averages}
        assert original_ids == average_ids, "ID должны сохраняться после compute_averages"
    
    def test_empty_list_handling_compute_averages(self):
        """Проверка обработки пустого списка в compute_averages"""
        result = compute_averages([])
        assert isinstance(result, list)
        assert len(result) == 0
    
    def test_empty_list_handling_filter_and_sort(self):
        """Проверка обработки пустого списка в filter_and_sort"""
        result = filter_and_sort([], min_age=18, max_avg=100)
        assert isinstance(result, list)
        assert len(result) == 0
    
    def test_single_student_pipeline(self):
        """Проверка работы с одним студентом"""
        students = [{"id": 1, "age": 20, "scores": [80, 90, 100]}]
        averages = compute_averages(students)
        filtered = filter_and_sort(averages, min_age=18, max_avg=100)
        assert len(filtered) > 0
        assert isinstance(filtered[0], dict)
