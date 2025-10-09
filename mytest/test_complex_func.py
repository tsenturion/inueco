import pytest
from complex_func import analyze_text_statistics

def test_basic_text_analysis():
    result = analyze_text_statistics("Hello world! Python is great.")
    assert result["total_words"] > 0
    assert result["total_sentences"] == 2
    assert result["longest_word"] is not None

def test_empty_text_raises_error():
    with pytest.raises(ValueError):
        analyze_text_statistics("")

def test_whitespace_only_raises_error():
    with pytest.raises(ValueError):
        analyze_text_statistics(" ")

def test_invalid_type_raises_error():
    with pytest.raises(TypeError):
        analyze_text_statistics(123)
    with pytest.raises(TypeError):
        analyze_text_statistics(["test"])

def test_word_count():
    result = analyze_text_statistics("One two three four five")
    assert result["total_words"] == 5

def test_character_count():
    result = analyze_text_statistics("Hello")
    assert result["total_characters"] == 5

def test_sentence_count():
    result = analyze_text_statistics("First! Second? Third.")
    assert result["total_sentences"] == 3

def test_longest_and_shortest_word():
    result = analyze_text_statistics("I am programming in Python language")
    assert result["longest_word"] == "programming"
    assert result["shortest_word"] == "i"

def test_word_frequency_with_min_length():
    result = analyze_text_statistics("cat dog cat bird cat dog", min_word_length=3)
    assert result["word_frequency"]["cat"] == 3
    assert result["word_frequency"]["dog"] == 2
    assert "cat" in [word["word"] for word in result["top_3_words"]]

def test_top_3_words():
    result = analyze_text_statistics("apple banana apple cherry apple banana cherry cherry cherry")
    top_words = [word["word"] for word in result["top_3_words"]]
    counts = [word["count"] for word in result["top_3_words"]]
    assert top_words[0] == "cherry"
    assert counts[0] == 4
    assert top_words[1] == "apple"
    assert counts[1] == 3
    assert len(result["top_3_words"]) == 3

def test_unique_words_percentage():
    result = analyze_text_statistics("test test test unique")
    assert result["unique_words_count"] == 2
    assert result["unique_words_percentage"] == 50.0

def test_average_word_length():
    result = analyze_text_statistics("ab abc abcd")
    assert result["average_word_length"] == pytest.approx(3.0, rel=0.01)

def test_text_with_punctuation():
    result = analyze_text_statistics("Hello, world! How are you?")
    assert result["total_words"] == 5

def test_text_without_valid_words():
    result = analyze_text_statistics("!!! ??? ...")
    assert result["total_words"] == 0
    assert result["longest_word"] is None

def test_custom_min_word_length():
    result = analyze_text_statistics("I am ok but you are great", min_word_length=4)
    short_words = ["i", "am", "ok", "but", "you", "are"]
    for word in short_words:
        assert word not in result["word_frequency"]
    assert "great" in result["word_frequency"]