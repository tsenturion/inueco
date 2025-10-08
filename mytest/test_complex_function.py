import pytest
from complex_func import analyze_text_statistics


# ============= БАЗОВЫЕ ТЕСТЫ =============

def test_basic_text_analysis():
    """Проверка анализа простого текста"""
    text = "Hello world! Python is great."
    result = analyze_text_statistics(text)
    
    assert result["total_words"] > 0
    assert result["total_sentences"] == 2
    assert result["longest_word"] is not None
    assert isinstance(result["word_frequency"], dict)
    assert isinstance(result["top_3_words"], list)
    pass

def test_empty_text_raises_error():
    """Проверка, что пустая строка вызывает ValueError"""
    with pytest.raises(ValueError):
        analyze_text_statistics("")
    pass

def test_whitespace_only_raises_error():
    """Проверка, что строка только с пробелами вызывает ValueError"""
    with pytest.raises(ValueError):
        analyze_text_statistics("   ")
    with pytest.raises(ValueError):
        analyze_text_statistics("  \t\n  ")
    pass

def test_invalid_type_raises_error():
    """Проверка, что передача нестрокового типа вызывает TypeError"""
    with pytest.raises(TypeError):
        analyze_text_statistics(123)
    with pytest.raises(TypeError):
        analyze_text_statistics(["test"])
    with pytest.raises(TypeError):
        analyze_text_statistics(None)
    pass

# ============= ТЕСТЫ ПОДСЧЕТА СЛОВ И СИМВОЛОВ =============

def test_word_count():
    """Проверка подсчета слов"""
    text = "One two three four five"
    result = analyze_text_statistics(text)
    
    assert result["total_words"] == 5
    assert result["total_characters"] == 23
    pass

def test_character_count():
    """Проверка подсчета символов"""
    text = "Hello"
    result = analyze_text_statistics(text)
    
    assert result["total_characters"] == 5
    assert result["total_words"] == 1
    pass

def test_sentence_count():
    """Проверка подсчета предложений"""
    text = "First! Second? Third."
    result = analyze_text_statistics(text)
    
    assert result["total_sentences"] == 3
    pass

# ============= ТЕСТЫ ПОИСКА СЛОВ =============

def test_longest_and_shortest_word():
    """Проверка поиска самого длинного и короткого слова"""
    text = "I am programming in Python language"
    result = analyze_text_statistics(text)
    
    assert result["longest_word"] == "programming"
    assert result["shortest_word"] == "i"
    pass

# ============= ТЕСТЫ ЧАСТОТЫ СЛОВ =============

def test_word_frequency_with_min_length():
    """Проверка частоты слов с минимальной длиной"""
    text = "cat dog cat bird cat dog"
    result = analyze_text_statistics(text, min_word_length=3)
    
    assert "cat" in result["word_frequency"]
    assert result["word_frequency"]["cat"] == 3
    assert "dog" in result["word_frequency"]
    assert result["word_frequency"]["dog"] == 2
    assert "bird" in result["word_frequency"]
    assert result["word_frequency"]["bird"] == 1
    pass

# ============= ДОПОЛНИТЕЛЬНЫЕ ТЕСТЫ =============

def test_unique_words_percentage():
    """Проверка процента уникальных слов"""
    text = "test test test unique"
    result = analyze_text_statistics(text)
    
    assert result["unique_words_count"] == 2
    assert result["unique_words_percentage"] == 50.0
    pass

def test_average_word_length():
    """Проверка средней длины слова"""
    text = "ab abc abcd"
    result = analyze_text_statistics(text)
    
    assert result["average_word_length"] == pytest.approx(3.0, rel=0.01)
    pass

def test_text_with_punctuation():
    """Проверка обработки текста с пунктуацией"""
    text = "Hello, world! How are you?"
    result = analyze_text_statistics(text)
    
    assert result["total_words"] == 5

    word_frequency_keys = list(result["word_frequency"].keys())
    assert "hello" in word_frequency_keys
    assert "world" in word_frequency_keys
    assert "hello," not in word_frequency_keys
    pass

def test_text_without_valid_words():
    """Проверка текста без валидных слов"""
    text = "!!! ??? ..."
    result = analyze_text_statistics(text)
    
    assert result["total_words"] == 0
    assert result["longest_word"] is None
    assert result["shortest_word"] is None
    assert result["word_frequency"] == {}
    assert result["top_3_words"] == []
    assert result["unique_words_count"] == 0
    assert result["unique_words_percentage"] == 0.0
    assert result["average_word_length"] == 0.0
    pass

def test_custom_min_word_length():
    """Проверка пользовательской минимальной длины слова"""
    text = "I am ok but you are great"
    result = analyze_text_statistics(text, min_word_length=4)

    for word in result["word_frequency"].keys():
        assert len(word) >= 4
    

    assert "great" in result["word_frequency"]
    assert "you" not in result["word_frequency"]
    assert "are" not in result["word_frequency"]
    pass

def test_case_insensitivity():
    """Проверка нечувствительности к регистру"""
    text = "Python PYTHON python PyThOn"
    result = analyze_text_statistics(text)
    
    assert result["word_frequency"]["python"] == 4
    assert len(result["word_frequency"]) == 1
    pass

def test_multiple_spaces():
    """Проверка обработки множественных пробелов"""
    text = "word1   word2    word3"
    result = analyze_text_statistics(text)
    
    assert result["total_words"] == 3
    assert "word1" in result["word_frequency"]
    assert "word2" in result["word_frequency"]
    assert "word3" in result["word_frequency"]
    pass

if __name__ == "__main__":
    pytest.main([__file__, "-v"])