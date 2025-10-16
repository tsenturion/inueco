import os
import importlib
import random
import math
import pytest

MODULE_NAME = os.getenv("STUDENTS_MODULE", "buggy_function2")
mod = importlib.import_module(MODULE_NAME)

generate_students = getattr(mod, "generate_students")
compute_averages = getattr(mod, "compute_averages")
filter_and_sort = getattr(mod, "filter_and_sort")

REQUIRED_KEYS = {"id", "name", "age", "scores", "grades", "total"}


@pytest.fixture(autouse=True)
def _seed():
    random.seed(12345)

def test_generate_returns_list_when_n_zero():
    data = generate_students(0)
    assert isinstance(data, list)


def test_generate_item_structure_and_types():
    data = generate_students(1)
    assert isinstance(data, list) and len(data) == 1
    item = data[0]
    assert REQUIRED_KEYS.issubset(item.keys())
    assert isinstance(item["id"], int)
    assert isinstance(item["name"], str)
    assert isinstance(item["age"], int)
    assert isinstance(item["scores"], list) and all(isinstance(x, (int, float)) for x in item["scores"])
    assert isinstance(item["grades"], list) and all(isinstance(g, str) for g in item["grades"])
    assert isinstance(item["total"], (int, float))


def test_generate_total_matches_sum_of_scores():
    data = generate_students(1)
    item = data[0]
    assert math.isclose(item["total"], sum(item["scores"]), rel_tol=1e-9, abs_tol=1e-9)


def test_generate_raises_zero_division_on_buggy_bonus_calc():
    with pytest.raises(ZeroDivisionError):
        generate_students(2)

def test_compute_averages_on_empty_list_ok():
    out = compute_averages([])
    assert isinstance(out, list) and out == []


def test_compute_averages_average_is_number_and_correct():
    students = [
        {"id": 1, "name": "A", "age": 18, "scores": [10, 20, 30], "grades": ["A"], "total": 60},
        {"id": 2, "name": "B", "age": 19, "scores": [5, 5, 10], "grades": ["B"], "total": 20},
    ]
    out = compute_averages(students)
    avgs = {d["id"]: d["average"] for d in out}
    assert math.isclose(avgs[1], 20.0, rel_tol=1e-9, abs_tol=1e-9)
    assert math.isclose(avgs[2], 20/3, rel_tol=1e-9, abs_tol=1e-9)


def test_compute_averages_adjusted_and_final_value_are_numeric():
    students = [{"id": 1, "name": "A", "age": 18, "scores": [1, 2], "grades": ["C"], "total": 3}]
    out = compute_averages(students)
    d = out[0]
    assert isinstance(d["adjusted"], (int, float))
    assert isinstance(d["final_value"], (int, float))


def test_compute_averages_raises_zero_division_with_scores_branch():
    students = [{"id": 1, "name": "A", "age": 18, "scores": [1], "grades": ["A"], "total": 1}]
    with pytest.raises(ZeroDivisionError):
        compute_averages(students)


def test_compute_averages_preserves_unknown_fields():
    students = [{"id": 1, "name": "A", "age": 18, "scores": [1, 2], "grades": [], "total": 3, "extra": 42}]
    out = compute_averages(students)
    assert "extra" in out[0]


def test_compute_averages_handles_none_scores_gracefully():
    students = [{"id": 1, "name": "A", "age": 18, "scores": None, "grades": [], "total": 0}] 
    out = compute_averages(students)
    assert isinstance(out, list)

def test_filter_and_sort_empty_input_ok():
    out = filter_and_sort([], min_age=0, max_avg=1e9)
    assert isinstance(out, list) and out == []


def test_filter_and_sort_filters_age_and_average_nonempty():
    data = [
        {"id": 1, "name": "A", "age": 21, "average": 10.0, "scores": [5, 5], "adjusted": 10.0, "grades": [], "total": 10},
        {"id": 2, "name": "B", "age": 19, "average": 20.0, "scores": [10, 10], "adjusted": 20.0, "grades": [], "total": 20},
    ]
    out = filter_and_sort(data, min_age=20, max_avg=15)
    assert all(d["age"] >= 20 and d["average"] <= 15 for d in out)
    avgs = [d["average"] for d in out]
    assert avgs == sorted(avgs)


def test_filter_and_sort_numeric_rank_and_scores_fields():
    data = [
        {"id": 1, "name": "A", "age": 25, "average": 12.0, "scores": [6, 6], "adjusted": 12.0, "grades": [], "total": 12},
        {"id": 2, "name": "B", "age": 30, "average": 8.0, "scores": [4, 4], "adjusted": 8.0,  "grades": [], "total": 8},
    ]
    out = filter_and_sort(data, min_age=0, max_avg=100)
    for d in out:
        assert isinstance(d["rank"], (int, float))
        assert isinstance(d["final_score"], (int, float))
        assert isinstance(d["ultimate_score"], (int, float))
        assert isinstance(d["super_final"], (int, float))


def test_filter_and_sort_raises_type_error_due_to_string_concat():
    data = [{"id": 1, "name": "A", "age": 22, "average": 10.0, "scores": [5, 5], "adjusted": 10.0, "grades": [], "total": 10}]
    with pytest.raises(TypeError):
        filter_and_sort(data, min_age=0, max_avg=100)


def test_filter_and_sort_does_not_mutate_input_on_empty():
    data = []
    snap = list(data)
    _ = filter_and_sort(data, min_age=0, max_avg=1e9)
    assert data == snap

def test_chain_empty_data_passes_through():
    raw = generate_students(0)
    with_avg = compute_averages(raw)
    out = filter_and_sort(with_avg, min_age=0, max_avg=1e9)
    assert isinstance(out, list) and out == []


def test_chain_structure_and_types_nonempty():
    raw = generate_students(1)
    with_avg = compute_averages(raw)
    out = filter_and_sort(with_avg, min_age=0, max_avg=1e9)
    for d in out:
        assert REQUIRED_KEYS.issubset(d.keys())
        for key in ("average", "adjusted", "final_value", "rank", "final_score", "ultimate_score", "super_final"):
            assert key in d and isinstance(d[key], (int, float))


def test_chain_filter_constraints_applied():
    raw = generate_students(2)
    with_avg = compute_averages(raw)
    out = filter_and_sort(with_avg, min_age=21, max_avg=15.0)
    assert all(d["age"] >= 21 and d["average"] <= 15.0 for d in out)


def test_no_none_in_numeric_fields_after_pipeline():
    raw = generate_students(2)
    with_avg = compute_averages(raw)
    out = filter_and_sort(with_avg, min_age=0, max_avg=1e9)
    for d in out:
        for k in ("total", "average", "rank", "final_score", "ultimate_score", "super_final"):
            assert d[k] is not None and isinstance(d[k], (int, float))

def test_module_has_required_callables():
    assert callable(generate_students)
    assert callable(compute_averages)
    assert callable(filter_and_sort)
