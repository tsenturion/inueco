import pytest
from complex_func import analyze_text_statistics


class TestAnalyzeTextStatistics:

    def test_complex_func_base_total_characters(self):
        analyze_text = analyze_text_statistics("Hello World!", 2)
        assert analyze_text["total_characters"] == 12


    def test_complex_func_base_total_word(self):
        analyze_text = analyze_text_statistics("One two three four five", 2)
        assert analyze_text["total_words"] == 5


    def test_complex_func_base_total_sentences(self):
        analyze_text = analyze_text_statistics("Hello World! My Tests", 2)
        assert analyze_text["total_sentences"] == 2

    
    def test_complex_func_base_longest_word(self):
        analyze_text = analyze_text_statistics("Hello World!", 2)
        assert analyze_text["longest_word"] != None


    def test_complex_func_raise_text_long_whitespace(self):
        with pytest.raises(ValueError) as e:
            analyze_text_statistics("           ", 2)
        assert str(e.value) != None


    def test_complex_func_raise_text_int(self):
        with pytest.raises(TypeError) as e:
            analyze_text_statistics(12333, 2)
        assert str(e.value) != None


    def test_complex_func_raise_text_none(self):
        with pytest.raises(TypeError) as e:
            analyze_text_statistics(None, 2)
        assert str(e.value) != None


    def test_complex_func_raise_word_lenght_none(self):
        with pytest.raises(TypeError) as e:
            analyze_text_statistics("Привет мир!", None)
        assert str(e.value) != None
    

    def test_complex_func_raise_all_none(self):
        with pytest.raises(TypeError) as e:
            analyze_text_statistics(None, None)
        assert str(e.value) != None


    def test_complex_func_longest_and_shortest_word(self):
        analyze_text = analyze_text_statistics("Привет мир!", 2)
        assert analyze_text["longest_word"] == "привет"
        assert analyze_text["shortest_word"] == "мир"


    def test_complex_func_average_word(self):
        analyze_text = analyze_text_statistics("Привет мир!", 2)
        assert analyze_text["average_word_length"] == pytest.approx(4.5, rel=0.01)


    def test_complex_func_unique_words_count(self):
        analyze_text = analyze_text_statistics("test test test unique", 2)
        assert analyze_text["unique_words_count"] == 2
        assert analyze_text["unique_words_percentage"] == pytest.approx(50.0, rel=0.01)


    def test_complex_func_top_3_words(self):
        analyze_text = analyze_text_statistics("cat dog cat bird cat dog", 2)
        assert analyze_text["top_3_words"][0]["count"] == 3 and analyze_text["top_3_words"][0]["word"] == "cat"
        assert analyze_text["top_3_words"][1]["count"] == 2 and analyze_text["top_3_words"][1]["word"] == "dog"


    def test_complex_func_without_valid_words(self):
        analyze_text = analyze_text_statistics("!!! , : &????", 2)
        assert analyze_text["total_words"] == 0
        assert analyze_text["longest_word"] == None


    def test_complex_func_min_word_length(self):
        analyze_text = analyze_text_statistics("I am ok but you are great", 4)
        assert "great" in analyze_text["word_frequency"]
        assert len(analyze_text["word_frequency"]) == 1


    def test_complex_func_raise_negative_word_length(self):
        with pytest.raises(ValueError) as e:
            analyze_text_statistics("Hello World", -55)
        assert str(e.value) != None


    def test_complex_func_raise_null_lenght_text(self):
        with pytest.raises(ValueError) as e:
            analyze_text_statistics("", 10)
        assert str(e.value) != None


    def test_complex_func_raise_lenght_min_object(self):
        with pytest.raises(TypeError) as e:
            analyze_text_statistics("test test test unique", str)
        assert str(e.value) != None
        

    def test_complex_func_raise_text_object(self):
        with pytest.raises(TypeError) as e:
            analyze_text_statistics(object, 11)
        assert str(e.value) != None


    def test_complex_func_raise_lenght_min_string(self):
        with pytest.raises(TypeError) as e:
            analyze_text_statistics("test test test unique", "string")
        assert str(e.value) != None


    def test_complex_func_raise_lenght_min_bool(self):
        assert analyze_text_statistics("test test test unique", True) != None