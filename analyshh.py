import requests
import time
import os
from typing import List, Dict
import json
import concurrent.futures
from functools import lru_cache
import re
from threading import Lock

# Глобальные настройки
MAX_WORKERS = 5
REQUEST_DELAY = 0.1
MAX_REQUESTS_PER_SECOND = 7

# Счетчики и блокировки
request_counter = 0
cached_requests_counter = 0
counter_lock = Lock()
last_request_time = time.time()
rate_limit_lock = Lock()

def increment_request_counter(use_cache=False):
    """
    Увеличивает счетчик запросов и контролирует rate limiting
    """
    global request_counter, cached_requests_counter, last_request_time
    
    with counter_lock:
        if use_cache:
            cached_requests_counter += 1
        else:
            request_counter += 1
            current_time = time.time()
            
            # Контроль rate limiting только для реальных запросов
            with rate_limit_lock:
                time_since_last_request = current_time - last_request_time
                if time_since_last_request < (1.0 / MAX_REQUESTS_PER_SECOND):
                    sleep_time = (1.0 / MAX_REQUESTS_PER_SECOND) - time_since_last_request
                    time.sleep(sleep_time)
                
                last_request_time = time.time()
        
        return request_counter, cached_requests_counter

def get_request_count():
    """
    Возвращает текущее количество выполненных запросов
    """
    with counter_lock:
        return request_counter, cached_requests_counter

def reset_request_counters():
    """
    Сбрасывает счетчики запросов
    """
    global request_counter, cached_requests_counter
    with counter_lock:
        request_counter = 0
        cached_requests_counter = 0

# Глобальный кэш для отслеживания запросов
description_cache = {}
cache_hits = 0
cache_misses = 0
cache_lock = Lock()

def get_vacancy_description_cached(vacancy_id: str) -> str:
    """
    Получает описание вакансии с кэшированием и подсчетом статистики
    """
    global cache_hits, cache_misses
    
    with cache_lock:
        if vacancy_id in description_cache:
            cache_hits += 1
            increment_request_counter(use_cache=True)
            return description_cache[vacancy_id]
    
    # Если нет в кэше, делаем реальный запрос
    try:
        url = f"https://api.hh.ru/vacancies/{vacancy_id}"
        response = requests.get(url)
        increment_request_counter(use_cache=False)  # Реальный запрос
        response.raise_for_status()
        data = response.json()

        description = data.get('description', '')
        
        with cache_lock:
            description_cache[vacancy_id] = description
            cache_misses += 1
        
        return description

    except requests.exceptions.RequestException:
        with cache_lock:
            description_cache[vacancy_id] = ""
            cache_misses += 1
        return ""

def get_cache_stats():
    """
    Возвращает статистику кэша
    """
    with cache_lock:
        total = cache_hits + cache_misses
        hit_rate = (cache_hits / total * 100) if total > 0 else 0
        return {
            'cache_hits': cache_hits,
            'cache_misses': cache_misses,
            'total_cache_requests': total,
            'cache_hit_rate': hit_rate,
            'cache_size': len(description_cache)
        }

def get_vacancies(search_text: str = '"Data Engineer"', area: int = 113, per_page: int = 100) -> List[Dict]:
    """
    Получает вакансии с API HH.ru с параллельной загрузкой страниц
    """
    base_url = "https://api.hh.ru/vacancies"
    
    # Сбрасываем счетчики в начале нового запроса
    reset_request_counters()
    
    # Сначала получаем информацию о количестве страниц
    try:
        params = {
            'text': search_text,
            'search_field': 'name',
            'area': area,
            'per_page': per_page,
            'page': 0,
            'only_with_salary': False
        }
        
        response = requests.get(base_url, params=params)
        increment_request_counter(use_cache=False)
        response.raise_for_status()
        data = response.json()
        
        total_pages = data.get('pages', 1)
        found = data.get('found', 0)
        
        real_requests, cached_requests = get_request_count()
        print(f"Всего найдено вакансий: {found}, страниц: {total_pages}")
        print(f"Запросов выполнено: {real_requests} реальных, {cached_requests} кэшированных")
        
        # Если страниц слишком много, ограничиваем для демонстрации
        if total_pages > 10:
            print(f"Ограничиваем количество страниц с {total_pages} до 10 для демонстрации")
            total_pages = 10
        
        # Загружаем все страницы параллельно
        vacancies = data.get('items', [])
        
        if total_pages > 1:
            with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
                future_to_page = {
                    executor.submit(fetch_single_page, base_url, search_text, area, per_page, page): page 
                    for page in range(1, total_pages)
                }
                
                for future in concurrent.futures.as_completed(future_to_page):
                    page = future_to_page[future]
                    try:
                        page_vacancies = future.result()
                        vacancies.extend(page_vacancies)
                        real_requests, cached_requests = get_request_count()
                        print(f"Загружена страница {page + 1}/{total_pages}. Запросов: {real_requests} реальных, {cached_requests} кэшированных")
                    except Exception as e:
                        print(f"Ошибка при загрузке страницы {page}: {e}")
            
            return vacancies
            
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе: {e}")
        return []

def fetch_single_page(base_url: str, search_text: str, area: int, per_page: int, page: int) -> List[Dict]:
    """
    Загружает одну страницу вакансий
    """
    params = {
        'text': search_text,
        'search_field': 'name',
        'area': area,
        'per_page': per_page,
        'page': page,
        'only_with_salary': False
    }
    
    response = requests.get(base_url, params=params)
    increment_request_counter(use_cache=False)
    response.raise_for_status()
    data = response.json()
    
    time.sleep(REQUEST_DELAY)
    
    return data.get('items', [])

def analyze_technology_in_vacancies_optimized(vacancies: List[Dict], technology: str) -> Dict:
    """
    Оптимизированный анализ вакансий на наличие указанной технологии
    """
    total_vacancies = len(vacancies)
    tech_lower = technology.lower()
    
    # Предварительно компилируем регулярное выражение для более быстрого поиска
    tech_pattern = re.compile(r'\b' + re.escape(tech_lower) + r'\b', re.IGNORECASE)
    
    tech_vacancies_details = []
    
    real_requests, cached_requests = get_request_count()
    print(f"Начинаем анализ {total_vacancies} вакансий...")
    print(f"Текущие запросы: {real_requests} реальных, {cached_requests} кэшированных")
    
    # Параллельная обработка вакансий
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        future_to_vacancy = {
            executor.submit(check_vacancy_for_tech, vacancy, tech_lower, tech_pattern): vacancy 
            for vacancy in vacancies
        }
        
        processed = 0
        for future in concurrent.futures.as_completed(future_to_vacancy):
            try:
                result = future.result()
                if result['has_tech']:
                    tech_vacancies_details.append(result['vacancy_info'])
                
                processed += 1
                if processed % 20 == 0:  # Выводим прогресс каждые 20 вакансий
                    real_requests, cached_requests = get_request_count()
                    cache_stats = get_cache_stats()
                    print(f"Обработано {processed}/{total_vacancies} вакансий. "
                          f"Запросы: {real_requests} реальных, {cached_requests} кэшированных. "
                          f"Кэш: {cache_stats['cache_hit_rate']:.1f}% попаданий")
                    
            except Exception as e:
                print(f"Ошибка при анализе вакансии: {e}")
                processed += 1
    
    tech_vacancies = len(tech_vacancies_details)
    
    return {
        'total_vacancies': total_vacancies,
        'tech_vacancies': tech_vacancies,
        'tech_percentage': (tech_vacancies / total_vacancies * 100) if total_vacancies > 0 else 0,
        'tech_vacancies_details': tech_vacancies_details,
        'technology': technology
    }

def check_vacancy_for_tech(vacancy: Dict, tech_lower: str, tech_pattern) -> Dict:
    """
    Проверяет одну вакансию на наличие технологии
    """
    vacancy_id = vacancy.get('id')
    vacancy_name = vacancy.get('name', '')
    vacancy_url = vacancy.get('alternate_url', '')

    # Проверяем название вакансии (самый быстрый способ)
    if tech_pattern.search(safe_lower(vacancy_name)):
        return {
            'has_tech': True,
            'vacancy_info': {
                'name': vacancy_name,
                'url': vacancy_url,
                'id': vacancy_id
            }
        }
    
    # Проверяем сниппет (быстрее чем полное описание)
    snippet = vacancy.get('snippet', {}) or {}
    requirement = safe_lower(snippet.get('requirement', ''))
    responsibility = safe_lower(snippet.get('responsibility', ''))
    
    snippet_text = requirement + " " + responsibility
    if tech_pattern.search(snippet_text):
        return {
            'has_tech': True,
            'vacancy_info': {
                'name': vacancy_name,
                'url': vacancy_url,
                'id': vacancy_id
            }
        }
    
    # Только если не нашли в названии и сниппете, загружаем полное описание
    description = safe_lower(get_vacancy_description_cached(vacancy_id))
    if tech_pattern.search(description):
        return {
            'has_tech': True,
            'vacancy_info': {
                'name': vacancy_name,
                'url': vacancy_url,
                'id': vacancy_id
            }
        }
    
    return {'has_tech': False, 'vacancy_info': None}

def safe_lower(text):
    """
    Безопасное приведение к нижнему регистру
    """
    if text is None:
        return ""
    return text.lower()

def print_statistics(stats: Dict, vacancy_title: str):
    """
    Выводит статистику в читаемом формате
    """
    technology = stats['technology']
    real_requests, cached_requests = get_request_count()
    cache_stats = get_cache_stats()
    total_requests = real_requests + cached_requests
    
    print("\n" + "="*70)
    print(f"СТАТИСТИКА ПО ВАКАНСИЯМ: {vacancy_title.upper()}")
    print(f"Анализ технологии: {technology.upper()}")
    print("="*70)
    print(f"Всего вакансий найдено: {stats['total_vacancies']}")
    print(f"Вакансий с {technology}: {stats['tech_vacancies']}")
    print(f"Процент вакансий с {technology}: {stats['tech_percentage']:.2f}%")
    print(f"\nСТАТИСТИКА ЗАПРОСОВ:")
    print(f"  Реальных запросов к API: {real_requests}")
    print(f"  Кэшированных запросов: {cached_requests}")
    print(f"  Всего обращений: {total_requests}")
    print(f"  Попаданий в кэш: {cache_stats['cache_hit_rate']:.1f}%")
    print(f"  Размер кэша: {cache_stats['cache_size']} вакансий")
    print("\n" + "-"*70)

    if stats['tech_vacancies_details']:
        print(f"Первые 10 вакансий с {technology}:")
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
    results_dir = ensure_results_dir()
    
    if filename is None:
        technology = stats['technology']
        safe_vacancy_title = "".join(c for c in vacancy_title if c.isalnum() or c in (' ', '-', '_')).rstrip()
        safe_vacancy_title = safe_vacancy_title.replace(' ', '_')
        filename = f"{safe_vacancy_title}_{technology}_analysis_results.json"

    filepath = os.path.join(results_dir, filename)
    
    # Добавляем информацию о запросах в результаты
    real_requests, cached_requests = get_request_count()
    cache_stats = get_cache_stats()
    
    with open(filepath, 'w', encoding='utf-8') as f:
        results = stats.copy()
        results['vacancy_title'] = vacancy_title
        results['api_requests'] = {
            'real_requests': real_requests,
            'cached_requests': cached_requests,
            'total_requests': real_requests + cached_requests,
            'cache_stats': cache_stats
        }
        results['analysis_timestamp'] = time.time()
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    print(f"\nРезультаты сохранены в файл: {filepath}")
    
    return filepath

def main():
    """
    Основная функция скрипта
    """
    print("Анализ вакансий с HeadHunter (оптимизированная версия)")
    print("=" * 50)
    print(f"Лимит запросов: {MAX_REQUESTS_PER_SECOND} в секунду")
    print("=" * 50)

    vacancy_title = input("Введите название вакансии для поиска: ").strip()
    
    if not vacancy_title:
        print("Название вакансии не указано. Используется значение по умолчанию: Data Engineer")
        vacancy_title = "Data Engineer"

    technology = input("Введите технологию/инструмент для анализа: ").strip()

    if not technology:
        print("Технология не указана. Используется значение по умолчанию: python")
        technology = "python"

    search_query = f'"{vacancy_title}"'

    print(f"\nНачинаем сбор вакансий '{vacancy_title}' с поиском технологии: {technology}")

    # Получаем вакансии
    vacancies = get_vacancies(
        search_text=search_query,
        area=113,
        per_page=100
    )

    if not vacancies:
        print("Не удалось получить вакансии")
        return

    print(f"\nПолучено {len(vacancies)} вакансий")
    real_requests, cached_requests = get_request_count()
    print(f"Запросов к API на этом этапе: {real_requests} реальных, {cached_requests} кэшированных")

    # Анализируем наличие указанной технологии
    print(f"Анализируем вакансии на наличие {technology}...")
    stats = analyze_technology_in_vacancies_optimized(vacancies, technology)

    # Выводим результаты
    print_statistics(stats, vacancy_title)

    # Сохраняем в файл
    save_results_to_file(stats, vacancy_title)

if __name__ == "__main__":
    main()