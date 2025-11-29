import requests
import time
import os
from typing import List, Dict
import json

def get_vacancies(search_text: str = '"Data Engineer"', area: int = 113, per_page: int = 100) -> List[Dict]:
    """
    Получает вакансии с API HH.ru

    Args:
        search_text: Текст для поиска (в кавычках для точного совпадения)
        area: ID региона (113 - Россия)
        per_page: Количество вакансий на странице (макс. 100)

    Returns:
        Список вакансий
    """
    base_url = "https://api.hh.ru/vacancies"
    vacancies = []
    page = 0
    pages = 1

    while page < pages:
        params = {
            'text': search_text,
            'search_field': 'name',  # Ищем именно в названии вакансии
            'area': area,
            'per_page': per_page,
            'page': page,
            'only_with_salary': False
        }

        try:
            response = requests.get(base_url, params=params)
            response.raise_for_status()
            data = response.json()

            vacancies.extend(data.get('items', []))
            pages = data.get('pages', 1)
            found = data.get('found', 0)

            print(f"Обработана страница {page + 1}/{pages}. Найдено вакансий: {found}")

            page += 1

            # Пауза чтобы не превысить лимиты API
            time.sleep(0.5)

        except requests.exceptions.RequestException as e:
            print(f"Ошибка при запросе: {e}")
            break

    return vacancies

def safe_lower(text):
    """
    Безопасное приведение к нижнему регистру
    """
    if text is None:
        return ""
    return text.lower()

def analyze_technology_in_vacancies(vacancies: List[Dict], technology: str) -> Dict:
    """
    Анализирует вакансии на наличие упоминаний указанной технологии

    Args:
        vacancies: Список вакансий
        technology: Технология для поиска (например: 'redis', 'python')

    Returns:
        Статистика по технологии
    """
    total_vacancies = len(vacancies)
    tech_vacancies = 0
    tech_vacancies_details = []

    # Приводим технологию к нижнему регистру для поиска
    tech_lower = technology.lower()

    for vacancy in vacancies:
        vacancy_id = vacancy.get('id')
        vacancy_name = vacancy.get('name', '')
        vacancy_url = vacancy.get('alternate_url', '')

        # Проверяем название и описание
        snippet = vacancy.get('snippet', {}) or {}
        requirement = safe_lower(snippet.get('requirement'))
        responsibility = safe_lower(snippet.get('responsibility'))

        # Получаем полное описание вакансии
        description = safe_lower(get_vacancy_description(vacancy_id))

        # Объединяем весь текст для поиска
        all_text = " ".join([
            safe_lower(vacancy_name),
            requirement,
            responsibility,
            description
        ])

        # Ищем указанную технологию
        has_tech = tech_lower in all_text

        if has_tech:
            tech_vacancies += 1
            tech_vacancies_details.append({
                'name': vacancy_name,
                'url': vacancy_url,
                'id': vacancy_id
            })

    return {
        'total_vacancies': total_vacancies,
        'tech_vacancies': tech_vacancies,
        'tech_percentage': (tech_vacancies / total_vacancies * 100) if total_vacancies > 0 else 0,
        'tech_vacancies_details': tech_vacancies_details,
        'technology': technology
    }

def get_vacancy_description(vacancy_id: str) -> str:
    """
    Получает полное описание вакансии по ID

    Args:
        vacancy_id: ID вакансии

    Returns:
        Текст описания вакансии
    """
    try:
        url = f"https://api.hh.ru/vacancies/{vacancy_id}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        description = data.get('description', '')
        return description

    except requests.exceptions.RequestException:
        return ""

def print_statistics(stats: Dict, vacancy_title: str):
    """
    Выводит статистику в читаемом формате
    """
    technology = stats['technology']
    print("\n" + "="*50)
    print(f"СТАТИСТИКА ПО ВАКАНСИЯМ: {vacancy_title.upper()}")
    print(f"Анализ технологии: {technology.upper()}")
    print("="*50)
    print(f"Всего вакансий найдено: {stats['total_vacancies']}")
    print(f"Вакансий с {technology}: {stats['tech_vacancies']}")
    print(f"Процент вакансий с {technology}: {stats['tech_percentage']:.2f}%")
    print("\n" + "-"*50)

    if stats['tech_vacancies_details']:
        print(f"Вакансии с {technology}:")
        for i, vacancy in enumerate(stats['tech_vacancies_details'][:10], 1):
            print(f"{i}. {vacancy['name']}")
            print(f"   Ссылка: {vacancy['url']}")

        if len(stats['tech_vacancies_details']) > 10:
            print(f"... и еще {len(stats['tech_vacancies_details']) - 10} вакансий")
    else:
        print(f"Вакансии с {technology} не найдены")

def ensure_results_dir():
    """
    Создает папку results, если она не существует
    """
    results_dir = "results"
    if not os.path.exists(results_dir):
        os.makedirs(results_dir)
        print(f"Создана папка {results_dir}")
    return results_dir

def save_results_to_file(stats: Dict, vacancy_title: str, filename: str = None):
    """
    Сохраняет результаты анализа в файл в папке results
    """
    # Создаем папку results, если её нет
    results_dir = ensure_results_dir()
    
    if filename is None:
        technology = stats['technology']
        # Создаем безопасное имя файла из названия вакансии и технологии
        safe_vacancy_title = "".join(c for c in vacancy_title if c.isalnum() or c in (' ', '-', '_')).rstrip()
        safe_vacancy_title = safe_vacancy_title.replace(' ', '_')
        filename = f"{safe_vacancy_title}_{technology}_analysis_results.json"

    # Формируем полный путь к файлу
    filepath = os.path.join(results_dir, filename)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        # Добавляем название вакансии в результаты
        results = stats.copy()
        results['vacancy_title'] = vacancy_title
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"\nРезультаты сохранены в файл: {filepath}")
    
    return filepath

# Альтернативная версия main с возможностью задания параметров через код
def main_with_params(vacancy_title="Data Engineer", technology="python", area=113, per_page=100) -> Dict:
    """
    Версия main с параметрами для вызова из кода
    """
    # Формируем поисковый запрос с кавычками для точного совпадения
    search_query = f'"{vacancy_title}"'

    print(f"\nНачинаем сбор вакансий '{vacancy_title}' с поиском технологии: {technology}")

    # Получаем вакансии с точным поиском по названию
    vacancies = get_vacancies(
        search_text=search_query,
        area=area,
        per_page=per_page
    )

    if not vacancies:
        print("Не удалось получить вакансии")
        return

    print(f"\nПолучено {len(vacancies)} вакансий")

    # Анализируем наличие указанной технологии
    print(f"Анализируем вакансии на наличие {technology}...")
    stats = analyze_technology_in_vacancies(vacancies, technology)

    # Выводим результаты
    print_statistics(stats, vacancy_title)

    # Сохраняем в файл в папке results
    filename = f"{time.time()}.json"
    save_results_to_file({"stats": stats, "vacancies": vacancies}, vacancy_title, filename)

    return {"stats": stats, "vacancies": vacancies, "resultID": filename.split('.json')[0]}