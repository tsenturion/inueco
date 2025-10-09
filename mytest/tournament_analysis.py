import datetime
from typing import List, Dict, Any, Optional, Tuple


def parse_match_data(match_string: str) -> Dict[str, Any]:
    """
    Парсит строку с информацией о матче и возвращает структурированные данные.
    
    Args:
        match_string: строка формата "YYYY-MM-DD | Team1 (X:Y) Team2 | Stadium | Attendance"
    
    Returns:
        Словарь с данными матча
        
    Raises:
        ValueError: при невалидном формате входных данных
    """
    parts = match_string.split(' | ')
    if len(parts) != 4:
        raise ValueError("Invalid format: expected 4 parts separated by ' | '")
    
    date_str, teams_score_str, stadium_str, attendance_str = parts
    
    # Валидация даты
    try:
        year, month, day = map(int, date_str.split('-'))
        datetime.date(year, month, day)
    except (ValueError, TypeError):
        raise ValueError("Invalid date format: expected YYYY-MM-DD")
    
    # Валидация команд и счёта
    if '(' not in teams_score_str or ')' not in teams_score_str:
        raise ValueError("Invalid teams/score format: expected 'Team1 (X:Y) Team2'")
    
    # Извлекаем команды и счёт
    score_start = teams_score_str.find('(')
    score_end = teams_score_str.find(')')
    
    team1 = teams_score_str[:score_start].strip()
    score_part = teams_score_str[score_start + 1:score_end]
    team2 = teams_score_str[score_end + 1:].strip()
    
    if not team1 or not team2:
        raise ValueError("Team names and stadium cannot be empty")
    
    # Валидация счёта
    try:
        score_parts = score_part.split(':')
        if len(score_parts) != 2:
            raise ValueError("Invalid score format")
        
        score1 = int(score_parts[0])
        score2 = int(score_parts[1])
        
        if score1 < 0 or score2 < 0:
            raise ValueError("Score must be non-negative")
    except (ValueError, TypeError):
        raise ValueError("Invalid score: must be non-negative integers")
    
    # Валидация стадиона
    stadium = stadium_str.strip()
    if not stadium:
        raise ValueError("Team names and stadium cannot be empty")
    
    # Валидация посещаемости
    try:
        attendance = int(attendance_str)
        if attendance <= 0:
            raise ValueError("Attendance must be positive")
    except (ValueError, TypeError):
        raise ValueError("Invalid attendance: must be a positive integer")
    
    return {
        "date": date_str,
        "team1": team1,
        "score1": score1,
        "team2": team2,
        "score2": score2,
        "stadium": stadium,
        "attendance": attendance
    }


def filter_matches_by_criteria(matches_list: List[Dict[str, Any]], **criteria) -> List[Dict[str, Any]]:
    """
    Фильтрует список матчей по произвольным критериям.
    
    Args:
        matches_list: список словарей матчей
        **criteria: критерии фильтрации (team, date_from, date_to, min_attendance, 
                   max_attendance, min_total_goals, stadium)
    
    Returns:
        Отфильтрованный список матчей
    """
    if not matches_list:
        return []
    
    filtered_matches = []
    
    for match in matches_list:
        valid = True
        
        # Проверяем все критерии
        if 'team' in criteria:
            team = criteria['team']
            if match['team1'] != team and match['team2'] != team:
                valid = False
        
        if 'date_from' in criteria and valid:
            if match['date'] < criteria['date_from']:
                valid = False
        
        if 'date_to' in criteria and valid:
            if match['date'] > criteria['date_to']:
                valid = False
        
        if 'min_attendance' in criteria and valid:
            if match['attendance'] < criteria['min_attendance']:
                valid = False
        
        if 'max_attendance' in criteria and valid:
            if match['attendance'] > criteria['max_attendance']:
                valid = False
        
        if 'min_total_goals' in criteria and valid:
            total_goals = match['score1'] + match['score2']
            if total_goals < criteria['min_total_goals']:
                valid = False
        
        if 'stadium' in criteria and valid:
            if match['stadium'] != criteria['stadium']:
                valid = False
        
        if valid:
            filtered_matches.append(match)
    
    return filtered_matches


def calculate_advanced_team_stats(matches_list: List[Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:
    """
    Вычисляет расширенную статистику для каждой команды.
    
    Args:
        matches_list: список словарей матчей
        
    Returns:
        Словарь со статистикой для каждой команды
    """
    if not matches_list:
        return {}
    
    # Сортируем матчи по дате для вычисления серий
    sorted_matches = sorted(matches_list, key=lambda x: x['date'])
    
    team_data = {}
    team_matches = {}  # Для хранения матчей по командам для вычисления серий
    
    # Инициализация данных команд
    for match in sorted_matches:
        for team in [match['team1'], match['team2']]:
            if team not in team_data:
                team_data[team] = {
                    'points': 0,
                    'matches_played': 0,
                    'wins': 0,
                    'draws': 0,
                    'losses': 0,
                    'goals_for': 0,
                    'goals_against': 0,
                    'goal_diff': 0,
                    'home_points': 0,
                    'away_points': 0,
                    'win_streak': 0,
                    'total_attendance': 0
                }
            if team not in team_matches:
                team_matches[team] = []
    
    # Заполняем матчи для каждой команды
    for match in sorted_matches:
        team1, team2 = match['team1'], match['team2']
        score1, score2 = match['score1'], match['score2']
        attendance = match['attendance']
        
        team_matches[team1].append((match['date'], 'home', score1, score2, attendance))
        team_matches[team2].append((match['date'], 'away', score2, score1, attendance))
    
    # Вычисляем статистику для каждой команды
    for team, matches in team_matches.items():
        # Сортируем матчи команды по дате
        matches.sort(key=lambda x: x[0])
        
        # Основная статистика
        for date, venue, goals_for, goals_against, attendance in matches:
            team_data[team]['matches_played'] += 1
            team_data[team]['goals_for'] += goals_for
            team_data[team]['goals_against'] += goals_against
            team_data[team]['total_attendance'] += attendance
            
            if goals_for > goals_against:  # Победа
                team_data[team]['wins'] += 1
                team_data[team]['points'] += 3
                if venue == 'home':
                    team_data[team]['home_points'] += 3
                else:
                    team_data[team]['away_points'] += 3
            elif goals_for == goals_against:  # Ничья
                team_data[team]['draws'] += 1
                team_data[team]['points'] += 1
                if venue == 'home':
                    team_data[team]['home_points'] += 1
                else:
                    team_data[team]['away_points'] += 1
            else:  # Поражение
                team_data[team]['losses'] += 1
        
        # Разница мячей
        team_data[team]['goal_diff'] = team_data[team]['goals_for'] - team_data[team]['goals_against']
        
        # Серия побед
        current_streak = 0
        for date, venue, goals_for, goals_against, attendance in reversed(matches):
            if goals_for > goals_against:
                current_streak += 1
            else:
                break
        team_data[team]['win_streak'] = current_streak
        
        # Средняя посещаемость
        if team_data[team]['matches_played'] > 0:
            avg_attendance = team_data[team]['total_attendance'] / team_data[team]['matches_played']
            team_data[team]['avg_attendance'] = round(avg_attendance, 2)
        else:
            team_data[team]['avg_attendance'] = 0.0
        
        # Удаляем временное поле
        del team_data[team]['total_attendance']
    
    return team_data


def rank_teams_advanced(team_stats: Dict[str, Dict[str, Any]], 
                       tiebreaker_order: List[str] = ['points', 'goal_diff', 'goals_for']) -> List[Tuple[int, str, int, int]]:
    """
    Ранжирует команды с учётом каскадной сортировки при равенстве очков.
    
    Args:
        team_stats: словарь статистики команд
        tiebreaker_order: порядок критериев для разрешения равенства
        
    Returns:
        Список кортежей (ранг, название команды, очки, разница мячей)
    """
    if not team_stats:
        return []
    
    # Преобразуем в список для сортировки
    teams_list = []
    for team, stats in team_stats.items():
        teams_list.append({
            'name': team,
            'points': stats['points'],
            'goal_diff': stats['goal_diff'],
            'goals_for': stats['goals_for'],
            'wins': stats['wins']
        })
    
    # Сортируем команды
    def sort_key(team):
        key = []
        for criterion in tiebreaker_order:
            if criterion == 'points':
                key.append(-team['points'])  # Отрицательное для сортировки по убыванию
            elif criterion == 'goal_diff':
                key.append(-team['goal_diff'])
            elif criterion == 'goals_for':
                key.append(-team['goals_for'])
            elif criterion == 'wins':
                key.append(-team['wins'])
        return tuple(key)
    
    teams_list.sort(key=sort_key)
    
    # Присваиваем ранги с учётом равенства
    result = []
    current_rank = 1
    prev_team = None
    
    for i, team in enumerate(teams_list):
        if i == 0:
            # Первая команда всегда ранг 1
            result.append((current_rank, team['name'], team['points'], team['goal_diff']))
            prev_team = team
        else:
            # Проверяем равенство с предыдущей командой
            is_equal = True
            for criterion in tiebreaker_order:
                if criterion == 'points' and team['points'] != prev_team['points']:
                    is_equal = False
                    break
                elif criterion == 'goal_diff' and team['goal_diff'] != prev_team['goal_diff']:
                    is_equal = False
                    break
                elif criterion == 'goals_for' and team['goals_for'] != prev_team['goals_for']:
                    is_equal = False
                    break
                elif criterion == 'wins' and team['wins'] != prev_team['wins']:
                    is_equal = False
                    break
            
            if is_equal:
                # Тот же ранг, что и у предыдущей команды
                result.append((current_rank, team['name'], team['points'], team['goal_diff']))
            else:
                # Новый ранг
                current_rank = i + 1
                result.append((current_rank, team['name'], team['points'], team['goal_diff']))
            
            prev_team = team
    
    return result


def generate_analytics_report(matches_list: List[Dict[str, Any]], 
                            team_stats: Dict[str, Dict[str, Any]], 
                            tournament_table: List[Tuple[int, str, int, int]]) -> Dict[str, Any]:
    """
    Генерирует итоговый аналитический отчёт.
    
    Args:
        matches_list: список всех матчей
        team_stats: статистика команд
        tournament_table: турнирная таблица
        
    Returns:
        Словарь с аналитикой
    """
    if not matches_list or not team_stats or not tournament_table:
        return {
            "tournament_leader": "",
            "most_goals_match": {},
            "highest_attendance_match": {},
            "most_efficient_team": "",
            "biggest_upset": None,
            "goal_distribution": {},
            "attendance_by_team": {}
        }
    
    # Создаем словарь для быстрого поиска ранга команды
    rank_dict = {}
    for rank, team, points, goal_diff in tournament_table:
        rank_dict[team] = rank
    
    # 1. Лидер турнира
    tournament_leader = tournament_table[0][1] if tournament_table else ""
    
    # 2. Матч с наибольшим количеством голов
    most_goals_match = max(matches_list, key=lambda m: m['score1'] + m['score2']) if matches_list else {}
    
    # 3. Матч с наибольшей посещаемостью
    highest_attendance_match = max(matches_list, key=lambda m: m['attendance']) if matches_list else {}
    
    # 4. Самая эффективная команда (points/matches_played)
    most_efficient_team = ""
    max_efficiency = -1.0
    
    for team, stats in team_stats.items():
        if stats['matches_played'] > 0:
            efficiency = round(stats['points'] / stats['matches_played'], 2)
            if efficiency > max_efficiency:
                max_efficiency = efficiency
                most_efficient_team = team
    
    # 5. Самый большой апсет
    biggest_upset = None
    max_rank_diff = -1
    
    for match in matches_list:
        team1, team2 = match['team1'], match['team2']
        score1, score2 = match['score1'], match['score2']
        
        # Пропускаем ничьи и матчи, где команды нет в таблице
        if score1 == score2 or team1 not in rank_dict or team2 not in rank_dict:
            continue
        
        if score1 > score2:  # Победила team1
            winner, loser = team1, team2
            winner_rank, loser_rank = rank_dict[team1], rank_dict[team2]
        else:  # Победила team2
            winner, loser = team2, team1
            winner_rank, loser_rank = rank_dict[team2], rank_dict[team1]
        
        # Upset: команда с худшим рангом победила команду с лучшим рангом
        if winner_rank > loser_rank:
            rank_diff = winner_rank - loser_rank
            if rank_diff > max_rank_diff:
                max_rank_diff = rank_diff
                biggest_upset = {
                    "match": match,
                    "winner_rank": winner_rank,
                    "loser_rank": loser_rank
                }
    
    # 6. Распределение голов
    goal_distribution = {}
    for match in matches_list:
        total_goals = match['score1'] + match['score2']
        goal_distribution[total_goals] = goal_distribution.get(total_goals, 0) + 1
    
    # 7. Посещаемость по командам
    attendance_by_team = {}
    for team, stats in team_stats.items():
        attendance_by_team[team] = stats.get('avg_attendance', 0.0)
    
    return {
        "tournament_leader": tournament_leader,
        "most_goals_match": most_goals_match,
        "highest_attendance_match": highest_attendance_match,
        "most_efficient_team": most_efficient_team,
        "biggest_upset": biggest_upset,
        "goal_distribution": goal_distribution,
        "attendance_by_team": attendance_by_team
    }
