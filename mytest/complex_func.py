def analyze_text_statistics(text: str, min_word_length: int = 3) -> dict:
    """
    Анализирует текст и возвращает подробную статистику.
    
    Функция выполняет комплексный анализ текста:
    - Подсчитывает общее количество символов, слов и предложений
    - Находит самое длинное и самое короткое слово
    - Подсчитывает частоту встречаемости слов (игнорируя слова короче min_word_length)
    - Определяет топ-3 самых частых слова
    - Вычисляет среднюю длину слова
    - Подсчитывает количество уникальных слов
    - Определяет процент уникальных слов от общего количества
    
    Args:
        text (str): Текст для анализа
        min_word_length (int): Минимальная длина слова для подсчета частоты (по умолчанию 3)
    
    Returns:
        dict: Словарь со статистикой текста
    
    Raises:
        ValueError: Если текст пустой или содержит только пробелы
        TypeError: Если text не является строкой
    """
    
    # Валидация входных данных
    if not isinstance(text, str):
        raise TypeError("Текст должен быть строкой")
    
    if not text.strip():
        raise ValueError("Текст не может быть пустым")
    
    # Подсчет общего количества символов (без пробелов в начале и конце)
    total_chars = len(text.strip())
    
    # Разделение на предложения (по точкам, восклицательным и вопросительным знакам)
    sentences = []
    current_sentence = ""
    prev_char_is_punctuation = False
    
    for char in text:
        if char in '.!?':
            current_sentence += char
            # Добавляем предложение только при первом знаке препинания подряд
            if not prev_char_is_punctuation:
                if current_sentence.strip():
                    sentences.append(current_sentence.strip())
                current_sentence = ""
            prev_char_is_punctuation = True
        else:
            current_sentence += char
            prev_char_is_punctuation = False
    
    if current_sentence.strip():
        sentences.append(current_sentence.strip())
    
    sentence_count = len(sentences)
    
    # Обработка слов
    words = []
    current_word = ""
    for char in text.lower():
        if char.isalpha() or char.isdigit():
            current_word += char
        else:
            if current_word:
                words.append(current_word)
                current_word = ""
    if current_word:
        words.append(current_word)
    
    # Проверка наличия слов
    if not words:
        return {
            "total_characters": total_chars,
            "total_words": 0,
            "total_sentences": sentence_count,
            "longest_word": None,
            "shortest_word": None,
            "average_word_length": 0.0,
            "unique_words_count": 0,
            "unique_words_percentage": 0.0,
            "top_3_words": [],
            "word_frequency": {}
        }
    
    total_words = len(words)
    
    # Поиск самого длинного и короткого слова
    longest_word = max(words, key=len)
    shortest_word = min(words, key=len)
    
    # Вычисление средней длины слова
    total_length = sum(len(word) for word in words)
    average_length = round(total_length / total_words, 2)
    
    # Подсчет частоты слов (только слова >= min_word_length)
    word_frequency = {}
    for word in words:
        if len(word) >= min_word_length:
            word_frequency[word] = word_frequency.get(word, 0) + 1
    
    # Поиск топ-3 самых частых слов
    sorted_words = sorted(word_frequency.items(), key=lambda x: (-x[1], x[0]))
    top_3_words = [{"word": word, "count": count} for word, count in sorted_words[:3]]
    
    # Подсчет уникальных слов
    unique_words = set(words)
    unique_count = len(unique_words)
    unique_percentage = round((unique_count / total_words) * 100, 2)
    
    return {
        "total_characters": total_chars,
        "total_words": total_words,
        "total_sentences": sentence_count,
        "longest_word": longest_word,
        "shortest_word": shortest_word,
        "average_word_length": average_length,
        "unique_words_count": unique_count,
        "unique_words_percentage": unique_percentage,
        "top_3_words": top_3_words,
        "word_frequency": word_frequency
    }


# Пример использования
if __name__ == "__main__":
    sample_text = """
    Python - это высокоуровневый язык программирования. Python используется 
    для веб-разработки, анализа данных и машинного обучения. Python очень популярен!
    """
    
    result = analyze_text_statistics(sample_text)
    
    print("=== СТАТИСТИКА ТЕКСТА ===")
    print(f"Всего символов: {result['total_characters']}")
    print(f"Всего слов: {result['total_words']}")
    print(f"Всего предложений: {result['total_sentences']}")
    print(f"Самое длинное слово: {result['longest_word']}")
    print(f"Самое короткое слово: {result['shortest_word']}")
    print(f"Средняя длина слова: {result['average_word_length']}")
    print(f"Уникальных слов: {result['unique_words_count']} ({result['unique_words_percentage']}%)")
    print(f"\nТоп-3 самых частых слова:")
    for item in result['top_3_words']:
        print(f"  - {item['word']}: {item['count']} раз")