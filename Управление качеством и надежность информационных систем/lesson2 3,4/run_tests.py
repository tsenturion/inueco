#!/usr/bin/env python3
"""
Скрипт для запуска всех тестов
"""

import unittest
import sys

def run_all_tests():
    """Запускает все доступные тесты"""
    print("=" * 70)
    print("СИСТЕМА ТЕСТИРОВАНИЯ TASK MANAGER")
    print("=" * 70)
    
    # Находим все тесты
    loader = unittest.TestLoader()
    
    # Итоговые результаты
    total_tests = 0
    total_failures = 0
    total_errors = 0
    
    # Запускаем тесты из test_task_manager.py
    try:
        print("\n ЗАПУСК БАЗОВЫХ ТЕСТОВ:")
        print("-" * 50)
        
        import test_task_manager
        suite1 = loader.loadTestsFromModule(test_task_manager)
        runner1 = unittest.TextTestRunner(verbosity=2)
        result1 = runner1.run(suite1)
        
        total_tests += result1.testsRun
        total_failures += len(result1.failures)
        total_errors += len(result1.errors)
    except ImportError as e:
        print(f" Ошибка: Не удалось загрузить test_task_manager.py")
        print(f"   Подробности: {e}")
        print("   Убедитесь, что файл существует в той же директории")
        return 1
    
    # Запускаем тесты из test_task_manager_with_resources.py (если существует)
    try:
        print("\n" + "=" * 70)
        print(" ЗАПУСК ТЕСТОВ С РЕСУРСАМИ:")
        print("-" * 50)
        
        import test_task_manager_with_resources
        suite2 = loader.loadTestsFromModule(test_task_manager_with_resources)
        runner2 = unittest.TextTestRunner(verbosity=2)
        result2 = runner2.run(suite2)
        
        total_tests += result2.testsRun
        total_failures += len(result2.failures)
        total_errors += len(result2.errors)
    except ImportError:
        print("  Файл test_task_manager_with_resources.py не найден")
        print("   Пропускаем тесты с ресурсами...")
    
    # Итоговый результат
    print("\n" + "=" * 70)
    print(" ИТОГИ:")
    print("=" * 70)
    
    print(f"Всего тестов выполнено: {total_tests}")
    print(f"Провалов (failures): {total_failures}")
    print(f"Ошибок (errors): {total_errors}")
    
    if total_failures == 0 and total_errors == 0:
        print("\n ВСЕ ТЕСТЫ ПРОЙДЕНЫ УСПЕШНО!")
        return 0
    else:
        print("\n ЕСТЬ ПРОБЛЕМЫ С ТЕСТАМИ!")
        
        # Выводим информацию о проваленных тестах
        if hasattr('result1', 'failures') and result1.failures:
            print("\nПроваленные тесты из test_task_manager.py:")
            for test, traceback in result1.failures:
                print(f"  - {test}")
        
        if hasattr('result2', 'failures') and result2 and result2.failures:
            print("\nПроваленные тесты из test_task_manager_with_resources.py:")
            for test, traceback in result2.failures:
                print(f"  - {test}")
        
        return 1

def run_specific_test(test_name):
    """Запускает конкретный тест"""
    print(f"Запуск теста: {test_name}")
    print("-" * 50)
    
    try:
        # Формат: module.TestClass.test_method
        suite = unittest.defaultTestLoader.loadTestsFromName(test_name)
        runner = unittest.TextTestRunner(verbosity=2)
        result = runner.run(suite)
        
        if result.failures or result.errors:
            return 1
        return 0
    except Exception as e:
        print(f" Ошибка при запуске теста: {e}")
        return 1

if __name__ == '__main__':
    # Проверяем аргументы командной строки
    if len(sys.argv) > 1:
        # Запускаем конкретный тест
        test_to_run = sys.argv[1]
        sys.exit(run_specific_test(test_to_run))
    else:
        # Запускаем все тесты
        sys.exit(run_all_tests())