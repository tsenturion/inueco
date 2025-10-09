import pytest
from complex_func import analyze_text_statistics


def test_basic_text_analysis():
    text = "Hello world! Python is great."
    result = analyze_text_statistics(text)
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
    word_freq = result["word_frequency"]
    assert word_freq["cat"] == 3
    assert word_freq["dog"] == 2
    
    top_words = []
    for item in result["top_3_words"]:
        if isinstance(item, tuple):
            top_words.append(item[0])
        elif isinstance(item, dict):
            top_words.append(item.get('word', ''))
        else:
            top_words.append(str(item))
    
    assert "cat" in top_words


def test_top_3_words():
    text = "apple banana apple cherry apple banana cherry cherry cherry"
    result = analyze_text_statistics(text)
    top_words = result["top_3_words"]
    assert len(top_words) == 3
    
    top_words_list = []
    for item in top_words:
        if isinstance(item, tuple):
            top_words_list.append(item[0])
        elif isinstance(item, dict):
            top_words_list.append(item.get('word', ''))
        else:
            top_words_list.append(str(item))
    
    assert "cherry" in top_words_list


def test_unique_words_percentage():
    text = "test test test unique"
    result = analyze_text_statistics(text)
    assert result["unique_words_count"] == 2
    assert result["unique_words_percentage"] == 50.0


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
    for word in result["word_frequency"].keys():
        assert len(word) >= 4
    assert "great" in result["word_frequency"]