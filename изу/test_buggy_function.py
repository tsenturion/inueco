from buggy_function import process_student_scores

def test_normal_data():
    """Тест с обычными корректными данными"""
    students_data = [
        {"name": "Иван", "scores": [85, 90, 78], "age": 20},
        {"name": "Мария", "scores": [55, 60, 50], "age": 18},
        {"name": "Петр", "scores": [70, 75, 80], "age": 19}
    ]
    
    result = process_student_scores(students_data)
    
    assert result["total_students"] == 3
    assert result["average_score"] == 71.44  
    assert result["top_student"] == "Иван"
    assert result["failed_students"] == ["Мария"]  
    assert result["adults_count"] == 3  


def test_empty_list():
    """Тест с пустым списком студентов"""
    result = process_student_scores([])
    assert result is None


def test_student_with_empty_scores():
    """Тест со студентом без оценок - должен обработаться корректно, но упадет из-за ОШИБКИ 1"""
    students_data = [
        {"name": "Иван", "scores": [], "age": 20}
    ]

    result = process_student_scores(students_data)
    assert result is not None
    assert result["total_students"] == 1


def test_single_student():
    """Тест с одним студентом"""
    students_data = [
        {"name": "Анна", "scores": [95, 98, 100], "age": 21}
    ]
    
    result = process_student_scores(students_data)
    
    assert result["total_students"] == 1
    assert result["average_score"] == 97.67
    assert result["top_student"] == "Анна"
    assert result["failed_students"] == []
    assert result["adults_count"] == 1


def test_failed_students_boundary():
    """Тест подсчета неуспевающих - упадет из-за ОШИБКИ 2"""
    students_data = [
        {"name": "Студент1", "scores": [59], "age": 20},  
        {"name": "Студент2", "scores": [60], "age": 20}, 
        {"name": "Студент3", "scores": [50], "age": 20}, 
    ]
    
    result = process_student_scores(students_data)
    
    expected = ["Студент1", "Студент3"]
    actual = result["failed_students"]
    
    assert actual == expected, f"Ожидалось {expected}, получено {actual}"


def test_adults_count_boundary():
    """Тест подсчета совершеннолетних - упадет из-за ОШИБКИ 3"""
    students_data = [
        {"name": "Студент1", "scores": [70], "age": 17},  
        {"name": "Студент2", "scores": [70], "age": 18},  
        {"name": "Студент3", "scores": [70], "age": 19},  
        {"name": "Студент4", "scores": [70], "age": 20}, 
    ]
    
    result = process_student_scores(students_data)
    
    expected = 3
    actual = result["adults_count"]
    
    assert actual == expected, f"Ожидалось {expected}, получено {actual}"


def test_top_student():
    """Тест определения лучшего студента"""
    students_data = [
        {"name": "Слабый", "scores": [50, 55, 60], "age": 18},
        {"name": "Средний", "scores": [70, 75, 80], "age": 19},
        {"name": "Отличник", "scores": [95, 98, 100], "age": 20},
        {"name": "Хороший", "scores": [85, 88, 90], "age": 21},
    ]
    
    result = process_student_scores(students_data)
    
    assert result["top_student"] == "Отличник"
    assert result["average_score"] == 78.75


def test_all_students_with_empty_scores():
    """Тест когда у всех студентов нет оценок - упадет из-за ОШИБКИ 1 и ОШИБКИ 4"""
    students_data = [
        {"name": "Студент1", "scores": [], "age": 20},
        {"name": "Студент2", "scores": [], "age": 21}
    ]
    
    result = process_student_scores(students_data)
    assert result is not None
    assert result["total_students"] == 2


def test_rounding_to_two_decimals():
    """Тест округления до 2 знаков после запятой"""
    students_data = [
        {"name": "Студент", "scores": [10, 15, 13], "age": 20}
    ]
    
    result = process_student_scores(students_data)

    assert result["average_score"] == 12.67


def test_student_exactly_60_should_not_fail():
    """Тест: студент с баллом 60 НЕ должен быть неуспевающим - упадет из-за ОШИБКИ 2"""
    students_data = [
        {"name": "Граница", "scores": [60], "age": 20}
    ]
    
    result = process_student_scores(students_data)
    
    assert "Граница" not in result["failed_students"], f"Студент с баллом 60 не должен быть неуспевающим, но в списке: {result['failed_students']}"


def test_student_exactly_18_should_be_adult():
    """Тест: студент 18 лет должен быть взрослым - упадет из-за ОШИБКИ 3"""
    students_data = [
        {"name": "Восемнадцать", "scores": [70], "age": 18}
    ]
    
    result = process_student_scores(students_data)
    
    assert result["adults_count"] == 1, f"Студент 18 лет должен быть взрослым, но получено: {result['adults_count']}"


if __name__ == "__main__":
    print(" Запуск тестов для функции process_student_scores...\n")
    
    tests = [
        ("test_normal_data", test_normal_data),
        ("test_empty_list", test_empty_list),
        ("test_student_with_empty_scores", test_student_with_empty_scores),
        ("test_single_student", test_single_student),
        ("test_failed_students_boundary", test_failed_students_boundary),
        ("test_adults_count_boundary", test_adults_count_boundary),
        ("test_top_student", test_top_student),
        ("test_all_students_with_empty_scores", test_all_students_with_empty_scores),
        ("test_rounding_to_two_decimals", test_rounding_to_two_decimals),
        ("test_student_exactly_60_should_not_fail", test_student_exactly_60_should_not_fail),
        ("test_student_exactly_18_should_be_adult", test_student_exactly_18_should_be_adult),
    ]
    
    passed = 0
    failed = 0
    error_1_tests = []
    error_2_tests = []
    error_3_tests = []  
    error_4_tests = []  
    for test_name, test_func in tests:
        try:
            test_func()
            print(f" {test_name}: PASSED")
            passed += 1
        except ZeroDivisionError as e:
            print(f" {test_name}: FAILED - ZeroDivisionError (деление на ноль)")
            failed += 1
            if "empty_scores" in test_name:
                error_1_tests.append(test_name)
                if "all_students" in test_name:
                    error_4_tests.append(test_name)
        except AssertionError as e:
            error_msg = str(e)
            print(f" {test_name}: FAILED {error_msg}")
            failed += 1
            
            # Определяем какую ошибку обнаружил тест
            if "60" in error_msg or "failed_students" in error_msg.lower() or "неуспевающ" in error_msg:
                error_2_tests.append(test_name)
            if "18" in error_msg or "adults" in error_msg.lower() or "взросл" in error_msg:
                error_3_tests.append(test_name)
            if not ("60" in error_msg or "18" in error_msg) and ("adults_count" in test_name or "failed_students" in test_name):
     
                error_2_tests.append(test_name)
                error_3_tests.append(test_name)
        except Exception as e:
            print(f" {test_name}: ERROR - {type(e).__name__}")
            failed += 1
    
    # Убираем дубликаты
    error_2_tests = list(set(error_2_tests))
    error_3_tests = list(set(error_3_tests))
    
    print(f"\n{'='*70}")
    print(f" ИТОГОВЫЕ РЕЗУЛЬТАТЫ ТЕСТИРОВАНИЯ")
    print(f"{'='*70}")
    print(f"\n Статистика:")
    print(f"• Всего тестов запущено: {len(tests)}")
    print(f"• Пройдено: {passed}")
    print(f"• Провалено: {failed}")
    print(f"\n Провалившиеся тесты обнаружили ошибки в функции!")
    
    # Подсчитываем уникальные ошибки
    unique_errors = []
    if error_1_tests:
        unique_errors.append("ОШИБКА 1")
    if error_2_tests:
        unique_errors.append("ОШИБКА 2")
    if error_3_tests:
        unique_errors.append("ОШИБКА 3")
    if error_4_tests:
        unique_errors.append("ОШИБКА 4")
    
    print(f"\n{'='*70}")
    print(f"ОБНАРУЖЕНО ОШИБОК В ФУНКЦИИ: {len(unique_errors)} из 4")
    print(f"{'='*70}")
    
    if error_1_tests:
        print(f"\nОШИБКА 1: Деление на ноль при пустом списке оценок")
        print(f"   Местоположение: строка 35")
        print(f"   Код: student_avg = sum(scores) / len(scores)")
        print(f"   Обнаружено тестами ({len(error_1_tests)}):")
        for test in error_1_tests:
            print(f"      • {test}")
    
    if error_2_tests:
        print(f"\nОШИБКА 2: Неправильное условие для неуспевающих (<= вместо <)")
        print(f"Местоположение: строка 41")
        print(f"Код: if student_avg <= 60:")
        print(f"Должно быть: if student_avg < 60:")
        print(f"Обнаружено тестами ({len(error_2_tests)}):")
        for test in error_2_tests:
            print(f"• {test}")
    
    if error_3_tests:
        print(f"\nОШИБКА 3: Неправильное условие для совершеннолетних (> вместо >=)")
        print(f"Местоположение: строка 45")
        print(f"Код: if age > 18:")
        print(f"Должно быть: if age >= 18:")
        print(f"Обнаружено тестами ({len(error_3_tests)}):")
        for test in error_3_tests:
            print(f"• {test}")
    
    if error_4_tests:
        print(f"\n ОШИБКА 4: Деление на ноль при пустом списке all_scores")
        print(f"Местоположение: строка 49")
        print(f"Код: average_score = sum(all_scores) / len(all_scores)")
        print(f"Обнаружено тестами ({len(error_4_tests)}):")
        for test in error_4_tests:
            print(f"• {test}")
    
    print(f"\n{'='*70}")
    if len(unique_errors) == 4:
        print(f"Все 4 ошибки успешно обнаружены тестами!")
    else:
        print(f"Обнаружено {len(unique_errors)} из 4 ошибок")
    print(f"{'='*70}")
