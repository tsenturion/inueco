import pytest
from complex_func import analyze_text_statistics

# Базовые тесты
def test_basic_text_analysis():
    str = "Hello world! Python is great."
    func_result = analyze_text_statistics(str)
    assert func_result['total_words'] > 0
    assert func_result['total_sentences'] == 2
    assert func_result['longest_word'] != None
    pass

def test_empty_text_raises_error():
    with pytest.raises(ValueError):
        analyze_text_statistics("")
    pass

def test_whitespace_only_raises_error():
    with pytest.raises(ValueError):
        analyze_text_statistics(" ")
    pass

def test_invalid_type_raises_error():
    with pytest.raises(TypeError):
        analyze_text_statistics(123)
        analyze_text_statistics(['test'])
    pass

# Тесты подсчёта слов и символов
def test_word_count():
    str = "One two three four five"
    func_result = analyze_text_statistics(str)
    assert func_result['total_words'] == 5
    pass

def test_character_count():
    str = "Hello"
    func_result = analyze_text_statistics(str)
    assert func_result['total_characters'] == 5
    pass

def test_sentence_count():
    str = "First! Second? Third."
    func_result = analyze_text_statistics(str)
    assert func_result['total_sentences'] == 3
    pass

# Тесты поиска слов
def test_longest_and_shortest_word():
    str = "I am programming in Python language"
    func_result = analyze_text_statistics(str)
    assert func_result['longest_word'] == "programming"
    assert func_result['shortest_word'] == "i"
    pass

# Тесты частоты слов
def test_word_frequency_with_min_length():
    str = "cat dog cat bird cat dog"
    func_result = analyze_text_statistics(str, min_word_length=3)
    assert func_result['word_frequency'].get('cat') == 3
    assert func_result['word_frequency'].get('dog') == 2
    assert any(x['word'] == 'cat' for x in func_result['top_3_words'])
    pass

def test_top_3_words():
    str = "apple banana apple cherry apple banana cherry cherry cherry"
    func_result = analyze_text_statistics(str)
    assert func_result['top_3_words'][0]['word'] == 'cherry' and func_result['top_3_words'][0]['count'] == 4
    assert func_result['top_3_words'][1]['word'] == 'apple' and func_result['top_3_words'][1]['count'] == 3
    assert len(func_result['top_3_words']) == 3
    pass

# Дополнительные тесты
def test_unique_words_percentage():
    str = "test test test unique"
    func_result = analyze_text_statistics(str)
    assert func_result['unique_words_count'] == 2
    assert func_result['unique_words_percentage'] == 50.0
    pass

def test_average_word_length():
    str = "ab abc abcd"
    func_result = analyze_text_statistics(str)
    assert func_result['average_word_length'] == pytest.approx(3.0, rel=0.01)
    pass

def test_text_with_punctuation():
    str = "Hello, world! How are you?"
    func_result = analyze_text_statistics(str)
    assert func_result['total_sentences'] == 2
    assert func_result['total_words'] == 5
    pass

def test_text_without_valid_words():
    str = "!!! ??? ..."
    func_result = analyze_text_statistics(str)
    assert func_result['total_words'] == 0
    assert func_result['longest_word'] == None
    pass

def test_custom_min_word_length():
    str = "I am ok but you are great"
    func_result = analyze_text_statistics(str, min_word_length=4)
    assert any(len(x) < 4 for x in func_result['word_frequency'].keys()) == False
    assert func_result['word_frequency'].get('great') != None
    pass

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
