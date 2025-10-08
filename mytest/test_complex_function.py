import pytest
from complex_func import analyze_text_statistics


def test_basic_text_analysis():
    """Тест базового анализа текста"""
    text = "Hello world! Python is great."
    result = analyze_text_statistics(text)
    
    assert result["total_words"] > 0
    assert result["total_sentences"] == 2
    assert result["longest_word"] is not None
    assert result["total_characters"] == len(text.strip())


def test_empty_text_raises_error():
    """Тест пустой строки вызывает ValueError"""
    with pytest.raises(ValueError):
        analyze_text_statistics("")


def test_whitespace_only_raises_error():
    """Тест строки только с пробелами вызывает ValueError"""
    with pytest.raises(ValueError):
        analyze_text_statistics("   ")
    with pytest.raises(ValueError):
        analyze_text_statistics("  \t\n  ")


def test_invalid_type_raises_error():
    """Тест неверного типа данных вызывает TypeError"""
    with pytest.raises(TypeError):
        analyze_text_statistics(123)
    with pytest.raises(TypeError):
        analyze_text_statistics(["test"])
    with pytest.raises(TypeError):
        analyze_text_statistics(None)


def test_word_count():
    """Тест подсчета количества слов"""
    text = "One two three four five"
    result = analyze_text_statistics(text)
    
    assert result["total_words"] == 5


def test_character_count():
    """Тест подсчета количества символов"""
    text = "Hello"
    result = analyze_text_statistics(text)
    
    assert result["total_characters"] == 5


def test_sentence_count():
    """Тест подсчета количества предложений"""
    text = "First! Second? Third."
    result = analyze_text_statistics(text)
    
    assert result["total_sentences"] == 3


def test_longest_and_shortest_word():
    """Тест поиска самого длинного и короткого слова"""
    text = "I am programming in Python language"
    result = analyze_text_statistics(text)
    
    assert result["longest_word"] == "programming"
    assert result["shortest_word"] == "i"


def test_word_frequency_with_min_length():
    """Тест частоты слов с минимальной длиной"""
    text = "cat dog cat bird cat dog"
    result = analyze_text_statistics(text, min_word_length=3)
    
    assert result["word_frequency"]["cat"] == 3
    assert result["word_frequency"]["dog"] == 2
    assert result["word_frequency"]["bird"] == 1
    
    # Проверяем, что cat в топ-3
    top_words = [item["word"] for item in result["top_3_words"]]
    assert "cat" in top_words


def test_top_3_words():
    """Тест топ-3 самых частых слов"""
    text = "apple banana apple cherry apple banana cherry cherry cherry"
    result = analyze_text_statistics(text)
    
    assert len(result["top_3_words"]) == 3
    assert result["top_3_words"][0]["word"] == "cherry"
    assert result["top_3_words"][0]["count"] == 4
    assert result["top_3_words"][1]["word"] == "apple"
    assert result["top_3_words"][1]["count"] == 3
    assert result["top_3_words"][2]["word"] == "banana"
    assert result["top_3_words"][2]["count"] == 2


def test_unique_words_percentage():
    """Тест процента уникальных слов"""
    text = "test test test unique"
    result = analyze_text_statistics(text)
    
    assert result["unique_words_count"] == 2
    assert result["unique_words_percentage"] == 50.0


def test_average_word_length():
    """Тест средней длины слова"""
    text = "ab abc abcd"
    result = analyze_text_statistics(text)
    
    assert result["average_word_length"] == pytest.approx(3.0, rel=0.01)


def test_text_with_punctuation():
    """Тест обработки текста со знаками препинания"""
    text = "Hello, world! How are you?"
    result = analyze_text_statistics(text)
    
    assert result["total_words"] == 5
    assert "hello" in result["word_frequency"]
    assert "world" in result["word_frequency"]


def test_text_without_valid_words():
    """Тест текста без валидных слов"""
    text = "!!! ??? ..."
    result = analyze_text_statistics(text)
    
    assert result["total_words"] == 0
    assert result["longest_word"] is None
    assert result["shortest_word"] is None
    assert result["average_word_length"] == 0.0
    assert result["unique_words_count"] == 0
    assert result["unique_words_percentage"] == 0.0
    assert result["top_3_words"] == []
    assert result["word_frequency"] == {}


def test_custom_min_word_length():
    """Тест пользовательской минимальной длины слова"""
    text = "I am ok but you are great"
    result = analyze_text_statistics(text, min_word_length=4)
    
    # Слова короче 4 символов не должны быть в word_frequency
    assert "i" not in result["word_frequency"]
    assert "am" not in result["word_frequency"]
    assert "ok" not in result["word_frequency"]
    assert "but" not in result["word_frequency"]
    assert "you" not in result["word_frequency"]
    assert "are" not in result["word_frequency"]
    
    # Слово 'great' должно присутствовать
    assert "great" in result["word_frequency"]
    
    # Но общее количество слов должно включать все слова
    assert result["total_words"] == 7