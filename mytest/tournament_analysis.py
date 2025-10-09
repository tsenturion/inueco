import re
from datetime import datetime
from collections import defaultdict

def parse_match_data(match_string):
    parts = match_string.split(" | ")
    if len(parts) != 4:
        raise ValueError("Invalid format: expected 4 parts separated by ' | '")
    date_str, teams_score_str, stadium, attendance_str = parts

    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        date = date_str
    except ValueError:
        raise ValueError("Invalid date format: expected YYYY-MM-DD")

    teams_score_pattern = r'^([a-zA-Z0-9_]*?)\s+\(([^:]+):([^)]+)\)\s+([a-zA-Z0-9_]*?)$'
    match = re.match(teams_score_pattern, teams_score_str)
    if not match:
        raise ValueError("Invalid teams/score format: expected 'Team1 (X:Y) Team2'")

    team1, score1_str, score2_str, team2 = match.groups()

    try:
        score1 = int(score1_str)
        score2 = int(score2_str)
        if score1 < 0 or score2 < 0:
            raise ValueError
    except ValueError:
        raise ValueError("Invalid score: must be non-negative integers")

    try:
        attendance = int(attendance_str)
        if attendance <= 0:
            raise ValueError
    except ValueError:
        raise ValueError("Invalid attendance: must be a positive integer")

    if team1 == "" or team2 == "" or stadium == "":
        raise ValueError("Team names and stadium cannot be empty")
    return {
        "date": date,
        "team1": team1,
        "score1": score1,
        "team2": team2,
        "score2": score2,
        "stadium": stadium,
        "attendance": attendance
    }


def filter_matches_by_criteria(matches_list, **criteria):
    result = []
    for match in matches_list:
        include = True

        if "team" in criteria:
            team = criteria["team"]
            if match["team1"] != team and match["team2"] != team:
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
            result.append(match)
    print(match)
    return result


def calculate_advanced_team_stats(matches_list):
    if not matches_list:
        return {}

    sorted_matches = sorted(matches_list, key=lambda x: x["date"])

    stats = defaultdict(lambda: {
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
        "attendances": []
    })

    for match in sorted_matches:
        team1 = match["team1"]
        stats[team1]["matches_played"] += 1
        stats[team1]["goals_for"] += match["score1"]
        stats[team1]["goals_against"] += match["score2"]
        stats[team1]["attendances"].append(match["attendance"])
        if match["score1"] > match["score2"]:
            stats[team1]["wins"] += 1
            stats[team1]["points"] += 3
            stats[team1]["home_points"] += 3
        elif match["score1"] == match["score2"]:
            stats[team1]["draws"] += 1
            stats[team1]["points"] += 1
            stats[team1]["home_points"] += 1
        else:
            stats[team1]["losses"] += 1

        team2 = match["team2"]
        stats[team2]["matches_played"] += 1
        stats[team2]["goals_for"] += match["score2"]
        stats[team2]["goals_against"] += match["score1"]
        stats[team2]["attendances"].append(match["attendance"])
        if match["score2"] > match["score1"]:
            stats[team2]["wins"] += 1
            stats[team2]["points"] += 3
            stats[team2]["away_points"] += 3
        elif match["score2"] == match["score1"]:
            stats[team2]["draws"] += 1
            stats[team2]["points"] += 1
            stats[team2]["away_points"] += 1
        else:
            stats[team2]["losses"] += 1

    for team in stats:
        stats[team]["goal_diff"] = stats[team]["goals_for"] - stats[team]["goals_against"]

    team_results = defaultdict(list)
    for match in sorted_matches:
        team1 = match["team1"]
        team2 = match["team2"]
        if match["score1"] > match["score2"]:
            team_results[team1].append("W")
            team_results[team2].append("L")
        elif match["score1"] < match["score2"]:
            team_results[team1].append("L")
            team_results[team2].append("W")
        else:
            team_results[team1].append("D")
            team_results[team2].append("D")
    for team in team_results:
        results = team_results[team]
        streak = 0
        
        for i in range(len(results) - 1, -1, -1):
            if results[i] == "W":
                streak += 1
            else:
                break
        
        stats[team]["win_streak"] = streak

    final_stats = {}
    for team in stats:
        attendances = stats[team]["attendances"]
        avg_attendance = round(sum(attendances) / len(attendances), 2) if attendances else 0.0
        
        final_stats[team] = {
            "points": stats[team]["points"],
            "matches_played": stats[team]["matches_played"],
            "wins": stats[team]["wins"],
            "draws": stats[team]["draws"],
            "losses": stats[team]["losses"],
            "goals_for": stats[team]["goals_for"],
            "goals_against": stats[team]["goals_against"],
            "goal_diff": stats[team]["goal_diff"],
            "home_points": stats[team]["home_points"],
            "away_points": stats[team]["away_points"],
            "win_streak": stats[team]["win_streak"],
            "avg_attendance": avg_attendance
        }
    return final_stats


def rank_teams_advanced(team_stats, tiebreaker_order=['points', 'goal_diff', 'goals_for']):
    if not team_stats:
        return []
    teams = []
    for team, stats in team_stats.items():
        teams.append((team, stats))
    for criterion in reversed(tiebreaker_order):
        teams.sort(key=lambda x: x[1][criterion], reverse=True)
    ranked_teams = []
    current_rank = 1
    for i, (team, stats) in enumerate(teams):
        if i > 0:
            prev_team = teams[i-1]
            is_equal = True
            for criterion in tiebreaker_order:
                if prev_team[1][criterion] != stats[criterion]:
                    is_equal = False
                    break
            if is_equal:
                current_rank = ranked_teams[-1][0]
            else:
                current_rank = i + 1
        
        ranked_teams.append((current_rank, team, stats["points"], stats["goal_diff"]))
    return ranked_teams


def generate_analytics_report(matches_list, team_stats, tournament_table):
    report = {}
    if tournament_table:
        report["tournament_leader"] = tournament_table[0][1]
    else:
        report["tournament_leader"] = None
    if matches_list:
        most_goals_match = max(matches_list, key=lambda x: x["score1"] + x["score2"])
        report["most_goals_match"] = most_goals_match
    else:
        report["most_goals_match"] = None
    if matches_list:
        highest_attendance_match = max(matches_list, key=lambda x: x["attendance"])
        report["highest_attendance_match"] = highest_attendance_match
    else:
        report["highest_attendance_match"] = None
    if team_stats:
        efficiency = {}
        for team, stats in team_stats.items():
            if stats["matches_played"] > 0:
                efficiency[team] = round(stats["points"] / stats["matches_played"], 2)
            else:
                efficiency[team] = 0.0
        most_efficient_team = max(efficiency, key=efficiency.get)
        report["most_efficient_team"] = most_efficient_team
    else:
        report["most_efficient_team"] = None

    team_ranks = {}
    for rank, team, points, goal_diff in tournament_table:
        team_ranks[team] = rank

    biggest_upset = None
    max_rank_diff = 0

    for match in matches_list:
        team1, team2 = match["team1"], match["team2"]
        score1, score2 = match["score1"], match["score2"]
        if team1 in team_ranks and team2 in team_ranks:
            rank1, rank2 = team_ranks[team1], team_ranks[team2]
            if score1 > score2:
                if rank1 > rank2:
                    rank_diff = rank1 - rank2
                    if rank_diff > max_rank_diff:
                        max_rank_diff = rank_diff
                        biggest_upset = {
                            "match": match,
                            "winner_rank": rank1,
                            "loser_rank": rank2
                        }
            elif score2 > score1:
                if rank2 > rank1:
                    rank_diff = rank2 - rank1
                    if rank_diff > max_rank_diff:
                        max_rank_diff = rank_diff
                        biggest_upset = {
                            "match": match,
                            "winner_rank": rank2,
                            "loser_rank": rank1
                        }

    report["biggest_upset"] = biggest_upset
    goal_distribution = defaultdict(int)
    for match in matches_list:
        total_goals = match["score1"] + match["score2"]
        goal_distribution[total_goals] += 1

    report["goal_distribution"] = dict(goal_distribution)
    attendance_by_team = {}
    for team, stats in team_stats.items():
        attendance_by_team[team] = stats["avg_attendance"]
    report["attendance_by_team"] = attendance_by_team
    return report