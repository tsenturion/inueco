import pytest
from complex_func import analyze_text_statistics


def test_basic_text_analysis():
    """Проверка анализа простого текста"""
    text = "Hello world! Python is great."
    result = analyze_text_statistics(text)
    
    assert result['total_words'] > 0
    assert result['total_sentences'] == 2
    assert result['longest_word'] is not None


def test_empty_text_raises_error():
    """Проверка, что пустая строка вызывает ValueError"""
    with pytest.raises(ValueError):
        analyze_text_statistics("")


def test_whitespace_only_raises_error():
    """Проверка, что строка только с пробелами вызывает ValueError"""
    with pytest.raises(ValueError):
        analyze_text_statistics("   ")


def test_invalid_type_raises_error():
    """Проверка, что нестроковые типы вызывают TypeError"""
    with pytest.raises(TypeError):
        analyze_text_statistics(123)
    
    with pytest.raises(TypeError):
        analyze_text_statistics(["test"])


def test_word_count():
    """Проверка подсчета слов"""
    text = "One two three four five"
    result = analyze_text_statistics(text)
    
    assert result['total_words'] == 5


def test_character_count():
    """Проверка подсчета символов"""
    text = "Hello"
    result = analyze_text_statistics(text)
    
    assert result['total_characters'] == 5


def test_sentence_count():
    """Проверка подсчета предложений"""
    text = "First! Second? Third."
    result = analyze_text_statistics(text)
    
    assert result['total_sentences'] == 3


def test_top_3_words():
    """Проверка топ-3 слов по частоте"""
    text = "apple banana apple cherry apple banana cherry cherry cherry"
    result = analyze_text_statistics(text)
    
    assert result['top_3_words'][0]['word'] == 'cherry'
    assert result['top_3_words'][0]['count'] == 4
    assert result['top_3_words'][1]['word'] == 'apple'
    assert result['top_3_words'][1]['count'] == 3
    assert len(result['top_3_words']) == 3


def test_unique_words_percentage():
    """Проверка процента уникальных слов"""
    text = "test test test unique"
    result = analyze_text_statistics(text)
    
    assert result['unique_words_count'] == 2
    assert result['unique_words_percentage'] == 50.0


def test_average_word_length():
    """Проверка средней длины слова"""
    text = "ab abc abcd"
    result = analyze_text_statistics(text)
    
    assert round(result['average_word_length'], 1) == 3.0


def test_text_with_punctuation():
    """Проверка обработки текста со знаками препинания"""
    text = "Hello, world! How are you?"
    result = analyze_text_statistics(text)
    
    assert result['total_words'] == 5


def test_text_without_valid_words():
    """Проверка текста без валидных слов"""
    text = "!!! ??? ..."
    result = analyze_text_statistics(text)
    
    assert result['total_words'] == 0
    assert result['longest_word'] is None


def test_custom_min_word_length():
    """Проверка пользовательской минимальной длины слова"""
    text = "I am ok but you are great"
    result = analyze_text_statistics(text, min_word_length=4)

    # Проверяем, что слова короче 4 символов отсутствуют
    for word in result['word_frequency']:
        assert len(word) >= 4
    
    assert 'great' in result['word_frequency']