import datetime
from typing import List, Dict, Any, Optional, Tuple


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
    
    if " (" not in teams_score_str or ") " not in teams_score_str:
        raise ValueError("Invalid teams/score format: expected 'Team1 (X:Y) Team2'")
    
    score_start = teams_score_str.find(" (")
    score_end = teams_score_str.find(") ")
    
    team1 = teams_score_str[:score_start].strip()
    score_part = teams_score_str[score_start + 2:score_end]
    team2 = teams_score_str[score_end + 2:].strip()
    
    if ":" not in score_part:
        raise ValueError("Invalid teams/score format: expected 'Team1 (X:Y) Team2'")
    
    try:
        score1_str, score2_str = score_part.split(":")
        score1 = int(score1_str)
        score2 = int(score2_str)
        
        if score1 < 0 or score2 < 0:
            raise ValueError("Invalid score: must be non-negative integers")
    except (ValueError, TypeError):
        raise ValueError("Invalid score: must be non-negative integers")
    
    if not team1 or not team2 or not stadium_str:
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
        "stadium": stadium_str,
        "attendance": attendance
    }


def filter_matches_by_criteria(matches_list: List[Dict[str, Any]], **criteria) -> List[Dict[str, Any]]:

    if not matches_list:
        return []
    
    filtered_matches = []
    
    for match in matches_list:
        valid = True
        
        for criterion, value in criteria.items():
            if criterion == "team":
                if match["team1"] != value and match["team2"] != value:
                    valid = False
                    break
            
            elif criterion == "date_from":
                if match["date"] < value:
                    valid = False
                    break
            
            elif criterion == "date_to":
                if match["date"] > value:
                    valid = False
                    break
            
            elif criterion == "min_attendance":
                if match["attendance"] < value:
                    valid = False
                    break
            
            elif criterion == "max_attendance":
                if match["attendance"] > value:
                    valid = False
                    break
            
            elif criterion == "min_total_goals":
                total_goals = match["score1"] + match["score2"]
                if total_goals < value:
                    valid = False
                    break
            
            elif criterion == "stadium":
                if match["stadium"] != value:
                    valid = False
                    break
        
        if valid:
            filtered_matches.append(match)
    
    return filtered_matches


def calculate_advanced_team_stats(matches_list: List[Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:

    if not matches_list:
        return {}
    
    sorted_matches = sorted(matches_list, key=lambda x: x["date"])
    
    team_stats = {}
    team_match_results = {}  # 
    
    for match in sorted_matches:
        for team in [match["team1"], match["team2"]]:
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
                    "total_attendance": 0
                }
            if team not in team_match_results:
                team_match_results[team] = []
    
    for match in sorted_matches:
        team1, team2 = match["team1"], match["team2"]
        score1, score2 = match["score1"], match["score2"]
        attendance = match["attendance"]
        
        stats1 = team_stats[team1]
        stats1["matches_played"] += 1
        stats1["goals_for"] += score1
        stats1["goals_against"] += score2
        stats1["total_attendance"] += attendance
        
        if score1 > score2: 
            stats1["points"] += 3
            stats1["wins"] += 1
            stats1["home_points"] += 3
            team_match_results[team1].append("win")
        elif score1 == score2: 
            stats1["points"] += 1
            stats1["draws"] += 1
            stats1["home_points"] += 1
            team_match_results[team1].append("draw")
        else: 
            stats1["losses"] += 1
            team_match_results[team1].append("loss")
        
        stats2 = team_stats[team2]
        stats2["matches_played"] += 1
        stats2["goals_for"] += score2
        stats2["goals_against"] += score1
        stats2["total_attendance"] += attendance
        
        if score2 > score1: 
            stats2["points"] += 3
            stats2["wins"] += 1
            stats2["away_points"] += 3
            team_match_results[team2].append("win")
        elif score2 == score1: 
            stats2["points"] += 1
            stats2["draws"] += 1
            stats2["away_points"] += 1
            team_match_results[team2].append("draw")
        else:  
            stats2["losses"] += 1
            team_match_results[team2].append("loss")
    
    for team, stats in team_stats.items():
        stats["goal_diff"] = stats["goals_for"] - stats["goals_against"]
        
        current_streak = 0
        for result in reversed(team_match_results[team]):
            if result == "win":
                current_streak += 1
            else:
                break
        stats["win_streak"] = current_streak
        
        if stats["matches_played"] > 0:
            stats["avg_attendance"] = round(stats["total_attendance"] / stats["matches_played"], 2)
        else:
            stats["avg_attendance"] = 0.0
        
        del stats["total_attendance"]
    
    return team_stats


def rank_teams_advanced(team_stats: Dict[str, Dict[str, Any]], 
                       tiebreaker_order: List[str] = None) -> List[Tuple[int, str, int, int]]:

    if tiebreaker_order is None:
        tiebreaker_order = ['points', 'goal_diff', 'goals_for']
    
    if not team_stats:
        return []
    
    
    teams_list = []
    for team, stats in team_stats.items():
        teams_list.append({
            "name": team,
            "points": stats["points"],
            "goal_diff": stats["goal_diff"],
            "goals_for": stats["goals_for"],
            "wins": stats["wins"]
        })
    

    for criterion in reversed(tiebreaker_order):
        reverse = True  
        if criterion == "points":
            teams_list.sort(key=lambda x: x["points"], reverse=reverse)
        elif criterion == "goal_diff":
            teams_list.sort(key=lambda x: x["goal_diff"], reverse=reverse)
        elif criterion == "goals_for":
            teams_list.sort(key=lambda x: x["goals_for"], reverse=reverse)
        elif criterion == "wins":
            teams_list.sort(key=lambda x: x["wins"], reverse=reverse)
    
    result = []
    
    for i, team in enumerate(teams_list):
        if i == 0:
            result.append((1, team["name"], team["points"], team["goal_diff"]))
        else:
            prev_team_data = teams_list[i-1]
            current_team_data = team
            
            is_equal = all(
                current_team_data[criterion] == prev_team_data[criterion] 
                for criterion in tiebreaker_order
            )
            
            if is_equal:
                prev_rank = result[-1][0]
                result.append((prev_rank, team["name"], team["points"], team["goal_diff"]))
            else:
                result.append((i + 1, team["name"], team["points"], team["goal_diff"]))
    
    return result


def generate_analytics_report(matches_list: List[Dict[str, Any]], 
                            team_stats: Dict[str, Dict[str, Any]], 
                            tournament_table: List[Tuple[int, str, int, int]]) -> Dict[str, Any]:

    report = {
        "tournament_leader": "",
        "most_goals_match": {},
        "highest_attendance_match": {},
        "most_efficient_team": "",
        "biggest_upset": None,
        "goal_distribution": {},
        "attendance_by_team": {}
    }
    
    if not matches_list:
        return report
    
    rank_dict = {}
    for rank, team, points, goal_diff in tournament_table:
        rank_dict[team] = rank
    
    if tournament_table:
        report["tournament_leader"] = tournament_table[0][1]
    
    if matches_list:
        report["most_goals_match"] = max(matches_list, 
                                       key=lambda m: m["score1"] + m["score2"])
    
    if matches_list:
        report["highest_attendance_match"] = max(matches_list, 
                                               key=lambda m: m["attendance"])
    
    efficiency_data = []
    for team, stats in team_stats.items():
        if stats["matches_played"] > 0:
            efficiency = round(stats["points"] / stats["matches_played"], 2)
            efficiency_data.append((team, efficiency, stats["points"], stats["matches_played"]))
    
    if efficiency_data:
        most_efficient = max(efficiency_data, 
                           key=lambda x: (x[1], x[2], -x[3]))
        report["most_efficient_team"] = most_efficient[0]
    
    upset_candidates = []
    for match in matches_list:
        team1, team2 = match["team1"], match["team2"]
        score1, score2 = match["score1"], match["score2"]
        
        if score1 == score2 or team1 not in rank_dict or team2 not in rank_dict:
            continue
        
        if score1 > score2: 
            winner, loser = team1, team2
            winner_rank, loser_rank = rank_dict[team1], rank_dict[team2]
        else:  
            winner, loser = team2, team1
            winner_rank, loser_rank = rank_dict[team2], rank_dict[team1]
        
        if winner_rank > loser_rank:
            upset_candidates.append({
                "match": match,
                "winner_rank": winner_rank,
                "loser_rank": loser_rank,
                "rank_diff": winner_rank - loser_rank
            })
    
    if upset_candidates:
        biggest_upset_candidate = max(upset_candidates, key=lambda x: x["rank_diff"])
        report["biggest_upset"] = {
            "match": biggest_upset_candidate["match"],
            "winner_rank": biggest_upset_candidate["winner_rank"],
            "loser_rank": biggest_upset_candidate["loser_rank"]
        }
    
    for match in matches_list:
        total_goals = match["score1"] + match["score2"]
        report["goal_distribution"][total_goals] = report["goal_distribution"].get(total_goals, 0) + 1
    
    for team, stats in team_stats.items():
        report["attendance_by_team"][team] = stats.get("avg_attendance", 0.0)
    
    return report