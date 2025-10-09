import datetime
from typing import List, Dict, Any, Optional, Tuple


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
    
    if '(' not in teams_score_str or ')' not in teams_score_str:
        raise ValueError("Invalid teams/score format: expected 'Team1 (X:Y) Team2'")

    score_start = teams_score_str.find('(')
    score_end = teams_score_str.find(')')
    score_part = teams_score_str[score_start + 1:score_end]
    
    try:
        score1_str, score2_str = score_part.split(':')
        score1 = int(score1_str)
        score2 = int(score2_str)
        
        if score1 < 0 or score2 < 0:
            raise ValueError("Invalid score: must be non-negative integers")
    except (ValueError, TypeError):
        raise ValueError("Invalid score: must be non-negative integers")

    team1 = teams_score_str[:score_start].strip()
    team2 = teams_score_str[score_end + 1:].strip()
    
    if not team1 or not team2:
        raise ValueError("Team names and stadium cannot be empty")

    stadium = stadium_str.strip()
    if not stadium:
        raise ValueError("Team names and stadium cannot be empty")

    try:
        attendance = int(attendance_str)
        if attendance <= 0:
            raise ValueError("Invalid attendance: must be a positive integer")
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
    
    if not matches_list:
        return []
    
    filtered_matches = matches_list.copy()
    
    for key, value in criteria.items():
        if value is None:
            continue
            
        if key == 'team':
            filtered_matches = [match for match in filtered_matches 
                              if match['team1'] == value or match['team2'] == value]
        
        elif key == 'date_from':
            filtered_matches = [match for match in filtered_matches 
                              if match['date'] >= value]
        
        elif key == 'date_to':
            filtered_matches = [match for match in filtered_matches 
                              if match['date'] <= value]
        
        elif key == 'min_attendance':
            filtered_matches = [match for match in filtered_matches 
                              if match['attendance'] >= value]
        
        elif key == 'max_attendance':
            filtered_matches = [match for match in filtered_matches 
                              if match['attendance'] <= value]
        
        elif key == 'min_total_goals':
            filtered_matches = [match for match in filtered_matches 
                              if match['score1'] + match['score2'] >= value]
        
        elif key == 'stadium':
            filtered_matches = [match for match in filtered_matches 
                              if match['stadium'] == value]
    
    return filtered_matches


def calculate_advanced_team_stats(matches_list: List[Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:

    if not matches_list:
        return {}
    
    sorted_matches = sorted(matches_list, key=lambda x: x['date'])
    
    team_stats = {}
    team_matches = {}
    
    for match in sorted_matches:
        team1, team2 = match['team1'], match['team2']
        
        if team1 not in team_matches:
            team_matches[team1] = []
        if team2 not in team_matches:
            team_matches[team2] = []
            
        team_matches[team1].append(('home', match))
        team_matches[team2].append(('away', match))
    
    for team, matches in team_matches.items():
        points = 0
        matches_played = len(matches)
        wins = 0
        draws = 0
        losses = 0
        goals_for = 0
        goals_against = 0
        home_points = 0
        away_points = 0
        total_attendance = 0
        win_streak = 0
        current_streak = 0
        
        for i, (location, match) in enumerate(matches):
            is_home = location == 'home'
            
            if is_home:
                team_score = match['score1']
                opponent_score = match['score2']
            else:
                team_score = match['score2']
                opponent_score = match['score1']
            
            goals_for += team_score
            goals_against += opponent_score
            total_attendance += match['attendance']
            
            if team_score > opponent_score:
                wins += 1
                match_points = 3
                current_streak += 1
            elif team_score == opponent_score:
                draws += 1
                match_points = 1
                current_streak = 0
            else:
                losses += 1
                match_points = 0
                current_streak = 0
            
            points += match_points
            
            if is_home:
                home_points += match_points
            else:
                away_points += match_points
            
            if i == len(matches) - 1: 
                win_streak = current_streak
        
        goal_diff = goals_for - goals_against
        avg_attendance = round(total_attendance / matches_played, 2) if matches_played > 0 else 0
        
        team_stats[team] = {
            "points": points,
            "matches_played": matches_played,
            "wins": wins,
            "draws": draws,
            "losses": losses,
            "goals_for": goals_for,
            "goals_against": goals_against,
            "goal_diff": goal_diff,
            "home_points": home_points,
            "away_points": away_points,
            "win_streak": win_streak,
            "avg_attendance": avg_attendance
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
        team_data = {
            'name': team,
            'points': stats['points'],
            'goal_diff': stats['goal_diff'],
            'goals_for': stats['goals_for'],
            'wins': stats['wins']
        }
        teams_list.append(team_data)
    
    def sort_key(team_data):
        key_values = []
        for criterion in tiebreaker_order:
            if criterion in team_data:
                key_values.append(-team_data[criterion])
            else:
                key_values.append(0)
        return tuple(key_values)
    
    sorted_teams = sorted(teams_list, key=sort_key)
    
    result = []
    current_rank = 1
    prev_team = None
    
    for i, team_data in enumerate(sorted_teams):
        if i == 0:
            result.append((current_rank, team_data['name'], team_data['points'], team_data['goal_diff']))
            prev_team = team_data
        else:
            is_equal = True
            for criterion in tiebreaker_order:
                if criterion in team_data and team_data[criterion] != prev_team[criterion]:
                    is_equal = False
                    break
            
            if is_equal:
                result.append((current_rank, team_data['name'], team_data['points'], team_data['goal_diff']))
            else:
                current_rank = i + 1
                result.append((current_rank, team_data['name'], team_data['points'], team_data['goal_diff']))
            
            prev_team = team_data
    
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
    
    most_goals_match = max(matches_list, key=lambda m: m['score1'] + m['score2'])
    
    highest_attendance_match = max(matches_list, key=lambda m: m['attendance'])
    
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
        
        if (score1 == score2 or 
            team1 not in rank_dict or 
            team2 not in rank_dict):
            continue
        
        if score1 > score2: 
            winner, loser = team1, team2
            winner_rank, loser_rank = rank_dict[team1], rank_dict[team2]
        else:  
            winner, loser = team2, team1
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