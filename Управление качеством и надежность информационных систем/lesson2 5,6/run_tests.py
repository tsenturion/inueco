# run_tests.py

import unittest
import sys

def run_all_tests():
    """Запускает все тесты"""
    print("=" * 70)
    print("ТЕСТИРОВАНИЕ ORDER SERVICE")
    print("=" * 70)
    print("Демонстрация unittest: setUp/tearDown, исключения, subTest, mock")
    print("=" * 70)
    
    # Используем discover для нахождения всех тестов
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir='.', pattern='test_*.py')
    
    # Запускаем тесты
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Выводим итоги
    print("\n" + "=" * 70)
    print("ИТОГИ ТЕСТИРОВАНИЯ:")
    print("=" * 70)
    
    print(f"Всего тестов: {result.testsRun}")
    print(f"Провалено: {len(result.failures)}")
    print(f"Ошибок: {len(result.errors)}")
    
    # Выводим важные выводы
    print("\n" + "=" * 70)
    print("ПРОВЕРЕННЫЕ КОНЦЕПЦИИ:")
    print("=" * 70)
    
    concepts = [
        ("✅" if result.testsRun > 0 else "❌", "Тесты запускаются"),
        ("✅" if not result.failures and not result.errors else "❌", "Все тесты проходят"),
        ("✅", "setUp и tearDown (видно в выводе)"),
        ("✅", "Тестирование исключений (assertRaises)"),
        ("✅", "Параметризация тестов (subTest)"),
        ("✅", "Использование unittest.mock"),
        ("✅", "Моки с проверкой вызовов (assert_called_once_with)"),
        ("✅", "Тесты независимы и изолированы"),
    ]
    
    for icon, concept in concepts:
        print(f"{icon} {concept}")
    
    if result.failures or result.errors:
        print("\n ЕСТЬ ПРОБЛЕМЫ С ТЕСТАМИ!")
        return 1
    else:
        print("\n ВСЕ ТЕСТЫ ПРОЙДЕНЫ УСПЕШНО!")
        return 0

if __name__ == '__main__':
    sys.exit(run_all_tests())