import pytest
from complex_func import analyze_text_statistics

def _freq_to_dict(freq):

    if isinstance(freq, dict):
        return freq
    if isinstance(freq, list):
        out = {}
        for item in freq:
            if isinstance(item, tuple) and len(item) >= 2:
                out[item[0]] = item[1]
            elif isinstance(item, dict):
                w = item.get("word")
                c = item.get("count")
                if w is not None:
                    out[w] = c
        return out
    raise AssertionError("Unexpected word_frequency format")


def _top_to_pairs(top):

    if isinstance(top, list):
        if not top:
            return []
        if isinstance(top[0], tuple):
            return top
        if isinstance(top[0], dict):
            return [(d.get("word"), d.get("count")) for d in top]
    raise AssertionError("Unexpected top_3_words format")


def _assert_has_keys(result, keys):
    for k in keys:
        assert k in result, f"Result must contain '{k}' key"

def test_basic_text_analysis():
    text = "Hello world! Python is great."
    result = analyze_text_statistics(text)

    required = {
        "total_words",
        "total_sentences",
        "total_characters",
        "longest_word",
        "shortest_word",
        "word_frequency",
        "top_3_words",
        "unique_words_count",
        "unique_words_percentage",
        "average_word_length",
    }
    _assert_has_keys(result, required)

    assert result["total_words"] > 0
    assert result["total_sentences"] == 2
    assert result["longest_word"] is not None

def test_empty_text_raises_error():
    with pytest.raises(ValueError):
        analyze_text_statistics("")

def test_whitespace_only_raises_error():
    with pytest.raises(ValueError):
        analyze_text_statistics("     \t   \n   ")

@pytest.mark.parametrize("bad_value", [123, 45.6, ["test"], {"text": "str"}])
def test_invalid_type_raises_error(bad_value):
    with pytest.raises(TypeError):
        analyze_text_statistics(bad_value)

def test_word_count():
    text = "One two three four five"
    result = analyze_text_statistics(text)
    assert result["total_words"] == 5

def test_character_count():
    text = "Hello"
    result = analyze_text_statistics(text)
    assert result["total_characters"] == 5

def test_sentence_count():
    text = "First! Second? Third."
    result = analyze_text_statistics(text)
    assert result["total_sentences"] == 3

def test_longest_and_shortest_word():
    text = "I am programming in Python language"
    result = analyze_text_statistics(text)
    assert result["longest_word"] == "programming"
    assert result["shortest_word"] == "i"

def test_word_frequency_with_min_length():
    text = "cat dog cat bird cat dog"
    result = analyze_text_statistics(text, min_word_length=3)
    freq = _freq_to_dict(result["word_frequency"])
    top = _top_to_pairs(result["top_3_words"])
    assert freq.get("cat", 0) == 3
    assert freq.get("dog", 0) == 2
    assert any(word == "cat" for word, count in top)


def test_top_3_words():
    text = "apple banana apple cherry apple banana cherry cherry cherry"
    result = analyze_text_statistics(text)

    top = _top_to_pairs(result["top_3_words"])
    assert len(top) == 3
    assert top[0][0] == "cherry" and top[0][1] == 4
    assert top[1][0] == "apple" and top[1][1] == 3

def test_unique_words_percentage():
    text = "test test test unique"
    result = analyze_text_statistics(text)
    assert result["unique_words_count"] == 2
    assert result["unique_words_percentage"] == pytest.approx(50.0, rel=1e-6)


def test_average_word_length():
    text = "ab abc abcd"
    result = analyze_text_statistics(text)
    assert result["average_word_length"] == pytest.approx(3.0, rel=0.01)


def test_text_with_punctuation():
    text = "Hello, world! How are you?"
    result = analyze_text_statistics(text)
    assert result["total_words"] == 5


def test_text_without_valid_words():
    text = "!!! ??? ..."
    result = analyze_text_statistics(text)
    assert result["total_words"] == 0
    assert result["longest_word"] is None


def test_custom_min_word_length():
    text = "I am ok but you are great"
    result = analyze_text_statistics(text, min_word_length=4)
    freq = _freq_to_dict(result["word_frequency"])
    assert "great" in freq and freq["great"] >= 1
    assert all(len(word) >= 4 for word in freq.keys())
