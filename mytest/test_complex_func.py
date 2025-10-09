import pytest
from complex_func import analyze_text_statistics


def test_basic_text_analysis():

    text = "Hello world! Python is great."
    result = analyze_text_statistics(text)
    
    assert result["total_words"] > 0
    
    assert result["total_sentences"] == 2
    
    assert result["longest_word"] is not None
    
    assert result["total_words"] == 5
    assert result["longest_word"] == "python"
    assert result["total_characters"] == 29
    assert result["average_word_length"] == pytest.approx(4.6, rel=0.01)
def test_empty_text_raises_error():

    with pytest.raises(ValueError):
        analyze_text_statistics("")


def test_whitespace_only_raises_error():

    with pytest.raises(ValueError):
        analyze_text_statistics(" ")
    
    with pytest.raises(ValueError):
        analyze_text_statistics("   ")
    
    with pytest.raises(ValueError):
        analyze_text_statistics("\t")
    
    with pytest.raises(ValueError):
        analyze_text_statistics("\n")

def test_invalid_type_raises_error():

    with pytest.raises(TypeError):
        analyze_text_statistics(123)
    
    with pytest.raises(TypeError):
        analyze_text_statistics(["test"])
    
    with pytest.raises(TypeError):
        analyze_text_statistics(None)
    
    with pytest.raises(TypeError):
        analyze_text_statistics({"key": "value"})


def test_text_with_punctuation():

    text = "Hello, world! How are you? I'm fine; thanks."
    result = analyze_text_statistics(text)
    
    assert result["total_words"] == 9
    assert result["total_sentences"] == 3
    assert result["longest_word"] == "thanks"


def test_text_with_numbers():

    text = "I have 3 apples and 15 oranges. Total 18 fruits."
    result = analyze_text_statistics(text)
    
    assert result["total_words"] == 10
    assert result["total_sentences"] == 2
    assert result["longest_word"] == "oranges"


def test_single_word_text():

    text = "Hello"
    result = analyze_text_statistics(text)
    
    assert result["total_words"] == 1
    assert result["total_sentences"] == 1
    assert result["longest_word"] == "hello"  
    assert result["average_word_length"] == pytest.approx(5.0, rel=0.01)


def test_text_with_multiple_spaces():

    text = "Hello    world!  How   are   you?"
    result = analyze_text_statistics(text)
    
    assert result["total_words"] == 5
    assert result["total_sentences"] == 2
    assert result["longest_word"] is not None


def test_text_with_special_characters():

    text = "Email: test@example.com, URL: https://example.com"
    result = analyze_text_statistics(text)
    
    assert result["total_words"] == 8
    assert result["total_sentences"] == 3
    assert len(result["longest_word"]) > 0


def test_text_with_mixed_case():

    text = "Python is AWESOME! JavaScript is also great."
    result = analyze_text_statistics(text)
    
    assert result["total_words"] == 7
    assert result["total_sentences"] == 2
    assert len(result["longest_word"]) >= len("javascript")


def test_text_with_unicode():

    text = "Привет мир! Hello world! こんにちは世界!"
    result = analyze_text_statistics(text)
    
    assert result["total_words"] == 5
    assert result["total_sentences"] == 3
    assert result["total_characters"] > 0


def test_average_word_length_calculation():

    text = "a bb ccc dddd eeeee"
    result = analyze_text_statistics(text)
    
    assert result["average_word_length"] == pytest.approx(3.0, rel=0.01)
    assert result["total_words"] == 5


def test_complex_sentence_detection():

    text = "This is sentence one. Is this sentence two? What about three! And four; maybe five..."
    result = analyze_text_statistics(text)
    
    assert result["total_sentences"] == 4
    assert result["total_words"] == 15

def test_word_count():

    text = "One two three four five"
    result = analyze_text_statistics(text)
    assert result["total_words"] == 5


def test_character_count():
    """Тест подсчета символов"""
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
    """Тест частоты слов с минимальной длиной"""
    text = "cat dog cat bird cat dog"
    result = analyze_text_statistics(text, min_word_length=3)

    assert "cat" in result["word_frequency"]
    assert "dog" in result["word_frequency"]
    assert "bird" in result["word_frequency"]

    assert result["word_frequency"]["cat"] == 3
    assert result["word_frequency"]["dog"] == 2

    top_words = [item["word"] if isinstance(item, dict) else item[0] for item in result["top_3_words"]]
    assert "cat" in top_words


def test_top_3_words():
    """Тест топ-3 слов"""
    text = "apple banana apple cherry apple banana cherry cherry cherry"
    result = analyze_text_statistics(text)

    assert len(result["top_3_words"]) == 3

    first_item = result["top_3_words"][0]
    if isinstance(first_item, dict):

        assert first_item["word"] == "cherry"
        assert first_item["count"] == 4
        
        second_item = result["top_3_words"][1]
        assert second_item["word"] == "apple"
        assert second_item["count"] == 3
    else:
        assert first_item[0] == "cherry"
        assert first_item[1] == 4
        
        second_item = result["top_3_words"][1]
        assert second_item[0] == "apple"
        assert second_item[1] == 3