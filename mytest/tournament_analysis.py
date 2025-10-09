import datetime
import re
from typing import List, Dict, Any, Tuple


def parse_match_data(match_string: str) -> Dict[str, Any]:
    parts = match_string.split(" | ")
    if len(parts) != 4:
        raise ValueError("Invalid format: expected 4 parts separated by ' | '")
    
    date_str, teams_score_str, stadium_str, attendance_str = parts
    
    try:
        year, month, day = map(int, date_str.split("-"))
        datetime.date(year, month, day)
    except (ValueError, TypeError):
        raise ValueError("Invalid date format: expected YYYY-MM-DD")

    teams_score_pattern = r'^\s*(.+?)\s*\(\s*(\S+)\s*:\s*(\S+)\s*\)\s*(.+?)\s*$'
    match = re.match(teams_score_pattern, teams_score_str)
    if not match:
        raise ValueError("Invalid teams/score format: expected 'Team1 (X:Y) Team2'")
    
    team1, score1_str, score2_str, team2 = match.groups()
    
    if not team1.strip() or not team2.strip() or not stadium_str.strip():
        raise ValueError("Team names and stadium cannot be empty")
    
    try:
        score1 = int(score1_str)
        score2 = int(score2_str)
        if score1 < 0 or score2 < 0:
            raise ValueError("Score cannot be negative")
    except ValueError:
        raise ValueError("Invalid score: must be non-negative integers")
    
    try:
        attendance = int(attendance_str)
        if attendance <= 0:
            raise ValueError("Attendance must be positive")
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


def filter_matches_by_criteria(matches_list: List[Dict[str, Any]], **criteria) -> List[Dict[str, Any]]:
    if not matches_list:
        return []
    
    filtered_matches = []
    
    for match in matches_list:
        valid = True
        
        for key, value in criteria.items():
            if key == "team":
                if value not in [match["team1"], match["team2"]]:
                    valid = False
                    break
                    
            elif key == "date_from":
                if match["date"] < value:
                    valid = False
                    break
                    
            elif key == "date_to":
                if match["date"] > value:
                    valid = False
                    break
                    
            elif key == "min_attendance":
                if match["attendance"] < value:
                    valid = False
                    break
                    
            elif key == "max_attendance":
                if match["attendance"] > value:
                    valid = False
                    break
                    
            elif key == "min_total_goals":
                total_goals = match["score1"] + match["score2"]
                if total_goals < value:
                    valid = False
                    break
                    
            elif key == "stadium":
                if match["stadium"] != value:
                    valid = False
                    break
        
        if valid:
            filtered_matches.append(match)
    
    return filtered_matches


def calculate_advanced_team_stats(matches_list: List[Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:
    if not matches_list:
        return {}
    
    team_stats = {}
    team_matches = {}
    
    for match in matches_list:
        date = match["date"]
        team1 = match["team1"]
        team2 = match["team2"]
        
        if team1 not in team_matches:
            team_matches[team1] = []
        if team2 not in team_matches:
            team_matches[team2] = []
            
        team_matches[team1].append((date, match, "home"))
        team_matches[team2].append((date, match, "away"))
    
    for team in team_matches:
        team_matches[team].sort(key=lambda x: x[0])
    
    for team, matches in team_matches.items():
        points = 0
        matches_played = 0
        wins = 0
        draws = 0
        losses = 0
        goals_for = 0
        goals_against = 0
        home_points = 0
        away_points = 0
        total_attendance = 0
        
        for date, match, venue in matches:
            matches_played += 1
            total_attendance += match["attendance"]
            
            if venue == "home":
                team_score = match["score1"]
                opponent_score = match["score2"]
            else:
                team_score = match["score2"]
                opponent_score = match["score1"]
            
            goals_for += team_score
            goals_against += opponent_score
            
            if team_score > opponent_score:
                wins += 1
                match_points = 3
                if venue == "home":
                    home_points += 3
                else:
                    away_points += 3
            elif team_score == opponent_score:
                draws += 1
                match_points = 1
                if venue == "home":
                    home_points += 1
                else:
                    away_points += 1
            else:
                losses += 1
                match_points = 0
            
            points += match_points
        
        win_streak = 0
        current_streak = 0
        
        for date, match, venue in reversed(matches):
            if venue == "home":
                team_score = match["score1"]
                opponent_score = match["score2"]
            else:
                team_score = match["score2"]
                opponent_score = match["score1"]
            
            if team_score > opponent_score:
                current_streak += 1
            else:
                break
        
        win_streak = current_streak
        
        team_stats[team] = {
            "points": points,
            "matches_played": matches_played,
            "wins": wins,
            "draws": draws,
            "losses": losses,
            "goals_for": goals_for,
            "goals_against": goals_against,
            "goal_diff": goals_for - goals_against,
            "home_points": home_points,
            "away_points": away_points,
            "win_streak": win_streak,
            "avg_attendance": round(total_attendance / matches_played, 2) if matches_played > 0 else 0.0
        }
    
    return team_stats


def rank_teams_advanced(team_stats: Dict[str, Dict[str, Any]], 
                       tiebreaker_order: List[str] = None) -> List[Tuple[int, str, int, int]]:
    if not team_stats:
        return []
    
    if tiebreaker_order is None:
        tiebreaker_order = ['points', 'goal_diff', 'goals_for']
    
    teams_list = []
    for team, stats in team_stats.items():
        teams_list.append({
            'name': team,
            'points': stats['points'],
            'goal_diff': stats['goal_diff'],
            'goals_for': stats['goals_for'],
            'wins': stats['wins']
        })
    
    def sort_key(team):
        key = []
        for criterion in tiebreaker_order:
            if criterion == "points":
                key.append(-team['points'])
            elif criterion == "goal_diff":
                key.append(-team['goal_diff'])
            elif criterion == "goals_for":
                key.append(-team['goals_for'])
            elif criterion == "wins":
                key.append(-team['wins'])
        return tuple(key)
    
    teams_list.sort(key=sort_key)
    
    result = []
    current_rank = 1
    prev_team = None
    
    for i, team in enumerate(teams_list):
        if i == 0:
            result.append((current_rank, team['name'], team['points'], team['goal_diff']))
            prev_team = team
        else:
            is_equal = True
            for criterion in tiebreaker_order:
                if team[criterion] != prev_team[criterion]:
                    is_equal = False
                    break
            
            if is_equal:
                result.append((current_rank, team['name'], team['points'], team['goal_diff']))
            else:
                current_rank = i + 1
                result.append((current_rank, team['name'], team['points'], team['goal_diff']))
            
            prev_team = team
    
    return result


def generate_analytics_report(matches_list: List[Dict[str, Any]], 
                            team_stats: Dict[str, Dict[str, Any]], 
                            tournament_table: List[Tuple[int, str, int, int]]) -> Dict[str, Any]:
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
    
    rank_dict = {}
    for rank, team, points, goal_diff in tournament_table:
        rank_dict[team] = rank
    
    tournament_leader = tournament_table[0][1] if tournament_table else ""
    
    most_goals_match = None
    max_goals = -1
    for match in matches_list:
        total_goals = match["score1"] + match["score2"]
        if total_goals > max_goals:
            max_goals = total_goals
            most_goals_match = match
    
    highest_attendance_match = None
    max_attendance = -1
    for match in matches_list:
        if match["attendance"] > max_attendance:
            max_attendance = match["attendance"]
            highest_attendance_match = match
    
    most_efficient_team = ""
    max_efficiency = -1.0
    for team, stats in team_stats.items():
        if stats["matches_played"] > 0:
            efficiency = round(stats["points"] / stats["matches_played"], 2)
            if efficiency > max_efficiency:
                max_efficiency = efficiency
                most_efficient_team = team
    
    biggest_upset = None
    max_rank_diff = -1
    
    for match in matches_list:
        team1 = match["team1"]
        team2 = match["team2"]
        score1 = match["score1"]
        score2 = match["score2"]
        
        if score1 == score2 or team1 not in rank_dict or team2 not in rank_dict:
            continue
        
        if score1 > score2:
            winner = team1
            loser = team2
        else:
            winner = team2
            loser = team1
        
        winner_rank = rank_dict[winner]
        loser_rank = rank_dict[loser]
        
        if winner_rank > loser_rank:
            rank_diff = winner_rank - loser_rank
            if rank_diff > max_rank_diff:
                max_rank_diff = rank_diff
                biggest_upset = {
                    "match": match,
                    "winner_rank": winner_rank,
                    "loser_rank": loser_rank
                }
    
    goal_distribution = {}
    for match in matches_list:
        total_goals = match["score1"] + match["score2"]
        goal_distribution[total_goals] = goal_distribution.get(total_goals, 0) + 1
    
    attendance_by_team = {}
    for team, stats in team_stats.items():
        attendance_by_team[team] = stats["avg_attendance"]
    
    return {
        "tournament_leader": tournament_leader,
        "most_goals_match": most_goals_match or {},
        "highest_attendance_match": highest_attendance_match or {},
        "most_efficient_team": most_efficient_team,
        "biggest_upset": biggest_upset,
        "goal_distribution": goal_distribution,
        "attendance_by_team": attendance_by_team
    }