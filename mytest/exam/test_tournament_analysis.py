import pytest
import datetime
from tournament_analysis import (
    parse_match_data,
    filter_matches_by_criteria,
    calculate_advanced_team_stats,
    rank_teams_advanced,
    generate_analytics_report
)


class TestParseMatchData:
    """Тесты для функции parse_match_data"""
    
    def test_valid_input(self):
        """Тест корректного формата строки"""
        input_str = "2024-03-15 | Team_A (3:1) Team_B | Stadium_X | 45000"
        expected = {
            "date": "2024-03-15",
            "team1": "Team_A",
            "score1": 3,
            "team2": "Team_B",
            "score2": 1,
            "stadium": "Stadium_X",
            "attendance": 45000
        }
        result = parse_match_data(input_str)
        assert result == expected

    def test_invalid_format_parts(self):
        """Тест неверного количества частей"""
        with pytest.raises(ValueError, match="Invalid format: expected 4 parts separated by ' | '"):
            parse_match_data("2024-03-15 | TeamA (3:1) TeamB")

    def test_invalid_date_format(self):
        """Тест неверного формата даты"""
        with pytest.raises(ValueError, match="Invalid date format: expected YYYY-MM-DD"):
            parse_match_data("2024/03/15 | TeamA (3:1) TeamB | Stadium | 1000")

    def test_invalid_date_values(self):
        """Тест невалидных значений даты"""
        with pytest.raises(ValueError, match="Invalid date format: expected YYYY-MM-DD"):
            parse_match_data("2024-13-01 | TeamA (3:1) TeamB | Stadium | 1000")

    def test_invalid_teams_score_format(self):
        """Тест неверного формата команд и счёта"""
        with pytest.raises(ValueError, match="Invalid teams/score format: expected 'Team1 \\(X:Y\\) Team2'"):
            parse_match_data("2024-03-15 | TeamA 3:1 TeamB | Stadium | 1000")

    def test_invalid_score_non_integer(self):
        """Тест нецелочисленного счёта"""
        with pytest.raises(ValueError, match="Invalid score: must be non-negative integers"):
            parse_match_data("2024-03-15 | TeamA (3:X) TeamB | Stadium | 1000")

    def test_invalid_score_negative(self):
        """Тест отрицательного счёта"""
        with pytest.raises(ValueError, match="Invalid score: must be non-negative integers"):
            parse_match_data("2024-03-15 | TeamA (-1:2) TeamB | Stadium | 1000")

    def test_invalid_attendance_non_integer(self):
        """Тест нецелочисленной посещаемости"""
        with pytest.raises(ValueError, match="Invalid attendance: must be a positive integer"):
            parse_match_data("2024-03-15 | TeamA (3:1) TeamB | Stadium | ABC")

    def test_invalid_attendance_negative(self):
        """Тест отрицательной посещаемости"""
        with pytest.raises(ValueError, match="Invalid attendance: must be a positive integer"):
            parse_match_data("2024-03-15 | TeamA (3:1) TeamB | Stadium | -100")

    def test_empty_team_names(self):
        """Тест пустых названий команд"""
        with pytest.raises(ValueError, match="Team names and stadium cannot be empty"):
            parse_match_data("2024-03-15 |  (3:1) TeamB | Stadium | 1000")

    def test_empty_stadium(self):
        """Тест пустого названия стадиона"""
        with pytest.raises(ValueError, match="Team names and stadium cannot be empty"):
            parse_match_data("2024-03-15 | TeamA (3:1) TeamB |  | 1000")

    def test_zero_scores_valid(self):
        """Тест нулевого счёта (валидный случай)"""
        input_str = "2024-03-15 | Team_A (0:0) Team_B | Stadium_X | 45000"
        result = parse_match_data(input_str)
        assert result["score1"] == 0
        assert result["score2"] == 0

    def test_high_scores_valid(self):
        """Тест высоких значений счёта"""
        input_str = "2024-03-15 | Team_A (10:15) Team_B | Stadium_X | 45000"
        result = parse_match_data(input_str)
        assert result["score1"] == 10
        assert result["score2"] == 15


class TestFilterMatchesByCriteria:
    """Тесты для функции filter_matches_by_criteria"""
    
    @pytest.fixture
    def sample_matches(self):
        return [
            {
                "date": "2024-03-15", 
                "team1": "TeamA", 
                "score1": 3, 
                "team2": "TeamB", 
                "score2": 1, 
                "stadium": "StadiumX", 
                "attendance": 45000
            },
            {
                "date": "2024-03-16", 
                "team1": "TeamC", 
                "score1": 2, 
                "team2": "TeamA", 
                "score2": 2, 
                "stadium": "StadiumY", 
                "attendance": 30000
            },
            {
                "date": "2024-03-17", 
                "team1": "TeamB", 
                "score1": 1, 
                "team2": "TeamC", 
                "score2": 0, 
                "stadium": "StadiumX", 
                "attendance": 25000
            }
        ]

    def test_filter_by_team(self, sample_matches):
        """Тест фильтрации по команде"""
        result = filter_matches_by_criteria(sample_matches, team="TeamA")
        assert len(result) == 2
        assert all("TeamA" in [match["team1"], match["team2"]] for match in result)

    def test_filter_by_date_range(self, sample_matches):
        """Тест фильтрации по диапазону дат"""
        result = filter_matches_by_criteria(
            sample_matches, 
            date_from="2024-03-15", 
            date_to="2024-03-16"
        )
        assert len(result) == 2
        assert all(match["date"] in ["2024-03-15", "2024-03-16"] for match in result)

    def test_filter_by_attendance(self, sample_matches):
        """Тест фильтрации по посещаемости"""
        result = filter_matches_by_criteria(sample_matches, min_attendance=30000)
        assert len(result) == 2
        assert all(match["attendance"] >= 30000 for match in result)

    def test_filter_by_total_goals(self, sample_matches):
        """Тест фильтрации по общему количеству голов"""
        result = filter_matches_by_criteria(sample_matches, min_total_goals=3)
        assert len(result) == 2
        assert all(match["score1"] + match["score2"] >= 3 for match in result)

    def test_filter_by_stadium(self, sample_matches):
        """Тест фильтрации по стадиону"""
        result = filter_matches_by_criteria(sample_matches, stadium="StadiumX")
        assert len(result) == 2
        assert all(match["stadium"] == "StadiumX" for match in result)

    def test_filter_multiple_criteria(self, sample_matches):
        """Тест фильтрации по нескольким критериям"""
        result = filter_matches_by_criteria(
            sample_matches, 
            team="TeamA", 
            min_attendance=40000
        )
        assert len(result) == 1
        assert result[0]["date"] == "2024-03-15"

    def test_empty_result(self, sample_matches):
        """Тест случая, когда нет подходящих матчей"""
        result = filter_matches_by_criteria(
            sample_matches, 
            team="NonexistentTeam"
        )
        assert result == []

    def test_no_criteria(self, sample_matches):
        """Тест без критериев фильтрации"""
        result = filter_matches_by_criteria(sample_matches)
        assert result == sample_matches


class TestCalculateAdvancedTeamStats:
    """Тесты для функции calculate_advanced_team_stats"""
    
    @pytest.fixture
    def sample_matches(self):
        return [
            {
                "date": "2024-03-15", 
                "team1": "TeamA", 
                "score1": 3, 
                "team2": "TeamB", 
                "score2": 1, 
                "stadium": "StadiumX", 
                "attendance": 45000
            },
            {
                "date": "2024-03-16", 
                "team1": "TeamC", 
                "score1": 2, 
                "team2": "TeamA", 
                "score2": 2, 
                "stadium": "StadiumY", 
                "attendance": 30000
            },
            {
                "date": "2024-03-17", 
                "team1": "TeamA", 
                "score1": 2, 
                "team2": "TeamC", 
                "score2": 0, 
                "stadium": "StadiumZ", 
                "attendance": 40000
            },
            {
                "date": "2024-03-18", 
                "team1": "TeamB", 
                "score1": 1, 
                "team2": "TeamC", 
                "score2": 0, 
                "stadium": "StadiumX", 
                "attendance": 25000
            }
        ]

    def test_basic_stats_calculation(self, sample_matches):
        """Тест базового расчёта статистики"""
        stats = calculate_advanced_team_stats(sample_matches)
        
        # Проверка TeamA
        team_a_stats = stats["TeamA"]
        assert team_a_stats["points"] == 7  # 3 (победа) + 1 (ничья) + 3 (победа)
        assert team_a_stats["matches_played"] == 3
        assert team_a_stats["wins"] == 2
        assert team_a_stats["draws"] == 1
        assert team_a_stats["losses"] == 0
        assert team_a_stats["goals_for"] == 7
        assert team_a_stats["goals_against"] == 3
        assert team_a_stats["goal_diff"] == 4

    def test_home_away_points(self, sample_matches):
        """Тест расчёта очков дома и в гостях"""
        stats = calculate_advanced_team_stats(sample_matches)
        
        team_a_stats = stats["TeamA"]
        assert team_a_stats["home_points"] == 6  # два домашних матча (3+3)
        assert team_a_stats["away_points"] == 1  # один выездной матч (1)

    def test_win_streak(self, sample_matches):
        """Тест расчёта серии побед"""
        stats = calculate_advanced_team_stats(sample_matches)
        
        # TeamA: победа, ничья, победа -> win_streak = 1
        assert stats["TeamA"]["win_streak"] == 1
        
        # TeamB: поражение, победа -> win_streak = 1
        assert stats["TeamB"]["win_streak"] == 1
        
        # TeamC: ничья, поражение, поражение -> win_streak = 0
        assert stats["TeamC"]["win_streak"] == 0

    def test_avg_attendance(self, sample_matches):
        """Тест расчёта средней посещаемости"""
        stats = calculate_advanced_team_stats(sample_matches)
        
        # TeamA: (45000 + 30000 + 40000) / 3 = 38333.33
        assert stats["TeamA"]["avg_attendance"] == pytest.approx(38333.33, abs=0.01)

    def test_empty_matches_list(self):
        """Тест пустого списка матчей"""
        stats = calculate_advanced_team_stats([])
        assert stats == {}

    def test_single_team_stats(self):
        """Тест статистики для одной команды"""
        matches = [
            {
                "date": "2024-03-15", 
                "team1": "TeamA", 
                "score1": 1, 
                "team2": "TeamB", 
                "score2": 0, 
                "stadium": "StadiumX", 
                "attendance": 10000
            }
        ]
        stats = calculate_advanced_team_stats(matches)
        
        assert "TeamA" in stats
        assert "TeamB" in stats
        assert stats["TeamA"]["points"] == 3
        assert stats["TeamB"]["points"] == 0


class TestRankTeamsAdvanced:
    """Тесты для функции rank_teams_advanced"""
    
    @pytest.fixture
    def sample_stats(self):
        return {
            "TeamA": {"points": 9, "goal_diff": 5, "goals_for": 10, "wins": 3},
            "TeamB": {"points": 7, "goal_diff": 3, "goals_for": 8, "wins": 2},
            "TeamC": {"points": 7, "goal_diff": 3, "goals_for": 7, "wins": 2},
            "TeamD": {"points": 4, "goal_diff": -2, "goals_for": 5, "wins": 1}
        }

    def test_basic_ranking(self, sample_stats):
        """Тест базового ранжирования"""
        result = rank_teams_advanced(sample_stats)
        
        # Проверяем что TeamA на первом месте, TeamD на последнем
        assert result[0] == (1, "TeamA", 9, 5)
        assert result[3][1] == "TeamD"  # TeamD на последнем месте
        
        # TeamB и TeamC должны быть на 2 и 3 местах (порядок может быть любым)
        teams_at_rank_2_3 = [result[1][1], result[2][1]]
        assert "TeamB" in teams_at_rank_2_3
        assert "TeamC" in teams_at_rank_2_3

    def test_custom_tiebreaker_order(self, sample_stats):
        """Тест с пользовательским порядком критериев"""
        result = rank_teams_advanced(sample_stats, ['points', 'wins', 'goal_diff'])
        
        # При равенстве points и wins, порядок TeamB и TeamC может быть любым
        teams_at_rank_2_3 = [result[1][1], result[2][1]]
        assert "TeamB" in teams_at_rank_2_3
        assert "TeamC" in teams_at_rank_2_3

    def test_tie_ranking_with_different_scores(self):
        """Тест рангов при равенстве очков, но разных дополнительных показателях"""
        stats = {
            "TeamA": {"points": 6, "goal_diff": 5, "goals_for": 8, "wins": 2},
            "TeamB": {"points": 6, "goal_diff": 3, "goals_for": 6, "wins": 2},
            "TeamC": {"points": 3, "goal_diff": 1, "goals_for": 4, "wins": 1}
        }
        result = rank_teams_advanced(stats)
        
        # TeamA и TeamB имеют равные очки, но TeamA имеет лучшую разницу голов
        assert result[0] == (1, "TeamA", 6, 5)
        assert result[1] == (2, "TeamB", 6, 3)
        assert result[2] == (3, "TeamC", 3, 1)

    def test_single_team(self):
        """Тест ранжирования одной команды"""
        stats = {"TeamA": {"points": 3, "goal_diff": 1, "goals_for": 2, "wins": 1}}
        result = rank_teams_advanced(stats)
        assert result == [(1, "TeamA", 3, 1)]

    def test_empty_stats(self):
        """Тест пустой статистики"""
        result = rank_teams_advanced({})
        assert result == []


class TestGenerateAnalyticsReport:
    """Тесты для функции generate_analytics_report"""
    
    @pytest.fixture
    def sample_data(self):
        matches = [
            {
                "date": "2024-03-15", 
                "team1": "TeamA", 
                "score1": 3, 
                "team2": "TeamB", 
                "score2": 1, 
                "stadium": "StadiumX", 
                "attendance": 45000
            },
            {
                "date": "2024-03-16", 
                "team1": "TeamC", 
                "score1": 2, 
                "team2": "TeamA", 
                "score2": 2, 
                "stadium": "StadiumY", 
                "attendance": 50000  # наивысшая посещаемость
            },
            {
                "date": "2024-03-17", 
                "team1": "TeamA", 
                "score1": 5, 
                "team2": "TeamC", 
                "score2": 0, 
                "stadium": "StadiumZ", 
                "attendance": 40000
            },
            {
                "date": "2024-03-18", 
                "team1": "TeamB", 
                "score1": 1, 
                "team2": "TeamC", 
                "score2": 0, 
                "stadium": "StadiumX", 
                "attendance": 25000
            }
        ]
        
        team_stats = {
            "TeamA": {
                "points": 7, "matches_played": 3, "wins": 2, "draws": 1, "losses": 0,
                "goals_for": 10, "goals_against": 3, "goal_diff": 7,
                "home_points": 6, "away_points": 1, "win_streak": 1, "avg_attendance": 45000.0
            },
            "TeamB": {
                "points": 3, "matches_played": 2, "wins": 1, "draws": 0, "losses": 1,
                "goals_for": 2, "goals_against": 3, "goal_diff": -1,
                "home_points": 3, "away_points": 0, "win_streak": 1, "avg_attendance": 35000.0
            },
            "TeamC": {
                "points": 1, "matches_played": 3, "wins": 0, "draws": 1, "losses": 2,
                "goals_for": 2, "goals_against": 8, "goal_diff": -6,
                "home_points": 1, "away_points": 0, "win_streak": 0, "avg_attendance": 38333.33
            }
        }
        
        tournament_table = [
            (1, "TeamA", 7, 7),
            (2, "TeamB", 3, -1),
            (3, "TeamC", 1, -6)
        ]
        
        return matches, team_stats, tournament_table

    @pytest.fixture
    def sample_data_with_upset(self):
        """Данные с явным upset - команда с худшим рангом побеждает команду с лучшим рангом"""
        matches = [
            {
                "date": "2024-03-15", 
                "team1": "TeamA",  # ранг 1
                "score1": 0, 
                "team2": "TeamC",  # ранг 3
                "score2": 1,       # upset: TeamC побеждает TeamA
                "stadium": "StadiumX", 
                "attendance": 45000
            },
            {
                "date": "2024-03-16", 
                "team1": "TeamB", 
                "score1": 2, 
                "team2": "TeamA", 
                "score2": 2, 
                "stadium": "StadiumY", 
                "attendance": 30000
            },
            {
                "date": "2024-03-17", 
                "team1": "TeamC", 
                "score1": 0, 
                "team2": "TeamB", 
                "score2": 1, 
                "stadium": "StadiumZ", 
                "attendance": 25000
            }
        ]
        
        team_stats = {
            "TeamA": {"points": 1, "matches_played": 2, "avg_attendance": 37500.0},
            "TeamB": {"points": 4, "matches_played": 2, "avg_attendance": 27500.0},
            "TeamC": {"points": 3, "matches_played": 2, "avg_attendance": 35000.0}
        }
        
        tournament_table = [
            (1, "TeamA", 1, 0),  # Лучший ранг
            (2, "TeamB", 4, 1),
            (3, "TeamC", 3, -1)  # Худший ранг
        ]
        
        return matches, team_stats, tournament_table

    def test_tournament_leader(self, sample_data):
        """Тест определения лидера турнира"""
        matches, team_stats, table = sample_data
        report = generate_analytics_report(matches, team_stats, table)
        assert report["tournament_leader"] == "TeamA"

    def test_most_goals_match(self, sample_data):
        """Тест определения матча с наибольшим количеством голов"""
        matches, team_stats, table = sample_data
        report = generate_analytics_report(matches, team_stats, table)
        most_goals_match = report["most_goals_match"]
        assert most_goals_match["score1"] + most_goals_match["score2"] == 5  # Матч TeamA vs TeamC

    def test_highest_attendance_match(self, sample_data):
        """Тест определения матча с наибольшей посещаемостью"""
        matches, team_stats, table = sample_data
        report = generate_analytics_report(matches, team_stats, table)
        highest_attendance_match = report["highest_attendance_match"]
        assert highest_attendance_match["attendance"] == 50000

    def test_most_efficient_team(self, sample_data):
        """Тест определения самой эффективной команды"""
        matches, team_stats, table = sample_data
        report = generate_analytics_report(matches, team_stats, table)
        # TeamA: 7/3 ≈ 2.33, TeamB: 3/2 = 1.5, TeamC: 1/3 ≈ 0.33
        assert report["most_efficient_team"] == "TeamA"

    def test_biggest_upset_with_clear_upset(self, sample_data_with_upset):
        """Тест определения upset при наличии явного неожиданного результата"""
        matches, team_stats, table = sample_data_with_upset
        report = generate_analytics_report(matches, team_stats, table)
        
        upset = report["biggest_upset"]
        assert upset is not None
        # TeamC (ранг 3) победил TeamA (ранг 1) - разница рангов = 2
        assert upset["winner_rank"] == 3  # TeamC
        assert upset["loser_rank"] == 1   # TeamA

    def test_goal_distribution(self, sample_data):
        """Тест распределения голов"""
        matches, team_stats, table = sample_data
        report = generate_analytics_report(matches, team_stats, table)
        
        distribution = report["goal_distribution"]
        # В наших данных: 4 гола (матч 1), 4 гола (матч 2), 5 голов (матч 3), 1 гол (матч 4)
        assert distribution[4] == 2
        assert distribution[5] == 1
        assert distribution[1] == 1

    def test_attendance_by_team(self, sample_data):
        """Тест средней посещаемости по командам"""
        matches, team_stats, table = sample_data
        report = generate_analytics_report(matches, team_stats, table)
        
        attendance = report["attendance_by_team"]
        assert attendance["TeamA"] == 45000.0
        assert attendance["TeamB"] == 35000.0
        assert attendance["TeamC"] == pytest.approx(38333.33, abs=0.01)

    def test_no_upsets(self):
        """Тест случая, когда нет неожиданных результатов"""
        matches = [
            {
                "date": "2024-03-15", 
                "team1": "TeamA", 
                "score1": 1, 
                "team2": "TeamB", 
                "score2": 0, 
                "stadium": "StadiumX", 
                "attendance": 10000
            }
        ]
        team_stats = {
            "TeamA": {"points": 3, "matches_played": 1, "avg_attendance": 10000.0},
            "TeamB": {"points": 0, "matches_played": 1, "avg_attendance": 10000.0}
        }
        table = [(1, "TeamA", 3, 1), (2, "TeamB", 0, -1)]
        
        report = generate_analytics_report(matches, team_stats, table)
        assert report["biggest_upset"] is None


def test_integration_full_workflow():
    """Интеграционный тест полного рабочего процесса"""
    # Шаг 1: Парсинг матчей
    match_strings = [
        "2024-03-15 | TeamA (2:1) TeamB | Stadium1 | 15000",
        "2024-03-16 | TeamC (0:0) TeamA | Stadium2 | 20000", 
        "2024-03-17 | TeamB (1:0) TeamC | Stadium1 | 12000"
    ]
    
    matches = [parse_match_data(match_str) for match_str in match_strings]
    assert len(matches) == 3
    
    # Шаг 2: Фильтрация
    filtered = filter_matches_by_criteria(matches, team="TeamA", min_attendance=10000)
    assert len(filtered) == 2
    
    # Шаг 3: Статистика команд
    stats = calculate_advanced_team_stats(matches)
    assert "TeamA" in stats
    assert "TeamB" in stats
    assert "TeamC" in stats
    
    # Шаг 4: Ранжирование
    table = rank_teams_advanced(stats)
    assert len(table) == 3
    
    # Шаг 5: Аналитический отчёт
    report = generate_analytics_report(matches, stats, table)
    assert "tournament_leader" in report
    assert "goal_distribution" in report
    
    # Проверка согласованности данных
    assert report["tournament_leader"] == table[0][1]  # Лидер = первая команда в таблице


if __name__ == "__main__":
    pytest.main([__file__, "-v"])