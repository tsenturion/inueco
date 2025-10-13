import datetime
import math
from typing import List, Dict, Any, Optional, Tuple

def parse_match_data(match_string: str) -> dict:
    """
    Парсит строку с информацией о матче и возвращает структурированные данные.
    
    Args:
        match_string: строка формата "YYYY-MM-DD | Team1 (X:Y) Team2 | Stadium | Attendance"
    
    Returns:
        Словарь с данными матча
        
    Raises:
        ValueError: при невалидном формате входных данных
    """
    # Проверка количества частей
    parts = match_string.split(' | ')
    if len(parts) != 4:
        raise ValueError("Invalid format: expected 4 parts separated by ' | '")
    
    date_str, teams_score_str, stadium_str, attendance_str = parts
    
    # Валидация даты
    try:
        datetime.datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Invalid date format: expected YYYY-MM-DD")
    
    # Валидация формата команд и счёта - используем более гибкое регулярное выражение
    import re
    pattern = r'^(.*?) \((.+):(.+)\) (.*)$'
    match = re.match(pattern, teams_score_str)
    if not match:
        raise ValueError("Invalid teams/score format: expected 'Team1 (X:Y) Team2'")
    
    team1, score1_str, score2_str, team2 = match.groups()
    
    # Проверка пустых названий
    if not team1.strip() or not team2.strip() or not stadium_str.strip():
        raise ValueError("Team names and stadium cannot be empty")
    
    # Валидация счёта - теперь проверяем отдельно
    try:
        score1 = int(score1_str)
        score2 = int(score2_str)
        if score1 < 0 or score2 < 0:
            raise ValueError("Invalid score: must be non-negative integers")
    except ValueError:
        raise ValueError("Invalid score: must be non-negative integers")
    
    # Валидация посещаемости
    try:
        attendance = int(attendance_str)
        if attendance <= 0:
            raise ValueError("Invalid attendance: must be a positive integer")
    except ValueError:
        raise ValueError("Invalid attendance: must be a positive integer")
    
    return {
        "date": date_str,
        "team1": team1.strip(),
        "score1": score1,
        "team2": team2.strip(),
        "score2": score2,
        "stadium": stadium_str.strip(),
        "attendance": attendance
    }


def filter_matches_by_criteria(matches_list: List[dict], **criteria) -> List[dict]:
    """
    Фильтрует список матчей по произвольным критериям.
    
    Args:
        matches_list: список словарей матчей
        **criteria: критерии фильтрации
        
    Returns:
        Отфильтрованный список матчей
    """
    if not matches_list:
        return []
    
    filtered_matches = matches_list.copy()
    
    for key, value in criteria.items():
        if key == 'team':
            filtered_matches = [m for m in filtered_matches 
                              if value in [m['team1'], m['team2']]]
        elif key == 'date_from':
            filtered_matches = [m for m in filtered_matches 
                              if m['date'] >= value]
        elif key == 'date_to':
            filtered_matches = [m for m in filtered_matches 
                              if m['date'] <= value]
        elif key == 'min_attendance':
            filtered_matches = [m for m in filtered_matches 
                              if m['attendance'] >= value]
        elif key == 'max_attendance':
            filtered_matches = [m for m in filtered_matches 
                              if m['attendance'] <= value]
        elif key == 'min_total_goals':
            filtered_matches = [m for m in filtered_matches 
                              if (m['score1'] + m['score2']) >= value]
        elif key == 'stadium':
            filtered_matches = [m for m in filtered_matches 
                              if m['stadium'] == value]
    
    return filtered_matches


def calculate_advanced_team_stats(matches_list: List[dict]) -> Dict[str, Dict[str, Any]]:
    """
    Вычисляет расширенную статистику для каждой команды.
    
    Args:
        matches_list: список словарей матчей
        
    Returns:
        Словарь со статистикой для каждой команды
    """
    if not matches_list:
        return {}
    
    # Сортируем матчи по дате для корректного расчета серий
    sorted_matches = sorted(matches_list, key=lambda x: x['date'])
    
    team_stats = {}
    team_match_history = {}
    
    # Инициализация структур данных
    for match in sorted_matches:
        for team in [match['team1'], match['team2']]:
            if team not in team_stats:
                team_stats[team] = {
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
                    'avg_attendance': 0.0
                }
                team_match_history[team] = []
    
    # Собираем все матчи для каждой команды в хронологическом порядке
    for match in sorted_matches:
        team1, team2 = match['team1'], match['team2']
        team_match_history[team1].append((match, 'home'))
        team_match_history[team2].append((match, 'away'))
    
    # Расчет статистики для каждой команды
    for team in team_stats:
        matches_history = team_match_history[team]
        total_attendance = 0
        current_streak = 0
        max_streak = 0
        
        for i, (match, venue) in enumerate(matches_history):
            is_home = venue == 'home'
            score_team = match['score1'] if is_home else match['score2']
            score_opponent = match['score2'] if is_home else match['score1']
            
            # Обновляем базовую статистику
            team_stats[team]['matches_played'] += 1
            team_stats[team]['goals_for'] += score_team
            team_stats[team]['goals_against'] += score_opponent
            total_attendance += match['attendance']
            
            # Определяем результат матча
            if score_team > score_opponent:
                team_stats[team]['wins'] += 1
                team_stats[team]['points'] += 3
                current_streak += 1
                max_streak = max(max_streak, current_streak)
                
                if is_home:
                    team_stats[team]['home_points'] += 3
                else:
                    team_stats[team]['away_points'] += 3
                    
            elif score_team == score_opponent:
                team_stats[team]['draws'] += 1
                team_stats[team]['points'] += 1
                current_streak = 0
                
                if is_home:
                    team_stats[team]['home_points'] += 1
                else:
                    team_stats[team]['away_points'] += 1
            else:
                team_stats[team]['losses'] += 1
                current_streak = 0
        
        # Устанавливаем текущую серию побед (только если последний матч - победа)
        if matches_history:
            last_match, last_venue = matches_history[-1]
            is_home_last = last_venue == 'home'
            score_team_last = last_match['score1'] if is_home_last else last_match['score2']
            score_opponent_last = last_match['score2'] if is_home_last else last_match['score1']
            
            if score_team_last > score_opponent_last:
                team_stats[team]['win_streak'] = current_streak
            else:
                team_stats[team]['win_streak'] = 0
        
        # Расчет средней посещаемости и разницы голов
        if team_stats[team]['matches_played'] > 0:
            team_stats[team]['avg_attendance'] = round(
                total_attendance / team_stats[team]['matches_played'], 2
            )
        team_stats[team]['goal_diff'] = (
            team_stats[team]['goals_for'] - team_stats[team]['goals_against']
        )
    
    return team_stats


def rank_teams_advanced(team_stats: Dict[str, Dict[str, Any]], 
                       tiebreaker_order: List[str] = None) -> List[Tuple[int, str, int, int]]:
    """
    Ранжирует команды с учётом каскадной сортировки при равенстве очков.
    
    Args:
        team_stats: словарь статистики команд
        tiebreaker_order: порядок критериев для разрешения равенства
        
    Returns:
        Список кортежей (ранг, название команды, очки, разница голов)
    """
    if tiebreaker_order is None:
        tiebreaker_order = ['points', 'goal_diff', 'goals_for']
    
    if not team_stats:
        return []
    
    # Подготовка списка команд для сортировки
    teams_list = []
    for team, stats in team_stats.items():
        teams_list.append({
            'name': team,
            'points': stats['points'],
            'goal_diff': stats['goal_diff'],
            'goals_for': stats['goals_for'],
            'wins': stats['wins']
        })
    
    # Сортировка по указанным критериям
    def sort_key(team):
        key_values = []
        for criterion in tiebreaker_order:
            if criterion == 'points':
                key_values.append(-team['points'])
            elif criterion == 'goal_diff':
                key_values.append(-team['goal_diff'])
            elif criterion == 'goals_for':
                key_values.append(-team['goals_for'])
            elif criterion == 'wins':
                key_values.append(-team['wins'])
        return tuple(key_values)
    
    sorted_teams = sorted(teams_list, key=sort_key)
    
    # Присвоение рангов с учетом равенства
    result = []
    current_rank = 1
    
    for i, team in enumerate(sorted_teams):
        if i == 0:
            result.append((current_rank, team['name'], team['points'], team['goal_diff']))
        else:
            prev_team = sorted_teams[i-1]
            # Проверяем равенство с предыдущей командой по всем критериям сортировки
            is_tie = all(
                prev_team.get(criterion) == team.get(criterion) 
                for criterion in tiebreaker_order
            )
            
            if is_tie:
                result.append((current_rank, team['name'], team['points'], team['goal_diff']))
            else:
                current_rank = i + 1
                result.append((current_rank, team['name'], team['points'], team['goal_diff']))
    
    return result


def generate_analytics_report(matches_list: List[dict], 
                            team_stats: Dict[str, Dict[str, Any]], 
                            tournament_table: List[Tuple[int, str, int, int]]) -> Dict[str, Any]:
    """
    Генерирует итоговый аналитический отчёт на основе всех собранных данных.
    
    Args:
        matches_list: список всех матчей
        team_stats: статистика команд
        tournament_table: турнирная таблица
        
    Returns:
        Словарь с аналитикой турнира
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
    
    # Создаем словарь для быстрого доступа к рангам команд
    rank_dict = {}
    for rank, team, points, goal_diff in tournament_table:
        rank_dict[team] = rank
    
    # 1. Лидер турнира
    tournament_leader = tournament_table[0][1] if tournament_table else ""
    
    # 2. Матч с наибольшим количеством голов
    most_goals_match = max(matches_list, 
                          key=lambda m: m['score1'] + m['score2'], 
                          default={})
    
    # 3. Матч с наибольшей посещаемостью
    highest_attendance_match = max(matches_list, 
                                  key=lambda m: m['attendance'], 
                                  default={})
    
    # 4. Самая эффективная команда (points/matches_played)
    most_efficient_team = ""
    max_efficiency = -1.0
    
    for team, stats in team_stats.items():
        if stats['matches_played'] > 0:
            efficiency = round(stats['points'] / stats['matches_played'], 2)
            if efficiency > max_efficiency or (efficiency == max_efficiency and not most_efficient_team):
                max_efficiency = efficiency
                most_efficient_team = team
    
    # 5. Самый неожиданный результат (upset)
    biggest_upset = None
    max_rank_diff = -1
    
    for match in matches_list:
        team1, team2 = match['team1'], match['team2']
        score1, score2 = match['score1'], match['score2']
        
        # Пропускаем ничьи и матчи, где команды отсутствуют в таблице
        if (score1 == score2 or team1 not in rank_dict or team2 not in rank_dict):
            continue
        
        if score1 > score2:  # Победа team1
            winner, loser = team1, team2
        else:  # Победа team2
            winner, loser = team2, team1
        
        winner_rank, loser_rank = rank_dict[winner], rank_dict[loser]
        
        # Upset: команда с худшим рангом (большим числом) победила команду с лучшим рангом (меньшим числом)
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
    
    # 7. Средняя посещаемость по командам
    attendance_by_team = {}
    for team, stats in team_stats.items():
        attendance_by_team[team] = stats['avg_attendance']
    
    return {
        "tournament_leader": tournament_leader,
        "most_goals_match": most_goals_match,
        "highest_attendance_match": highest_attendance_match,
        "most_efficient_team": most_efficient_team,
        "biggest_upset": biggest_upset,
        "goal_distribution": goal_distribution,
        "attendance_by_team": attendance_by_team
    }