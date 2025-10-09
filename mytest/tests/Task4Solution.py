import pytest
from complex_func import analyze_text_statistics


def _freq_get(freq_container, word):
    if isinstance(freq_container, dict):
        return int(freq_container.get(word, 0))
    total = 0
    for item in freq_container:
        if isinstance(item, dict):
            w = item.get("word") or item.get("token") or item.get("term")
            c = item.get("count") or item.get("freq") or item.get("frequency") or 0
            if w == word:
                total += int(c)
        elif isinstance(item, (list, tuple)) and len(item) >= 2:
            if item[0] == word:
                total += int(item[1])
    return total


def _top_pairs(top):
    pairs = []
    for item in top:
        if isinstance(item, dict):
            w = item.get("word") or item.get("token") or item.get("term")
            c = item.get("count") or item.get("freq") or item.get("frequency")
            pairs.append((w, int(c)))
        elif isinstance(item, (list, tuple)) and len(item) >= 2:
            pairs.append((item[0], int(item[1])))
        else:
            raise AssertionError("Unsupported top_3_words element format")
    return pairs


def _freq_keys(freq_container):
    if isinstance(freq_container, dict):
        return set(freq_container.keys())
    keys = set()
    for item in freq_container:
        if isinstance(item, dict):
            keys.add(item.get("word") or item.get("token") or item.get("term"))
        elif isinstance(item, (list, tuple)) and len(item) >= 1:
            keys.add(item[0])
    return keys


def test_basic_text_analysis():
    text = "Hello world! Python is great."
    result = analyze_text_statistics(text)
    for key in [
        "total_words", "total_sentences", "longest_word", "shortest_word",
        "total_characters", "word_frequency", "top_3_words",
        "unique_words_count", "unique_words_percentage", "average_word_length",
    ]:
        assert key in result
    assert result["total_words"] > 0
    assert result["total_sentences"] == 2
    assert result["longest_word"] is not None


def test_empty_text_raises_error():
    with pytest.raises(ValueError):
        analyze_text_statistics("")


def test_whitespace_only_raises_error():
    with pytest.raises(ValueError):
        analyze_text_statistics("   ")


def test_invalid_type_raises_error():
    with pytest.raises(TypeError):
        analyze_text_statistics(123)  
    with pytest.raises(TypeError):
        analyze_text_statistics(["test"])  


def test_word_count():
    res = analyze_text_statistics("One two three four five")
    assert res["total_words"] == 5


def test_character_count():
    res = analyze_text_statistics("Hello")
    assert res["total_characters"] == 5


def test_sentence_count():
    res = analyze_text_statistics("First! Second? Third.")
    assert res["total_sentences"] == 3


def test_longest_and_shortest_word():
    res = analyze_text_statistics("I am programming in Python language")
    assert res["longest_word"].lower() == "programming"
    assert res["shortest_word"].lower() == "i"


def test_word_frequency_with_min_length():
    text = "cat dog cat bird cat dog"
    res = analyze_text_statistics(text, min_word_length=3)
    freq = res["word_frequency"]
    assert _freq_get(freq, "cat") == 3
    assert _freq_get(freq, "dog") == 2
    top_pairs = _top_pairs(res["top_3_words"])
    assert any(w == "cat" for w, _ in top_pairs)


def test_top_3_words():
    text = "apple banana apple cherry apple banana cherry cherry cherry"
    res = analyze_text_statistics(text)
    top = _top_pairs(res["top_3_words"])
    assert len(top) == 3
    assert top[0][0] == "cherry" and top[0][1] == 4
    assert top[1][0] == "apple" and top[1][1] == 3


def test_unique_words_percentage():
    res = analyze_text_statistics("test test test unique")
    assert res["unique_words_count"] == 2
    assert res["unique_words_percentage"] == pytest.approx(50.0, rel=1e-6)


def test_average_word_length():
    res = analyze_text_statistics("ab abc abcd")
    assert res["average_word_length"] == pytest.approx(3.0, rel=1e-3)


def test_text_with_punctuation():
    res = analyze_text_statistics("Hello, world! How are you?")
    assert res["total_words"] == 5
    assert res["total_sentences"] == 2


def test_text_without_valid_words():
    res = analyze_text_statistics("!!! ??? ...")
    assert res["total_words"] == 0
    assert res["longest_word"] is None


def test_custom_min_word_length():
    res = analyze_text_statistics("I am ok but you are great", min_word_length=4)
    keys = _freq_keys(res["word_frequency"])
    assert all(len(k) >= 4 for k in keys)
    assert "great" in keys
