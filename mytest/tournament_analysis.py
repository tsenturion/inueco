from datetime import datetime
from typing import Dict, List, Tuple, Any, Optional, Union
import re
import math

def parse_match_data(match_string: str) -> Dict[str, Any]:
    if not isinstance(match_string, str):
        raise ValueError("Invalid format: expected 4 parts separated by ' | '")
    parts = match_string.split(" | ")
    if len(parts) != 4:
        raise ValueError("Invalid format: expected 4 parts separated by ' | '")
    date_str, teams_part, stadium, attendance_str = (p.strip() for p in parts)
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", date_str):
        raise ValueError("Invalid date format: expected YYYY-MM-DD")
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid date format: expected YYYY-MM-DD")
    m = re.fullmatch(
        r"\s*(?P<team1>.*?)\s*\(\s*(?P<s1>[^:]+)\s*:\s*(?P<s2>[^)]+)\s*\)\s*(?P<team2>.*)\s*",
        teams_part,
    )
    if not m:
        raise ValueError("Invalid teams/score format: expected 'Team1 (X:Y) Team2'")
    team1 = m.group("team1").strip()
    team2 = m.group("team2").strip()
    s1_raw = m.group("s1").strip()
    s2_raw = m.group("s2").strip()
    if not team1 or not team2 or not stadium:
        raise ValueError("Team names and stadium cannot be empty")
    try:
        s1 = int(s1_raw)
        s2 = int(s2_raw)
    except Exception:
        raise ValueError("Invalid score: must be non-negative integers")
    if s1 < 0 or s2 < 0:
        raise ValueError("Invalid score: must be non-negative integers")
    try:
        attendance = int(attendance_str)
    except Exception:
        raise ValueError("Invalid attendance: must be a positive integer")
    if attendance <= 0:
        raise ValueError("Invalid attendance: must be a positive integer")
    return {
        "date": date_str,
        "team1": team1,
        "score1": s1,
        "team2": team2,
        "score2": s2,
        "stadium": stadium,
        "attendance": attendance,
    }

def filter_matches_by_criteria(matches_list: List[Dict[str, Any]], **criteria) -> List[Dict[str, Any]]:
    def date_ok(d: str, f: Optional[str], t: Optional[str]) -> bool:
        if f and d < f:
            return False
        if t and d > t:
            return False
        return True
    team = criteria.get("team")
    date_from = criteria.get("date_from")
    date_to = criteria.get("date_to")
    min_att = criteria.get("min_attendance")
    max_att = criteria.get("max_attendance")
    min_goals = criteria.get("min_total_goals")
    stadium = criteria.get("stadium")
    result: List[Dict[str, Any]] = []
    for m in matches_list:
        if team and (m["team1"] != team and m["team2"] != team):
            continue
        if not date_ok(m["date"], date_from, date_to):
            continue
        if min_att is not None and m["attendance"] < int(min_att):
            continue
        if max_att is not None and m["attendance"] > int(max_att):
            continue
        if min_goals is not None and (m["score1"] + m["score2"]) < int(min_goals):
            continue
        if stadium and m["stadium"] != stadium:
            continue
        result.append(m)
    return result

def calculate_advanced_team_stats(matches_list: List[Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:
    matches_sorted = sorted(matches_list, key=lambda x: x["date"])
    stats: Dict[str, Dict[str, Any]] = {}
    sums: Dict[str, Dict[str, float]] = {}
    streak: Dict[str, int] = {}
    def ensure(team: str):
        if team not in stats:
            stats[team] = {
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
                "avg_attendance": 0.0,
            }
            sums[team] = {"att_sum": 0.0, "games": 0}
            streak[team] = 0
    for m in matches_sorted:
        t1, t2 = m["team1"], m["team2"]
        s1, s2 = int(m["score1"]), int(m["score2"])
        att = float(m["attendance"])
        ensure(t1)
        ensure(t2)
        for team, gf, ga in ((t1, s1, s2), (t2, s2, s1)):
            st = stats[team]
            st["matches_played"] += 1
            st["goals_for"] += gf
            st["goals_against"] += ga
            st["goal_diff"] = st["goals_for"] - st["goals_against"]
            sums[team]["att_sum"] += att
            sums[team]["games"] += 1
        if s1 > s2:
            stats[t1]["wins"] += 1
            stats[t2]["losses"] += 1
            stats[t1]["points"] += 3
            stats[t1]["home_points"] += 3
            streak[t1] += 1
            streak[t2] = 0
        elif s1 < s2:
            stats[t2]["wins"] += 1
            stats[t1]["losses"] += 1
            stats[t2]["points"] += 3
            stats[t2]["away_points"] += 3
            streak[t2] += 1
            streak[t1] = 0
        else:
            stats[t1]["draws"] += 1
            stats[t2]["draws"] += 1
            stats[t1]["points"] += 1
            stats[t2]["points"] += 1
            stats[t1]["home_points"] += 1
            stats[t2]["away_points"] += 1
            streak[t1] = 0
            streak[t2] = 0
    for team, st in stats.items():
        g = sums[team]["games"]
        st["avg_attendance"] = round(sums[team]["att_sum"] / g, 2) if g > 0 else 0.0
        st["win_streak"] = streak[team]
    return stats

def rank_teams_advanced(
    team_stats: Dict[str, Dict[str, Any]],
    tiebreaker_order: Union[List[str], Tuple[str, ...]] = ("points", "goal_diff", "goals_for"),
) -> List[Tuple[int, str, int, int]]:
    order = list(tiebreaker_order)
    def sort_key(item):
        team, st = item
        vals = [-(int(st.get(crit, 0))) for crit in order]
        vals.append(team)
        return tuple(vals)
    sorted_items = sorted(team_stats.items(), key=sort_key)
    table: List[Tuple[int, str, int, int]] = []
    prev_key = None
    current_rank = 0
    for idx, (team, st) in enumerate(sorted_items, start=1):
        key_vals = tuple(st.get(crit, 0) for crit in order)
        if key_vals != prev_key:
            current_rank = idx
            prev_key = key_vals
        table.append((current_rank, team, int(st.get("points", 0)), int(st.get("goal_diff", 0))))
    return table

def generate_analytics_report(
    matches_list: List[Dict[str, Any]],
    team_stats: Dict[str, Dict[str, Any]],
    tournament_table: List[Tuple[int, str, int, int]],
) -> Dict[str, Any]:
    report: Dict[str, Any] = {}
    report["tournament_leader"] = tournament_table[0][1] if tournament_table else None
    most_goals_match = None
    most_goals = -1
    highest_att_match = None
    highest_att = -1
    goal_distribution: Dict[int, int] = {}
    for m in matches_list:
        total_g = int(m["score1"]) + int(m["score2"])
        if total_g > most_goals:
            most_goals = total_g
            most_goals_match = m
        if int(m["attendance"]) > highest_att:
            highest_att = int(m["attendance"])
            highest_att_match = m
        goal_distribution[total_g] = goal_distribution.get(total_g, 0) + 1
    report["most_goals_match"] = most_goals_match
    report["highest_attendance_match"] = highest_att_match
    report["goal_distribution"] = goal_distribution
    best_team = None
    best_eff = -math.inf
    for team, st in team_stats.items():
        mp = st.get("matches_played", 0)
        eff = round(st.get("points", 0) / mp, 2) if mp else 0.0
        if eff > best_eff:
            best_eff = eff
            best_team = team
    report["most_efficient_team"] = best_team
    rank_map: Dict[str, int] = {team: r for (r, team, _, _) in tournament_table}
    biggest = None
    best_delta = 0
    for m in matches_list:
        s1, s2 = int(m["score1"]), int(m["score2"])
        if s1 == s2:
            continue
        t1, t2 = m["team1"], m["team2"]
        if t1 not in rank_map or t2 not in rank_map:
            continue
        if s1 > s2:
            winner, loser = t1, t2
        else:
            winner, loser = t2, t1
        w_rank, l_rank = rank_map[winner], rank_map[loser]
        if w_rank > l_rank:
            delta = w_rank - l_rank
            if delta > best_delta:
                best_delta = delta
                biggest = {"match": m, "winner_rank": w_rank, "loser_rank": l_rank}
    report["biggest_upset"] = biggest
    report["attendance_by_team"] = {team: round(st.get("avg_attendance", 0.0), 2) for team, st in team_stats.items()}
    return report
