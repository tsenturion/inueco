from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict, Iterable, List, Tuple, Optional


_DATE_FMT = "%Y-%m-%d"


def _parse_strict_date(date_str: str) -> datetime.date:
    try:
        if len(date_str) != 10 or date_str[4] != "-" or date_str[7] != "-":
            raise ValueError
        return datetime.strptime(date_str, _DATE_FMT).date()
    except Exception as exc:
        raise ValueError("Invalid date format: expected YYYY-MM-DD") from exc


def parse_match_data(match_string: str) -> Dict[str, Any]:
    if not isinstance(match_string, str):
        raise TypeError("match_string must be a string")

    parts = match_string.split(" | ")
    if len(parts) != 4:
        raise ValueError("Invalid format: expected 4 parts separated by ' | '")

    date_part, teams_part, stadium_part, attendance_part = parts

    _ = _parse_strict_date(date_part)

    import re

    teams_re = re.compile(
        r"^\s*([A-Za-z0-9_]*)\s*\(\s*([^\s:()]+)\s*:\s*([^\s:()]+)\s*\)\s*([A-Za-z0-9_]*)\s*$"
    )
    m = teams_re.match(teams_part)
    if not m:
        raise ValueError("Invalid teams/score format: expected 'Team1 (X:Y) Team2'")

    team1, score1_raw, score2_raw, team2 = m.groups()

    if team1.strip() == "" or team2.strip() == "" or stadium_part.strip() == "":
        raise ValueError("Team names and stadium cannot be empty")

    try:
        score1 = int(score1_raw)
        score2 = int(score2_raw)
        if score1 < 0 or score2 < 0:
            raise ValueError
    except Exception as exc:
        raise ValueError("Invalid score: must be non-negative integers") from exc

    attendance_part_stripped = attendance_part.strip().replace("_", "")
    try:
        attendance = int(attendance_part_stripped)
        if attendance <= 0:
            raise ValueError
    except Exception as exc:
        raise ValueError("Invalid attendance: must be a positive integer") from exc

    return {
        "date": date_part,
        "team1": team1,
        "score1": score1,
        "team2": team2,
        "score2": score2,
        "stadium": stadium_part.strip(),
        "attendance": attendance,
    }


def filter_matches_by_criteria(matches_list: List[Dict[str, Any]], **criteria) -> List[Dict[str, Any]]:
    """
    Фильтрует список матчей по переданным критериям (логическое И).
    Поддерживаемые критерии:
      - team (str)                     : команда участвует (team1/team2)
      - date_from (YYYY-MM-DD)         : дата >=
      - date_to   (YYYY-MM-DD)         : дата <=
      - min_attendance (int)           : посещаемость >=
      - max_attendance (int)           : посещаемость <=
      - min_total_goals (int)          : (score1+score2) >=
      - stadium (str)                  : стадион равен
    Неизвестные критерии игнорируются.
    """

    team = criteria.get("team")
    stadium = criteria.get("stadium")
    date_from = criteria.get("date_from")
    date_to = criteria.get("date_to")
    min_att = criteria.get("min_attendance")
    max_att = criteria.get("max_attendance")
    min_goals = criteria.get("min_total_goals")

    date_from_parsed = _parse_strict_date(date_from) if date_from else None
    date_to_parsed = _parse_strict_date(date_to) if date_to else None

    if min_att is not None and not isinstance(min_att, int):
        raise TypeError("min_attendance must be int")
    if max_att is not None and not isinstance(max_att, int):
        raise TypeError("max_attendance must be int")
    if min_goals is not None and not isinstance(min_goals, int):
        raise TypeError("min_total_goals must be int")

    result: List[Dict[str, Any]] = []

    for m in matches_list:
        m_date = _parse_strict_date(m["date"])

        if team is not None and team != m.get("team1") and team != m.get("team2"):
            continue
        if stadium is not None and stadium != m.get("stadium"):
            continue
        if date_from_parsed and m_date < date_from_parsed:
            continue
        if date_to_parsed and m_date > date_to_parsed:
            continue

        attendance = int(m.get("attendance", 0))
        if min_att is not None and attendance < min_att:
            continue
        if max_att is not None and attendance > max_att:
            continue

        total_goals = int(m.get("score1", 0)) + int(m.get("score2", 0))
        if min_goals is not None and total_goals < min_goals:
            continue

        result.append(m)

    return result


def calculate_advanced_team_stats(matches_list: List[Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:
    teams = set()
    for m in matches_list:
        teams.add(m["team1"])
        teams.add(m["team2"])
    enumerated = list(enumerate(matches_list))
    enumerated.sort(key=lambda kv: (_parse_strict_date(kv[1]["date"]), kv[0]))

    stats: Dict[str, Dict[str, Any]] = {
        t: {
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
        } for t in teams
    }

    results_by_team: Dict[str, List[str]] = {t: [] for t in teams}
    attendance_sums: Dict[str, int] = defaultdict(int)

    for _, m in enumerated:
        t1, t2 = m["team1"], m["team2"]
        s1, s2 = int(m["score1"]), int(m["score2"])
        att = int(m.get("attendance", 0))

        for team in (t1, t2):
            stats[team]["matches_played"] += 1
            attendance_sums[team] += att

        stats[t1]["goals_for"] += s1
        stats[t1]["goals_against"] += s2
        stats[t2]["goals_for"] += s2
        stats[t2]["goals_against"] += s1

        if s1 > s2:
            stats[t1]["wins"] += 1
            stats[t2]["losses"] += 1
            stats[t1]["points"] += 3
            stats[t1]["home_points"] += 3
            results_by_team[t1].append("W")
            results_by_team[t2].append("L")
        elif s1 < s2:
            stats[t2]["wins"] += 1
            stats[t1]["losses"] += 1
            stats[t2]["points"] += 3
            stats[t2]["away_points"] += 3
            results_by_team[t1].append("L")
            results_by_team[t2].append("W")
        else:
            stats[t1]["draws"] += 1
            stats[t2]["draws"] += 1
            stats[t1]["points"] += 1
            stats[t2]["points"] += 1
            stats[t1]["home_points"] += 1
            stats[t2]["away_points"] += 1
            results_by_team[t1].append("D")
            results_by_team[t2].append("D")

    for t in teams:
        stats[t]["goal_diff"] = stats[t]["goals_for"] - stats[t]["goals_against"]

        seq = results_by_team[t]
        streak = 0
        if seq and seq[-1] == "W":
            for r in reversed(seq):
                if r == "W":
                    streak += 1
                else:
                    break
        else:
            streak = 0
        stats[t]["win_streak"] = streak

        mp = stats[t]["matches_played"]
        avg_att = (attendance_sums[t] / mp) if mp > 0 else 0.0
        stats[t]["avg_attendance"] = round(float(avg_att), 2)
    return {t: s for t, s in stats.items() if s["matches_played"] > 0}


def rank_teams_advanced(
    team_stats: Dict[str, Dict[str, Any]],
    tiebreaker_order: List[str] | Tuple[str, ...] = ("points", "goal_diff", "goals_for"),
) -> List[Tuple[int, str, int, int]]:
    supported = {"points", "goal_diff", "goals_for", "wins"}
    order = [c for c in tiebreaker_order if c in supported]
    if not order:
        order = ["points", "goal_diff", "goals_for"]

    def key_tuple(team_name: str) -> Tuple:
        s = team_stats.get(team_name, {})
        values = []
        for crit in order:
            values.append(s.get(crit, 0))
        return tuple(values)

    teams = list(team_stats.keys())
    teams.sort(key=lambda tn: (key_tuple(tn), tn), reverse=True)
    ranked: List[Tuple[int, str, int, int]] = []
    last_key: Optional[Tuple] = None
    current_rank = 0
    for idx, team in enumerate(teams, start=1):
        kt = key_tuple(team)
        if kt != last_key:
            current_rank = idx
            last_key = kt
        s = team_stats[team]
        ranked.append((current_rank, team, int(s.get("points", 0)), int(s.get("goal_diff", 0))))

    return ranked


def generate_analytics_report(
    matches_list: List[Dict[str, Any]],
    team_stats: Dict[str, Dict[str, Any]],
    tournament_table: List[Tuple[int, str, int, int]],
) -> Dict[str, Any]:
    report: Dict[str, Any] = {
        "tournament_leader": None,
        "most_goals_match": None,
        "highest_attendance_match": None,
        "most_efficient_team": None,
        "biggest_upset": None,
        "goal_distribution": {},
        "attendance_by_team": {},
    }

    if tournament_table:
        tournament_table_sorted = sorted(tournament_table, key=lambda r: (r[0], r[1]))
        report["tournament_leader"] = tournament_table_sorted[0][1]

    most_goals = -1
    most_goals_match = None
    for m in matches_list:
        tg = int(m.get("score1", 0)) + int(m.get("score2", 0))
        if tg > most_goals:
            most_goals = tg
            most_goals_match = m
    report["most_goals_match"] = most_goals_match

    max_att = -1
    max_att_match = None
    for m in matches_list:
        att = int(m.get("attendance", 0))
        if att > max_att:
            max_att = att
            max_att_match = m
    report["highest_attendance_match"] = max_att_match

    best_eff_val = -1.0
    best_eff_team: Optional[str] = None
    for team, s in team_stats.items():
        mp = int(s.get("matches_played", 0))
        pts = float(s.get("points", 0))
        eff = round(pts / mp, 2) if mp > 0 else 0.0
        if eff > best_eff_val:
            best_eff_val = eff
            best_eff_team = team
    report["most_efficient_team"] = best_eff_team

    ranks: Dict[str, int] = {}
    for rnk, team_name, _, _ in tournament_table:
        if team_name not in ranks:
            ranks[team_name] = rnk

    biggest_gap = 0
    upset_payload = None

    for m in matches_list:
        s1, s2 = int(m.get("score1", 0)), int(m.get("score2", 0))
        if s1 == s2:
            continue

        winner = m["team1"] if s1 > s2 else m["team2"]
        loser = m["team2"] if s1 > s2 else m["team1"]

        if winner not in ranks or loser not in ranks:
            continue

        winner_rank = ranks[winner]
        loser_rank = ranks[loser]

        if winner_rank > loser_rank:
            gap = winner_rank - loser_rank
            if gap > biggest_gap:
                biggest_gap = gap
                upset_payload = {
                    "match": m,
                    "winner_rank": winner_rank,
                    "loser_rank": loser_rank,
                }

    report["biggest_upset"] = upset_payload

    dist = Counter()
    for m in matches_list:
        tg = int(m.get("score1", 0)) + int(m.get("score2", 0))
        dist[tg] += 1
    report["goal_distribution"] = dict(sorted(dist.items()))

    attendance_by_team = {
        team: round(float(s.get("avg_attendance", 0.0)), 2) for team, s in team_stats.items()
    }
    report["attendance_by_team"] = dict(sorted(attendance_by_team.items()))

    return report


if __name__ == "__main__":
    import sys
    import pprint

    sample_lines = [
        "2024-03-15 | TeamA (3:1) TeamB | StadiumX | 45000",
        "2024-03-16 | TeamC (2:2) TeamA | StadiumY | 30000",
        "2024-03-17 | TeamA (2:0) TeamC | StadiumZ | 40000",
        "2024-03-18 | TeamB (1:0) TeamC | StadiumX | 25000",
    ]

    lines = sample_lines
    if len(sys.argv) > 1:
        path = sys.argv[1]
        try:
            with open(path, "r", encoding="utf-8") as f:
                file_lines = [ln.strip() for ln in f if ln.strip()]
                if file_lines:
                    lines = file_lines
        except Exception as e:
            print(f"[warn] Не удалось прочитать файл '{path}': {e}")
            print("[info] Использую встроенный набор матчей.")

    matches = []
    for i, s in enumerate(lines, 1):
        try:
            matches.append(parse_match_data(s))
        except Exception as e:
            print(f"[warn] Строка {i} пропущена: {e}")

    stats = calculate_advanced_team_stats(matches)
    table = rank_teams_advanced(stats, ['points', 'goal_diff', 'goals_for'])
    report = generate_analytics_report(matches, stats, table)

    print("=== TOURNAMENT TABLE ===")
    pprint.pprint(table)
    print("\n=== REPORT (summary) ===")
    pprint.pprint({
        "tournament_leader": report["tournament_leader"],
        "most_goals_match_total_goals": (
            None if not report["most_goals_match"]
            else report["most_goals_match"]["score1"] + report["most_goals_match"]["score2"]
        ),
        "highest_attendance": (
            None if not report["highest_attendance_match"]
            else report["highest_attendance_match"]["attendance"]
        ),
        "most_efficient_team": report["most_efficient_team"],
        "biggest_upset": report["biggest_upset"],
        "goal_distribution": report["goal_distribution"],
        "attendance_by_team": report["attendance_by_team"],
    })
