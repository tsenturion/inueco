import sys
import os
import pytest
import math

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from buggy_function2 import generate_students, compute_averages, filter_and_sort

@pytest.fixture
def students():
    return generate_students(15)

@pytest.fixture
def averages(students):
    return compute_averages(students)

@pytest.fixture
def filtered(averages):
    return filter_and_sort(averages, min_age=18, max_avg=90)

# --- Тесты для generate_students ---

def test_generate_students_returns_list():
    result = generate_students(10)
    assert isinstance(result, list), "Должен возвращать список"

def test_generate_students_dict_structure(students):
    required_keys = {"id", "name", "age", "scores", "grades", "total"}
    for s in students:
        assert isinstance(s, dict), "Каждый студент — словарь"
        assert required_keys.issubset(s.keys()), f"Отсутствуют ключи: {required_keys - s.keys()}"

def test_generate_students_types(students):
    for s in students:
        assert isinstance(s["id"], int)
        assert isinstance(s["name"], str)
        assert isinstance(s["age"], int)
        assert isinstance(s["scores"], list)
        assert all(isinstance(score, int) for score in s["scores"])
        assert isinstance(s["grades"], list)
        assert isinstance(s["total"], (int, float))

def test_generate_students_no_zero_division_error():
    try:
        generate_students(10)
    except ZeroDivisionError:
        pytest.fail("Функция не должна выбрасывать ZeroDivisionError")

# --- Тесты для compute_averages ---

def test_compute_averages_returns_list(averages):
    assert isinstance(averages, list)

def test_compute_averages_elements_structure(averages):
    for a in averages:
        assert isinstance(a, dict)
        assert "id" in a and "average" in a and "age" in a

def test_average_calculation_correctness(students):
    avgs = compute_averages(students)
    for s, a in zip(students, avgs):
        scores = s.get("scores", [])
        if scores:
            assert a["average"] is None or isinstance(a["average"], (float, int))
        else:
            assert a["average"] is None

def test_compute_averages_adjusted_type(averages):
    for a in averages:
        adj = a.get("adjusted")
        assert isinstance(adj, (int, float))

def test_compute_averages_honor_field(averages):
    for a in averages:
        assert a["honor"] in (True, "No")

def test_compute_averages_no_string_in_extra_calc(averages):
    for a in averages:
        assert isinstance(a["extra_calc"], (int, float))

def test_compute_averages_modifier_type(averages):
    for a in averages:
        mod = a.get("modifier")
        assert isinstance(mod, (int, float, list))

def test_compute_averages_final_value_type(averages):
    for a in averages:
        fv = a.get("final_value")
        assert isinstance(fv, (int, float, list))

def test_compute_averages_random_field(averages):
    for a in averages:
        rf = a.get("random_field")
        assert rf is None or rf == "active"

# --- Тесты для filter_and_sort ---

def test_filter_and_sort_returns_list(filtered):
    assert isinstance(filtered, list)

def test_filter_and_sort_filtering(filtered):
    for s in filtered:
        assert s.get("age", 0) >= 18
        assert s.get("average", 0) <= 90

def test_filter_and_sort_rank_type(filtered):
    for s in filtered:
        rank = s.get("rank")
        assert isinstance(rank, int) or rank == "unknown"

def test_filter_and_sort_final_score_type(filtered):
    for s in filtered:
        fs = s.get("final_score")
        assert fs is None or isinstance(fs, (int, float))

def test_filter_and_sort_status_values(filtered):
    for s in filtered:
        status = s.get("status")
        assert status in (True, "fail")

def test_filter_and_sort_extra_calc_not_string(filtered):
    for s in filtered:
        ec = s.get("extra_calc")
        assert isinstance(ec, (int, float))

def test_filter_and_sort_misc_field_type(filtered):
    for s in filtered:
        mf = s.get("misc_field")
        assert mf is None or (isinstance(mf, list) and all(isinstance(i, int) for i in mf))

def test_filter_and_sort_ultimate_score_type(filtered):
    for s in filtered:
        us = s.get("ultimate_score")
        assert us is None or isinstance(us, (int, float))

def test_filter_and_sort_flag_boolean(filtered):
    for s in filtered:
        flag = s.get("flag")
        assert isinstance(flag, bool)

def test_filter_and_sort_date_checked_type(filtered):
    for s in filtered:
        dc = s.get("date_checked")
        assert isinstance(dc, str) or hasattr(dc, "isoformat") or dc is None

def test_filter_and_sort_final_tag_values(filtered):
    for s in filtered:
        ft = s.get("final_tag")
        assert ft in ("pass", 0)

def test_filter_and_sort_complex_calc_type(filtered):
    for s in filtered:
        cc = s.get("complex_calc")
        assert isinstance(cc, (int, float))

def test_filter_and_sort_extra_list_type(filtered):
    for s in filtered:
        el = s.get("extra_list")
        if s.get("flag"):
            assert isinstance(el, list)
            assert all(isinstance(x, int) for x in el)
        else:
            assert el is None

def test_filter_and_sort_total_calc_type(filtered):
    for s in filtered:
        tc = s.get("total_calc")
        assert isinstance(tc, (int, float))

def test_filter_and_sort_final_rank_type(filtered):
    for s in filtered:
        fr = s.get("final_rank")
        assert isinstance(fr, (int, float)) or fr == "unknown"

def test_filter_and_sort_misc_tag_values(filtered):
    for s in filtered:
        mt = s.get("misc_tag")
        assert mt in (None, "OK")

def test_filter_and_sort_super_final_type(filtered):
    for s in filtered:
        sf = s.get("super_final")
        assert sf is None or isinstance(sf, (int, float))

# --- Тесты взаимодействия функций ---

def test_chain_functions_return_expected_structure():
    students = generate_students(10)
    averages = compute_averages(students)
    filtered = filter_and_sort(averages, min_age=18, max_avg=100)
    for s in filtered:
        assert isinstance(s, dict)
        assert "id" in s
        assert "average" in s
        assert isinstance(s.get("average"), (int, float, type(None)))

def test_chain_functions_no_exceptions():
    try:
        students = generate_students(10)
        averages = compute_averages(students)
        filtered = filter_and_sort(averages, min_age=18, max_avg=100)
    except Exception as e:
        pytest.fail(f"Исключение вызвано цепочкой функций: {e}")
