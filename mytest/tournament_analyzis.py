import datetime
from typing import List, Dict, Tuple, Optional, Any


def parse_match_data(match_string: str) -> Dict[str, Any]:
    parts = match_string.split(' | ')
    if len(parts) != 4:
        raise ValueError("Invalid format: expected 4 parts separated by ' | '")
    
    date_str, teams_score_str, stadium_str, attendance_str = parts
    
    try:
        year, month, day = map(int, date_str.split('-'))
        datetime.date(year, month, day)
    except (ValueError, TypeError):
        raise ValueError("Invalid date format: expected YYYY-MM-DD")
    
    stadium = stadium_str.strip()
    if not stadium:
        raise ValueError("Team names and stadium cannot be empty")
    
    try:
        attendance = int(attendance_str)
        if attendance <= 0:
            raise ValueError("Invalid attendance: must be a positive integer")
    except (ValueError, TypeError):
        raise ValueError("Invalid attendance: must be a positive integer")
    
    if '(' not in teams_score_str or ')' not in teams_score_str:
        raise ValueError("Invalid teams/score format: expected 'Team1 (X:Y) Team2'")
    
    open_bracket = teams_score_str.find('(')
    close_bracket = teams_score_str.find(')')
    
    if open_bracket == -1 or close_bracket == -1 or close_bracket < open_bracket:
        raise ValueError("Invalid teams/score format: expected 'Team1 (X:Y) Team2'")
    
    team1 = teams_score_str[:open_bracket].strip()
    score_part = teams_score_str[open_bracket+1:close_bracket].strip()
    team2 = teams_score_str[close_bracket+1:].strip()
    
    if not team1 or not team2:
        raise ValueError("Team names and stadium cannot be empty")
    
    if ':' not in score_part:
        raise ValueError("Invalid teams/score format: expected 'Team1 (X:Y) Team2'")
    
    score_parts = score_part.split(':')
    if len(score_parts) != 2:
        raise ValueError("Invalid teams/score format: expected 'Team1 (X:Y) Team2'")
    
    score1_str, score2_str = score_parts
    
    try:
        score1 = int(score1_str)
        score2 = int(score2_str)
    except ValueError:
        raise ValueError("Invalid score: must be non-negative integers")
    
    if score1 < 0 or score2 < 0:
        raise ValueError("Invalid score: must be non-negative integers")
    
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
    if not matches_list:
        return []
    
    filtered_matches = []
    
    for match in matches_list:
        valid = True
        
        for criterion, value in criteria.items():
            if criterion == 'team':
                if match['team1'] != value and match['team2'] != value:
                    valid = False
                    break
            elif criterion == 'date_from':
                if match['date'] < value:
                    valid = False
                    break
            elif criterion == 'date_to':
                if match['date'] > value:
                    valid = False
                    break
            elif criterion == 'min_attendance':
                if match['attendance'] < value:
                    valid = False
                    break
            elif criterion == 'max_attendance':
                if match['attendance'] > value:
                    valid = False
                    break
            elif criterion == 'min_total_goals':
                if match['score1'] + match['score2'] < value:
                    valid = False
                    break
            elif criterion == 'stadium':
                if match['stadium'] != value:
                    valid = False
                    break
        
        if valid:
            filtered_matches.append(match)
    
    return filtered_matches


def calculate_advanced_team_stats(matches_list: List[Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:
    if not matches_list:
        return {}
    
    sorted_matches = sorted(matches_list, key=lambda x: x['date'])
    team_stats = {}
    
    for match in sorted_matches:
        team1, team2 = match['team1'], match['team2']
        score1, score2 = match['score1'], match['score2']
        attendance = match['attendance']
        
        if team1 not in team_stats:
            team_stats[team1] = {
                "points": 0, "matches_played": 0, "wins": 0, "draws": 0, "losses": 0,
                "goals_for": 0, "goals_against": 0, "goal_diff": 0,
                "home_points": 0, "away_points": 0, "win_streak": 0,
                "total_attendance": 0, "last_results": []
            }
        
        if team2 not in team_stats:
            team_stats[team2] = {
                "points": 0, "matches_played": 0, "wins": 0, "draws": 0, "losses": 0,
                "goals_for": 0, "goals_against": 0, "goal_diff": 0,
                "home_points": 0, "away_points": 0, "win_streak": 0,
                "total_attendance": 0, "last_results": []
            }
        
        # Team1 (home)
        team_stats[team1]["matches_played"] += 1
        team_stats[team1]["goals_for"] += score1
        team_stats[team1]["goals_against"] += score2
        team_stats[team1]["goal_diff"] = team_stats[team1]["goals_for"] - team_stats[team1]["goals_against"]
        team_stats[team1]["total_attendance"] += attendance
        
        if score1 > score2:
            team_stats[team1]["points"] += 3
            team_stats[team1]["wins"] += 1
            team_stats[team1]["home_points"] += 3
            team_stats[team1]["last_results"].append('W')
        elif score1 == score2:
            team_stats[team1]["points"] += 1
            team_stats[team1]["draws"] += 1
            team_stats[team1]["home_points"] += 1
            team_stats[team1]["last_results"].append('D')
        else:
            team_stats[team1]["losses"] += 1
            team_stats[team1]["last_results"].append('L')
        
        # Team2 (away)
        team_stats[team2]["matches_played"] += 1
        team_stats[team2]["goals_for"] += score2
        team_stats[team2]["goals_against"] += score1
        team_stats[team2]["goal_diff"] = team_stats[team2]["goals_for"] - team_stats[team2]["goals_against"]
        team_stats[team2]["total_attendance"] += attendance
        
        if score2 > score1:
            team_stats[team2]["points"] += 3
            team_stats[team2]["wins"] += 1
            team_stats[team2]["away_points"] += 3
            team_stats[team2]["last_results"].append('W')
        elif score2 == score1:
            team_stats[team2]["points"] += 1
            team_stats[team2]["draws"] += 1
            team_stats[team2]["away_points"] += 1
            team_stats[team2]["last_results"].append('D')
        else:
            team_stats[team2]["losses"] += 1
            team_stats[team2]["last_results"].append('L')
    
    # Calculate win streaks and average attendance
    result = {}
    for team, stats in team_stats.items():
        win_streak = 0
        for result_char in reversed(stats["last_results"]):
            if result_char == 'W':
                win_streak += 1
            else:
                break
        
        avg_attendance = round(stats["total_attendance"] / stats["matches_played"], 2)
        
        result[team] = {
            "points": stats["points"],
            "matches_played": stats["matches_played"],
            "wins": stats["wins"],
            "draws": stats["draws"],
            "losses": stats["losses"],
            "goals_for": stats["goals_for"],
            "goals_against": stats["goals_against"],
            "goal_diff": stats["goal_diff"],
            "home_points": stats["home_points"],
            "away_points": stats["away_points"],
            "win_streak": win_streak,
            "avg_attendance": avg_attendance
        }
    
    return result


def rank_teams_advanced(team_stats: Dict[str, Dict[str, Any]], 
                       tiebreaker_order: List[str] = ['points', 'goal_diff', 'goals_for']) -> List[Tuple[int, str, int, int]]:
    if not team_stats:
        return []
    
    teams_list = [(team, stats) for team, stats in team_stats.items()]
    
    for criterion in reversed(tiebreaker_order):
        reverse = True
        if criterion == "points":
            teams_list.sort(key=lambda x: x[1]["points"], reverse=reverse)
        elif criterion == "goal_diff":
            teams_list.sort(key=lambda x: x[1]["goal_diff"], reverse=reverse)
        elif criterion == "goals_for":
            teams_list.sort(key=lambda x: x[1]["goals_for"], reverse=reverse)
        elif criterion == "wins":
            teams_list.sort(key=lambda x: x[1]["wins"], reverse=reverse)
    
    result = []
    current_rank = 1
    previous_stats = None
    
    for i, (team, stats) in enumerate(teams_list):
        current_stats = tuple(stats[criterion] for criterion in tiebreaker_order)
        
        if i == 0:
            result.append((current_rank, team, stats["points"], stats["goal_diff"]))
        else:
            if current_stats == previous_stats:
                result.append((current_rank, team, stats["points"], stats["goal_diff"]))
            else:
                current_rank = i + 1
                result.append((current_rank, team, stats["points"], stats["goal_diff"]))
        
        previous_stats = current_stats
    
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
    
    tournament_leader = tournament_table[0][1]
    most_goals_match = max(matches_list, key=lambda x: x['score1'] + x['score2'])
    highest_attendance_match = max(matches_list, key=lambda x: x['attendance'])
    
    most_efficient_team = ""
    max_efficiency = -1.0
    
    for team, stats in team_stats.items():
        if stats['matches_played'] > 0:
            efficiency = round(stats['points'] / stats['matches_played'], 2)
            if efficiency > max_efficiency:
                max_efficiency = efficiency
                most_efficient_team = team
    
    biggest_upset = None
    max_rank_diff = -1
    
    for match in matches_list:
        team1, team2 = match['team1'], match['team2']
        score1, score2 = match['score1'], match['score2']
        
        if score1 == score2 or team1 not in rank_dict or team2 not in rank_dict:
            continue
        
        if score1 > score2:
            winner_rank, loser_rank = rank_dict[team1], rank_dict[team2]
        else:
            winner_rank, loser_rank = rank_dict[team2], rank_dict[team1]
        
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
        total_goals = match['score1'] + match['score2']
        goal_distribution[total_goals] = goal_distribution.get(total_goals, 0) + 1
    
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