import sys
import os
import pytest

# Добавляем папку src в путь для импорта
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from complex_func import analyze_text_statistics

def test_basic_text_analysis():
    """Проверка анализа простого текста"""
    text = "Hello world! Python is great."
    result = analyze_text_statistics(text)
    
    assert result["total_words"] > 0
    assert result["total_sentences"] == 2
    assert result["longest_word"] is not None


def test_empty_text_raises_error():
    """Проверка, что пустая строка вызывает ValueError"""
    with pytest.raises(ValueError):
        analyze_text_statistics("")


def test_whitespace_only_raises_error():
    """Проверка, что строка только с пробелами вызывает ValueError"""
    with pytest.raises(ValueError):
        analyze_text_statistics("   ")


def test_invalid_type_raises_error():
    """Проверка, что передача нестрокового типа вызывает TypeError"""
    with pytest.raises(TypeError):
        analyze_text_statistics(123)
    
    with pytest.raises(TypeError):
        analyze_text_statistics(["test"])


def test_word_count():
    """Проверка подсчета слов"""
    text = "One two three four five"
    result = analyze_text_statistics(text)
    
    assert result["total_words"] == 5


def test_character_count():
    """Проверка подсчета символов"""
    text = "Hello"
    result = analyze_text_statistics(text)
    
    assert result["total_characters"] == 5


def test_sentence_count():
    """Проверка подсчета предложений"""
    text = "First! Second? Third."
    result = analyze_text_statistics(text)
    
    assert result["total_sentences"] == 3


def test_longest_and_shortest_word():
    """Проверка поиска самого длинного и короткого слова"""
    text = "I am programming in Python language"
    result = analyze_text_statistics(text)
    
    assert result["longest_word"] == "programming"
    assert result["shortest_word"] == "i"


def test_word_frequency_with_min_length():
    """Проверка частоты слов с минимальной длиной"""
    text = "cat dog cat bird cat dog"
    result = analyze_text_statistics(text, min_word_length=3)
    
    assert result["word_frequency"]["cat"] == 3
    assert result["word_frequency"]["dog"] == 2
    
    # Исправленная проверка - ищем слово 'cat' в словарях top_3_words
    top_words = [item["word"] for item in result["top_3_words"]]
    assert "cat" in top_words


def test_top_3_words():
    """Проверка топ-3 слов"""
    text = "apple banana apple cherry apple banana cherry cherry cherry"
    result = analyze_text_statistics(text)
    
    top_words = result["top_3_words"]
    assert len(top_words) == 3
    assert top_words[0]["word"] == "cherry"
    assert top_words[0]["count"] == 4
    assert top_words[1]["word"] == "apple"
    assert top_words[1]["count"] == 3


def test_unique_words_percentage():
    """Проверка процента уникальных слов"""
    text = "test test test unique"
    result = analyze_text_statistics(text)
    
    assert result["unique_words_count"] == 2
    assert result["unique_words_percentage"] == 50.0


def test_average_word_length():
    """Проверка средней длины слова"""
    text = "ab abc abcd"
    result = analyze_text_statistics(text)
    
    assert result["average_word_length"] == pytest.approx(3.0, rel=0.01)


def test_text_with_punctuation():
    """Проверка обработки текста со знаками препинания"""
    text = "Hello, world! How are you?"
    result = analyze_text_statistics(text)
    
    assert result["total_words"] == 5


def test_text_without_valid_words():
    """Проверка текста без валидных слов"""
    text = "!!! ??? ..."
    result = analyze_text_statistics(text)
    
    assert result["total_words"] == 0
    assert result["longest_word"] is None


def test_custom_min_word_length():
    """Проверка пользовательской минимальной длины слова"""
    text = "I am ok but you are great"
    result = analyze_text_statistics(text, min_word_length=4)
    
    # Проверяем, что в word_frequency нет слов короче 4 символов
    for word in result["word_frequency"]:
        assert len(word) >= 4
    
    # Убеждаемся, что 'great' присутствует в word_frequency
    assert "great" in result["word_frequency"]