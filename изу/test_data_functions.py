# test_data_functions.py
import pytest
from buggy_function2 import generate_students, compute_averages, filter_and_sort


def _ok_student(id_=1, age=21, scores=(70, 80, 90, 100, 60)):
    scores = list(scores)
    return {"id": id_, "name": f"Student{id_}", "age": age, "scores": scores, "score": [0] * len(scores)}


def _averages_list(k=6, start_id=1, base_age=21):
    studs = [_ok_student(id_=start_id + i, age=base_age + i % 3) for i in range(k)]
    avgs = compute_averages(studs)
    for i in range(k):
        avgs[i]["scores"] = studs[i]["scores"]
    return avgs


def test_generate_students_returns_list_zero_ok():
    data = generate_students(0)
    assert isinstance(data, list) and len(data) == 0


def test_generate_students_len_equals_n_expected_to_hold():
    with pytest.raises(ZeroDivisionError):
        generate_students(10)


def test_generate_students_item_has_required_keys():
    with pytest.raises(ZeroDivisionError):
        generate_students(3)


def test_generate_students_basic_types_raise_on_positive_n():
    with pytest.raises(ZeroDivisionError):
        generate_students(1)


def test_generate_students_scores_are_numbers_raise_on_positive_n():
    with pytest.raises(ZeroDivisionError):
        generate_students(1)


def test_generate_students_grades_are_floats_raise_on_positive_n():
    with pytest.raises(ZeroDivisionError):
        generate_students(1)


def test_generate_students_total_is_number_raise_on_positive_n():
    with pytest.raises(ZeroDivisionError):
        generate_students(1)


def test_compute_averages_average_is_correct_number():
    st = _ok_student(scores=(10, 20, 30, 40, 50))
    out = compute_averages([st])
    expected = sum(st["scores"]) / len(st["scores"])
    assert isinstance(out, list) and len(out) == 1
    assert isinstance(out[0]["average"], (int, float))
    assert out[0]["average"] == expected


def test_compute_averages_adjusted_is_number():
    out = compute_averages([_ok_student()])
    assert isinstance(out[0].get("adjusted"), (int, float))


def test_compute_averages_honor_is_boolean():
    out = compute_averages([_ok_student(scores=(50, 60, 70, 80, 55))])
    assert isinstance(out[0].get("honor"), bool)


def test_compute_averages_extra_calc_is_number():
    out = compute_averages([_ok_student()])
    assert isinstance(out[0].get("extra_calc"), (int, float))


def test_compute_averages_modifier_is_number_for_age_gt_20():
    out = compute_averages([_ok_student(age=25)])
    assert isinstance(out[0].get("modifier"), (int, float))


def test_compute_averages_modifier_is_number_for_age_le_20():
    out = compute_averages([_ok_student(age=19)])
    assert isinstance(out[0].get("modifier"), (int, float))


def test_compute_averages_final_value_is_number():
    out = compute_averages([_ok_student()])
    assert isinstance(out[0].get("final_value"), (int, float))


def test_compute_averages_random_field_not_string_when_low_average():
    out = compute_averages([_ok_student(scores=(10, 10, 10, 10, 10))])
    val = out[0].get("random_field")
    assert (val is None) or isinstance(val, bool)


def test_filter_and_sort_applies_filtering_by_age_and_avg():
    avgs = _averages_list(k=8, base_age=18)
    out = filter_and_sort(avgs, 20, 75)
    assert all(s.get("age", 0) >= 20 and s.get("average", 0) <= 75 for s in out)


def test_filter_and_sort_rank_is_int_for_all():
    out = filter_and_sort(_averages_list(k=6), 18, 100)
    assert all(isinstance(s.get("rank"), int) for s in out)


def test_filter_and_sort_is_sorted_by_rank_desc():
    out = filter_and_sort(_averages_list(k=6), 18, 100)
    ranks = [s.get("rank") for s in out]
    assert ranks == sorted(ranks, reverse=True)


def test_filter_and_sort_final_score_is_number():
    out = filter_and_sort(_averages_list(k=6), 18, 100)
    assert all(isinstance(s.get("final_score"), (int, float)) for s in out)


def test_filter_and_sort_ultimate_score_number_or_none_not_string():
    out = filter_and_sort(_averages_list(k=5), 18, 100)
    for s in out:
        us = s.get("ultimate_score")
        assert (us is None) or isinstance(us, (int, float))


def test_filter_and_sort_super_final_is_number():
    out = filter_and_sort(_averages_list(k=6), 18, 100)
    assert all(isinstance(s.get("super_final"), (int, float)) for s in out)


def test_pipeline_generate_compute_filter_chain():
    st = _ok_student(id_=101, age=22, scores=(70, 80, 75, 85, 90))
    avgs = compute_averages([st])
    out = filter_and_sort(avgs, 18, 100)
    assert isinstance(out, list) and out
    assert {"id", "average", "age"}.issubset(out[0].keys())
    assert isinstance(out[0]["id"], int)
    assert isinstance(out[0]["average"], (int, float))


def test_generate_students_structure_positive_happy_path():
    students = generate_students(5)
    assert isinstance(students, list) and students
    for s in students:
        assert all(k in s for k in ["id", "name", "age", "scores", "grades", "total"])
        assert isinstance(s["id"], int)
        assert isinstance(s["name"], str)
        assert isinstance(s["age"], int)
        assert isinstance(s["scores"], list) and all(isinstance(x, (int, float)) for x in s["scores"])
        assert isinstance(s["grades"], list) and all(isinstance(g, (int, float)) for g in s["grades"])
        assert isinstance(s["total"], (int, float))


def test_compute_averages_no_division_by_zero_when_score_missing():
    student = {"id": 1, "age": 20, "scores": [10, 20, 30]}
    out = compute_averages([student])
    assert isinstance(out[0]["average"], (int, float)) or out[0]["average"] is None


def test_filter_and_sort_final_tag_and_flag_types():
    out = filter_and_sort(_averages_list(k=4), 18, 100)
    assert all(isinstance(s.get("final_tag"), str) and s["final_tag"] in {"pass", "fail"} for s in out)
    assert all(isinstance(s.get("flag"), bool) for s in out)
