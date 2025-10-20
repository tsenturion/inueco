import pytest
from complex_func import analyze_text_statistics


def test_basic_text_analysis():
    """Тест базового анализа простого текста"""
    text = "Hello world! Python is great."
    result = analyze_text_statistics(text)
    
    assert result["total_words"] > 0
    assert result["total_sentences"] == 2
    assert result["longest_word"] is not None
    assert isinstance(result, dict)


def test_empty_text_raises_error():
    """Тест на пустую строку - должно вызвать ValueError"""
    with pytest.raises(ValueError):
        analyze_text_statistics("")


def test_whitespace_only_raises_error():
    """Тест на строку только с пробелами - должно вызвать ValueError"""
    with pytest.raises(ValueError):
        analyze_text_statistics("   ")
    
    with pytest.raises(ValueError):
        analyze_text_statistics("\n\t  ")


def test_invalid_type_raises_error():
    """Тест на неверный тип данных - должно вызвать TypeError"""
    with pytest.raises(TypeError):
        analyze_text_statistics(123)
    
    with pytest.raises(TypeError):
        analyze_text_statistics(["test"])
    
    with pytest.raises(TypeError):
        analyze_text_statistics(None)


def test_word_count():
    """Тест правильного подсчета количества слов"""
    text = "One two three four five"
    result = analyze_text_statistics(text)
    
    assert result["total_words"] == 5


def test_character_count():
    """Тест правильного подсчета символов"""
    text = "Hello"
    result = analyze_text_statistics(text)
    
    assert result["total_characters"] == 5


def test_sentence_count():
    """Тест правильного подсчета предложений"""
    text = "First! Second? Third."
    result = analyze_text_statistics(text)
    
    assert result["total_sentences"] == 3
    
    # Дополнительный тест с одним предложением
    text2 = "Only one sentence"
    result2 = analyze_text_statistics(text2)
    assert result2["total_sentences"] == 1


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
    
    assert "cat" in result["word_frequency"]
    assert result["word_frequency"]["cat"] == 3
    assert "dog" in result["word_frequency"]
    assert result["word_frequency"]["dog"] == 2
    assert "bird" in result["word_frequency"]
    assert result["word_frequency"]["bird"] == 1
    
    # Проверяем, что cat есть в топ-3
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
    
    # (2 + 3 + 4) / 3 = 3.0
    assert result["average_word_length"] == pytest.approx(3.0, rel=0.01)
    
    # Дополнительный тест
    text2 = "hello world"
    result2 = analyze_text_statistics(text2)
    # (5 + 5) / 2 = 5.0
    assert result2["average_word_length"] == 5.0


def test_text_with_punctuation():
    """Тест корректной обработки знаков препинания"""
    text = "Hello, world! How are you?"
    result = analyze_text_statistics(text)
    
    assert result["total_words"] == 5
    assert "hello" in [result["longest_word"], result["shortest_word"]]


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
    """Тест кастомной минимальной длины слова"""
    text = "I am ok but you are great"
    result = analyze_text_statistics(text, min_word_length=4)
    
    # Проверяем, что короткие слова не попали в word_frequency
    assert "i" not in result["word_frequency"]
    assert "am" not in result["word_frequency"]
    assert "ok" not in result["word_frequency"]
    assert "but" not in result["word_frequency"]
    assert "you" not in result["word_frequency"]
    assert "are" not in result["word_frequency"]
    
    # Проверяем, что слово длиной 5 символов есть
    assert "great" in result["word_frequency"]
    assert result["word_frequency"]["great"] == 1


def test_case_insensitivity():
    """Тест на нечувствительность к регистру"""
    text = "Python python PYTHON PyThOn"
    result = analyze_text_statistics(text)
    
    assert result["word_frequency"]["python"] == 4
    assert result["unique_words_count"] == 1


def test_numbers_in_text():
    """Тест обработки текста с цифрами"""
    text = "Python3 is better than Python2"
    result = analyze_text_statistics(text)
    
    assert result["total_words"] == 5
    assert "python3" in result["word_frequency"]
    assert "python2" in result["word_frequency"]


def test_multiple_sentences_without_spaces():
    """Тест нескольких предложений без пробелов после знаков"""
    text = "First.Second!Third?"
    result = analyze_text_statistics(text)
    
    assert result["total_sentences"] == 3


def test_mixed_punctuation():
    """Тест смешанной пунктуации"""
    text = "Hello!!! World??? Python... Great!!!"
    result = analyze_text_statistics(text)
    
    assert result["total_words"] == 4
    assert result["total_sentences"] == 4


def test_return_structure():
    """Тест корректной структуры возвращаемого словаря"""
    text = "Simple test text"
    result = analyze_text_statistics(text)
    
    # Проверяем наличие всех ключей
    required_keys = [
        "total_characters",
        "total_words",
        "total_sentences",
        "longest_word",
        "shortest_word",
        "average_word_length",
        "unique_words_count",
        "unique_words_percentage",
        "top_3_words",
        "word_frequency"
    ]
    
    for key in required_keys:
        assert key in result
    
    # Проверяем типы данных
    assert isinstance(result["total_characters"], int)
    assert isinstance(result["total_words"], int)
    assert isinstance(result["total_sentences"], int)
    assert isinstance(result["average_word_length"], float)
    assert isinstance(result["unique_words_count"], int)
    assert isinstance(result["unique_words_percentage"], float)
    assert isinstance(result["top_3_words"], list)
    assert isinstance(result["word_frequency"], dict)