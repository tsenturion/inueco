import pytest
from buggy_function import process_student_scores



class TestBuggyFunction:

    def test_success_method(self):
        result = process_student_scores( [{"name": "Илья", "scores": [57,87,45,92, 80, 70], "age": 20}, {"name": "Евгений", "scores": [99,100,88,89, 90, 97], "age": 19}, {"name": "Анатолий", "scores": [100,55,87,25], "age": 18}] )
        assert result != None
        assert result["total_students"] == 3

    def test_none_list_strudent(self):
        result = process_student_scores([])
        assert result == None

    def test_none_list_score(self):
        with pytest.raises(TypeError) as e:
            process_student_scores( [{"name": "Илья", "scores": [57,87,45,92, 80, 70], "age": 20}, {"name": "Евгений", "scores": [], "age": 19}, {"name": "Анатолий", "scores": [100,55,87,25], "age": 18}] )
        assert str(e.value) != None

    def test_none_list_score_all(self):
        with pytest.raises(TypeError) as e:
            process_student_scores( [{"name": "Илья", "scores": [], "age": 20}, {"name": "Евгений", "scores": [], "age": 19}, {"name": "Анатолий", "scores": [], "age": 18}] )
        assert str(e.value) != None

    def test_list_one_student(self):
        result = process_student_scores( [{"name": "Илья", "scores": [57,87,45,92, 80, 70], "age": 20}] )
        assert result != None

    def test_average_score_more_60(self):
        result = process_student_scores( [{"name": "Илья", "scores": [57,87,45,92, 80, 70], "age": 20}, {"name": "Евгений", "scores": [99,100,88,89, 90, 97], "age": 19}, {"name": "Анатолий", "scores": [100,55,87,25], "age": 19}] )
        assert result != None
        assert result["average_score"] == pytest.approx(78.8, rel=0.01)

    def test_len_average_score_60_student(self):
        result = process_student_scores( [{"name": "Илья", "scores": [65,87,95,92, 80, 70], "age": 20}, {"name": "Евгений", "scores": [60,60,60,60, 60, 60], "age": 19}, {"name": "Анатолий", "scores": [70,20,40,50], "age": 19}] )
        assert result != None
        assert len(result["failed_students"]) == 1


    def test_age_total_18(self):
        result = process_student_scores( [{"name": "Илья", "scores": [57,87,45,92, 80, 70], "age": 20}, {"name": "Евгений", "scores": [99,100,88,89, 90, 97], "age": 18}, {"name": "Анатолий", "scores": [100,55,87,25], "age": 18}] )
        assert result != None
        assert result["adults_count"] == 3

    def test_top_student(self):
        result = process_student_scores( [{"name": "Илья", "scores": [57,87,45,92, 80, 70], "age": 20}, {"name": "Евгений", "scores": [99,100,88,89, 90, 97], "age": 19}, {"name": "Анатолий", "scores": [100,55,30,25], "age": 18}] )
        assert result != None
        assert result["top_student"] == "Евгений"

    def test_age_minus(self):
        with pytest.raises(ValueError) as e:
            process_student_scores( [{"name": "Илья", "scores": [0,0,0,0], "age": 20}, {"name": "Евгений", "scores": [0,0,0,0], "age": 19}, {"name": "Анатолий", "scores": [0,0,0,0,0], "age": -18}] )
        assert str(e.value) != None

    def test_name_number(self):
        with pytest.raises(TypeError) as e:
            process_student_scores( [{"name": 12333, "scores": [57,87,45,92, 80, 70], "age": 20}, {"name": "Евгений", "scores": [99,100,88,89, 90, 97], "age": 19}, {"name": "Анатолий", "scores": [100,55,87,25], "age": 18}] )
        assert str(e.value) != None


    def test_name_number(self):
        with pytest.raises(TypeError) as e:
            process_student_scores( [{"name": "Илья", "scores": ["57","str","45",92, 80, 70], "age": 20}, {"name": "Евгений", "scores": [99,100,88,89, 90, 97], "age": 19}, {"name": "Анатолий", "scores": [100,55,87,25], "age": 18}] )
        assert str(e.value) != None

    def test_minus_number_score(self):
        with pytest.raises(ValueError) as e:
            process_student_scores( [{"name": "Илья", "scores": [-57,87,-45,92, 80, -70], "age": 20}, {"name": "Евгений", "scores": [99,100,88,89, 90, 97], "age": 19}, {"name": "Анатолий", "scores": [100,55,87,25], "age": 18}] )
        assert str(e.value) != None

    def test_string_age(self):
        with pytest.raises(TypeError) as e:
            process_student_scores( [{"name": "Илья", "scores": [57,87,45,92, 80, 70], "age": "20"}, {"name": "Евгений", "scores": [99,100,88,89, 90, 97], "age": 19}, {"name": "Анатолий", "scores": [100,55,87,25], "age": 18}] )
        assert str(e.value) != None

    def test_scores_int(self):
        with pytest.raises(TypeError) as e:
            process_student_scores( [{"name": "Илья", "scores": 10, "age": "20"}, {"name": "Евгений", "scores": [99,100,88,89, 90, 97], "age": 19}, {"name": "Анатолий", "scores": [100,55,87,25], "age": 18}] )
        assert str(e.value) != None

