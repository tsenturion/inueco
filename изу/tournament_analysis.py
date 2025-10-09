# tournament_analysis.py

from datetime import datetime
from collections import defaultdict, Counter
import re

# Функция 1
def parse_match_data(match_string):
    parts = match_string.split(" | ")
    if len(parts) != 4:
        raise ValueError("Invalid format: expected 4 parts separated by ' | '")

    date_str, teams_score_str, stadium, attendance_str = parts

    # Проверка даты
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        if not (1 <= date_obj.month <= 12):
            raise ValueError
    except ValueError:
        raise ValueError("Invalid date format: expected YYYY-MM-DD")

    # Проверка наличия скобок с счётом
    score_match = re.search(r"\((.*):(.*)\)", teams_score_str)
    if not score_match:
        raise ValueError("Invalid teams/score format: expected 'Team1 (X:Y) Team2'")

    score1_str, score2_str = score_match.groups()
    # Разделяем команды по скобкам
    team_parts = teams_score_str.split("(")
    team1 = team_parts[0].strip() if len(team_parts) > 0 else ""
    team2_part = team_parts[1].split(")")[-1].strip() if len(team_parts) > 1 else ""
    team2 = team2_part

    if not team1 or not team2 or not stadium.strip():
        raise ValueError("Team names and stadium cannot be empty")

    # Проверка счёта
    try:
        score1 = int(score1_str)
        score2 = int(score2_str)
        if score1 < 0 or score2 < 0:
            raise ValueError
    except ValueError:
        raise ValueError("Invalid score: must be non-negative integers")

    # Проверка посещаемости
    try:
        attendance = int(attendance_str)
        if attendance <= 0:
            raise ValueError
    except ValueError:
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



# Функция 2
def filter_matches_by_criteria(matches_list, **criteria):
    filtered = []

    for match in matches_list:
        include = True
        if "team" in criteria:
            if criteria["team"] != match["team1"] and criteria["team"] != match["team2"]:
                include = False
        if "date_from" in criteria:
            if match["date"] < criteria["date_from"]:
                include = False
        if "date_to" in criteria:
            if match["date"] > criteria["date_to"]:
                include = False
        if "min_attendance" in criteria:
            if match["attendance"] < criteria["min_attendance"]:
                include = False
        if "max_attendance" in criteria:
            if match["attendance"] > criteria["max_attendance"]:
                include = False
        if "min_total_goals" in criteria:
            total_goals = match["score1"] + match["score2"]
            if total_goals < criteria["min_total_goals"]:
                include = False
        if "stadium" in criteria:
            if match["stadium"] != criteria["stadium"]:
                include = False

        if include:
            filtered.append(match)

    return filtered


# Функция 3
def calculate_advanced_team_stats(matches_list):
    team_stats = {}
    matches_by_team = defaultdict(list)

    # Сортировка по дате
    sorted_matches = sorted(matches_list, key=lambda x: x["date"])

    for match in sorted_matches:
        for is_home, team, goals_for, goals_against in [
            (True, match["team1"], match["score1"], match["score2"]),
            (False, match["team2"], match["score2"], match["score1"])
        ]:
            if team not in team_stats:
                team_stats[team] = {
                    "points": 0,
                    "matches_played": 0,
                    "wins": 0,
                    "draws": 0,
                    "losses": 0,
                    "goals_for": 0,
                    "goals_against": 0,
                    "goal_diff": 0,
                    "home_points": 0,
                    "away_points": 0,
                    "win_streak": 0,
                    "avg_attendance": 0.0
                }
            stats = team_stats[team]
            stats["matches_played"] += 1
            stats["goals_for"] += goals_for
            stats["goals_against"] += goals_against
            stats["goal_diff"] = stats["goals_for"] - stats["goals_against"]
            stats["avg_attendance"] += match["attendance"]

            # Очки
            if goals_for > goals_against:
                stats["points"] += 3
                stats["wins"] += 1
                if is_home:
                    stats["home_points"] += 3
                else:
                    stats["away_points"] += 3
            elif goals_for == goals_against:
                stats["points"] += 1
                stats["draws"] += 1
                if is_home:
                    stats["home_points"] += 1
                else:
                    stats["away_points"] += 1
            else:
                stats["losses"] += 1

            matches_by_team[team].append(goals_for > goals_against)

    # Вычисление win_streak и avg_attendance
    for team, wins_seq in matches_by_team.items():
        streak = 0
        for won in reversed(wins_seq):
            if won:
                streak += 1
            else:
                break
        team_stats[team]["win_streak"] = streak
        avg_att = team_stats[team]["avg_attendance"] / team_stats[team]["matches_played"]
        team_stats[team]["avg_attendance"] = round(avg_att, 2)

    return team_stats


# Функция 4
def rank_teams_advanced(team_stats, tiebreaker_order=['points', 'goal_diff', 'goals_for']):
    def sort_key(item):
        team_name, stats = item
        return tuple(-stats[criterion] for criterion in tiebreaker_order)

    sorted_teams = sorted(team_stats.items(), key=sort_key)
    ranking = []
    last_values = None
    last_rank = 0
    skip_count = 0

    for idx, (team_name, stats) in enumerate(sorted_teams, start=1):
        current_values = tuple(stats[criterion] for criterion in tiebreaker_order)
        if current_values == last_values:
            rank = last_rank
            skip_count += 1
        else:
            rank = last_rank + 1 + skip_count
            skip_count = 0
        last_rank = rank
        last_values = current_values
        ranking.append((rank, team_name, stats.get("points", 0), stats.get("goal_diff", 0)))

    return ranking


# Функция 5
def generate_analytics_report(matches_list, team_stats, tournament_table):
    report = {}

    if tournament_table:
        report["tournament_leader"] = tournament_table[0][1]
    else:
        report["tournament_leader"] = None


    if matches_list:
        report["most_goals_match"] = max(matches_list, key=lambda m: m["score1"] + m["score2"])
        report["highest_attendance_match"] = max(matches_list, key=lambda m: m["attendance"])
    else:
        report["most_goals_match"] = None
        report["highest_attendance_match"] = None

   
    most_eff = None
    best_ratio = -1
    for team, stats in team_stats.items():
        if stats["matches_played"] == 0:
            continue
        ratio = round(stats["points"] / stats["matches_played"], 2)
        if ratio > best_ratio:
            best_ratio = ratio
            most_eff = team
    report["most_efficient_team"] = most_eff


    team_rank_map = {team: rank for rank, team, _, _ in tournament_table}
    biggest_diff = -1
    upset_match = None
    for match in matches_list:
        if match["score1"] == match["score2"]:
            continue
        winner = match["team1"] if match["score1"] > match["score2"] else match["team2"]
        loser = match["team2"] if match["score1"] > match["score2"] else match["team1"]
        if winner not in team_rank_map or loser not in team_rank_map:
            continue
        diff = team_rank_map[winner] - team_rank_map[loser]
        if diff > biggest_diff:
            biggest_diff = diff
            upset_match = {
                "match": match,
                "winner_rank": team_rank_map[winner],
                "loser_rank": team_rank_map[loser]
            }
    report["biggest_upset"] = upset_match if biggest_diff > 0 else None


    goal_counts = Counter(match["score1"] + match["score2"] for match in matches_list)
    report["goal_distribution"] = dict(goal_counts)

    attendance_map = {team: round(stats["avg_attendance"], 2) for team, stats in team_stats.items()}
    report["attendance_by_team"] = attendance_map
    return report