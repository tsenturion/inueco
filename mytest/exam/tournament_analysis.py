from __future__ import annotations
from datetime import datetime
from typing import List, Dict, Any, Tuple
from collections import defaultdict, Counter
import re


def parse_match_data(match_string: str) -> Dict[str, Any]:
    if not isinstance(match_string, str):
        raise ValueError("Invalid format: expected 4 parts separated by ' | '")
    parts = match_string.split(" | ")
    if len(parts) != 4:
        raise ValueError("Invalid format: expected 4 parts separated by ' | '")
    date_str, teams_score_str, stadium_str, attendance_str = parts

    # Дата
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
    except Exception:
        raise ValueError("Invalid date format: expected YYYY-MM-DD")

    # Общая форма Team1 (X:Y) Team2 — сначала просто распарсим
    m = re.fullmatch(
        r"\s*([A-Za-z0-9_]*)\s*\(([^:]+):([^)]+)\)\s*([A-Za-z0-9_]*)\s*",
        teams_score_str,
    )
    if not m:
        raise ValueError("Invalid teams/score format: expected 'Team1 (X:Y) Team2'")
    team1, s1_raw, s2_raw, team2 = m.groups()

    # Пустые имена и стадион
    if not team1 or not team2 or not stadium_str.strip():
        raise ValueError("Team names and stadium cannot be empty")

    # Счёт — только неотрицательные целые
    try:
        s1 = int(s1_raw)
        s2 = int(s2_raw)
    except Exception:
        raise ValueError("Invalid score: must be non-negative integers")
    if s1 < 0 or s2 < 0:
        raise ValueError("Invalid score: must be non-negative integers")

    # Посещаемость — положительное целое
    att_str = attendance_str.strip()
    if not re.fullmatch(r"\d+", att_str):
        raise ValueError("Invalid attendance: must be a positive integer")
    attendance = int(att_str)
    if attendance <= 0:
        raise ValueError("Invalid attendance: must be a positive integer")

    return {
        "date": date_str,
        "team1": team1,
        "score1": s1,
        "team2": team2,
        "score2": s2,
        "stadium": stadium_str.strip(),
        "attendance": attendance,
    }

def filter_matches_by_criteria(matches_list: List[Dict[str, Any]], **criteria) -> List[Dict[str, Any]]:
    def to_date(s: str):
        return datetime.strptime(s, "%Y-%m-%d")

    team = criteria.get("team")
    date_from = criteria.get("date_from")
    date_to = criteria.get("date_to")
    min_att = criteria.get("min_attendance")
    max_att = criteria.get("max_attendance")
    min_goals = criteria.get("min_total_goals")
    stadium = criteria.get("stadium")

    date_from_dt = to_date(date_from) if date_from else None
    date_to_dt = to_date(date_to) if date_to else None

    out: List[Dict[str, Any]] = []
    for m in matches_list:
        ok = True
        d = to_date(m["date"])

        if date_from_dt and d < date_from_dt:
            ok = False
        if ok and date_to_dt and d > date_to_dt:
            ok = False
        if ok and team and (m["team1"] != team and m["team2"] != team):
            ok = False
        if ok and stadium and m.get("stadium") != stadium:
            ok = False
        if ok and min_att is not None and m.get("attendance", 0) < int(min_att):
            ok = False
        if ok and max_att is not None and m.get("attendance", 0) > int(max_att):
            ok = False
        if ok and min_goals is not None:
            if int(m.get("score1", 0)) + int(m.get("score2", 0)) < int(min_goals):
                ok = False

        if ok:
            out.append(m)

    return out

def calculate_advanced_team_stats(matches_list: List[Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:
    if not matches_list:
        return {}

    matches_sorted = sorted(matches_list, key=lambda x: x["date"])

    stats: Dict[str, Dict[str, Any]] = {}
    streaks: Dict[str, list] = defaultdict(list)
    att_sum: Dict[str, int] = defaultdict(int)
    att_cnt: Dict[str, int] = defaultdict(int)

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

    for m in matches_sorted:
        t1, t2 = m["team1"], m["team2"]
        s1, s2 = int(m["score1"]), int(m["score2"])
        att = int(m.get("attendance", 0))

        ensure(t1); ensure(t2)

        stats[t1]["matches_played"] += 1
        stats[t2]["matches_played"] += 1

        stats[t1]["goals_for"] += s1
        stats[t1]["goals_against"] += s2
        stats[t2]["goals_for"] += s2
        stats[t2]["goals_against"] += s1

        if s1 > s2:
            stats[t1]["wins"] += 1
            stats[t1]["points"] += 3
            stats[t1]["home_points"] += 3
            streaks[t1].append("W")
            stats[t2]["losses"] += 1
            streaks[t2].append("L")
        elif s1 < s2:
            stats[t2]["wins"] += 1
            stats[t2]["points"] += 3
            stats[t2]["away_points"] += 3
            streaks[t2].append("W")
            stats[t1]["losses"] += 1
            streaks[t1].append("L")
        else:
            # Ничья: по 1 очку всем; и в home_points/away_points тоже по 1
            stats[t1]["draws"] += 1
            stats[t2]["draws"] += 1
            stats[t1]["points"] += 1
            stats[t2]["points"] += 1
            stats[t1]["home_points"] += 1
            stats[t2]["away_points"] += 1
            streaks[t1].append("D")
            streaks[t2].append("D")

        att_sum[t1] += att; att_cnt[t1] += 1
        att_sum[t2] += att; att_cnt[t2] += 1

    for team, st in stats.items():
        st["goal_diff"] = st["goals_for"] - st["goals_against"]
        st["avg_attendance"] = round(att_sum[team] / att_cnt[team], 2) if att_cnt[team] else 0.0

        # текущая серия побед — считаем с конца
        streak = 0
        for r in reversed(streaks[team]):
            if r == "W":
                streak += 1
            else:
                break
        st["win_streak"] = streak

    return stats

def rank_teams_advanced(
    team_stats: Dict[str, Dict[str, Any]],
    tiebreaker_order: Tuple[str, ...] | List[str] = ("points", "goal_diff", "goals_for"),
) -> List[Tuple[int, str, int, int]]:
    if not team_stats:
        return []

    supported = {"points", "goal_diff", "goals_for", "wins"}
    for crit in tiebreaker_order:
        if crit not in supported:
            raise ValueError(f"Unsupported tiebreaker: {crit}")

    rows = []
    for team, st in team_stats.items():
        key = tuple(st.get(k, 0) for k in tiebreaker_order)
        rows.append((team, key, st.get("points", 0), st.get("goal_diff", 0)))

    rows.sort(key=lambda r: (r[1], r[0]), reverse=True)

    ranked: List[Tuple[int, str, int, int]] = []
    prev_key = None
    current_rank = 0
    processed = 0
    for team, key, pts, gd in rows:
        processed += 1
        if key != prev_key:
            current_rank = processed
            prev_key = key
        ranked.append((current_rank, team, pts, gd))

    return ranked

def generate_analytics_report(
    matches_list: List[Dict[str, Any]],
    team_stats: Dict[str, Dict[str, Any]],
    tournament_table: List[Tuple[int, str, int, int]],
) -> Dict[str, Any]:
    report: Dict[str, Any] = {
        "tournament_leader": "",
        "most_goals_match": None,
        "highest_attendance_match": None,
        "most_efficient_team": None,
        "biggest_upset": None,
        "goal_distribution": {},
        "attendance_by_team": {},
    }

    if tournament_table:
        report["tournament_leader"] = tournament_table[0][1]

    if matches_list:
        most_goals = -1
        most_goals_match = None
        best_att = -1
        best_att_match = None
        dist = Counter()

        for m in matches_list:
            total = int(m.get("score1", 0)) + int(m.get("score2", 0))
            dist[total] += 1
            if total > most_goals:
                most_goals = total
                most_goals_match = m
            att = int(m.get("attendance", 0))
            if att > best_att:
                best_att = att
                best_att_match = m

        report["most_goals_match"] = most_goals_match
        report["highest_attendance_match"] = best_att_match
        report["goal_distribution"] = dict(sorted(dist.items()))

    if team_stats:
        best_eff = -1.0
        best_team = None
        for team, st in team_stats.items():
            mp = st.get("matches_played", 0)
            if mp <= 0:
                continue
            eff = round(st.get("points", 0) / mp, 2)
            if eff > best_eff:
                best_eff = eff
                best_team = team
        report["most_efficient_team"] = best_team

    if matches_list and tournament_table:
        rank_map = {team: rank for (rank, team, _p, _gd) in tournament_table}
        best_diff = 0
        upset = None
        for m in matches_list:
            s1, s2 = int(m["score1"]), int(m["score2"])
            if s1 == s2:
                continue
            winner = m["team1"] if s1 > s2 else m["team2"]
            loser = m["team2"] if s1 > s2 else m["team1"]
            if winner not in rank_map or loser not in rank_map:
                continue
            wr, lr = rank_map[winner], rank_map[loser]
            diff = wr - lr  
            if diff > best_diff:
                best_diff = diff
                upset = {"match": m, "winner_rank": wr, "loser_rank": lr}
        report["biggest_upset"] = upset

    if team_stats:
        report["attendance_by_team"] = {t: st.get("avg_attendance", 0.0) for t, st in team_stats.items()}
    return report