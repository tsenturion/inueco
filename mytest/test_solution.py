import pytest
from solution import analyze_temperature


class TestAnalyzeTemperature:
    """Тесты для функции analyze_temperature"""
    def test_normal_week(self):
        """Тест с обычными данными за неделю"""
        temperatures = [22, 28, 15, 8, 30, 18, 25]
        result = analyze_temperature(temperatures)
        assert result is not None
        assert result["average"] == 20.9
        assert result["max"] == 30
        assert result["min"] == 8
        assert result["hot_days"] == 2
        assert result["cold_days"] == 1
    def test_all_hot_days(self):
        """Тест когда все дни жаркие"""
        temperatures = [26, 27, 28, 29, 30, 31, 32]
        result = analyze_temperature(temperatures)
        assert result["hot_days"] == 7
        assert result["cold_days"] == 0
        assert result["max"] == 32
        assert result["min"] == 26
    def test_all_cold_days(self):
        """Тест когда все дни холодные"""
        temperatures = [5, 6, 3, 2, 8, 9, 4]
        result = analyze_temperature(temperatures)
        assert result["hot_days"] == 0
        assert result["cold_days"] == 7
        assert result["max"] == 9
        assert result["min"] == 2
    def test_moderate_temperatures(self):
        """Тест с умеренными температурами (нет жарких и холодных дней)"""
        temperatures = [15, 16, 17, 18, 19, 20, 21]
        result = analyze_temperature(temperatures)
        assert result["hot_days"] == 0
        assert result["cold_days"] == 0
        assert result["average"] == 18.0
    def test_empty_list(self):
        """Тест с пустым списком"""
        temperatures = []
        result = analyze_temperature(temperatures)
        assert result is None
    def test_too_few_days(self):
        """Тест с недостаточным количеством дней"""
        temperatures = [15, 16, 17]
        result = analyze_temperature(temperatures)
        assert result is None
    def test_too_many_days(self):
        """Тест со слишком большим количеством дней"""
        temperatures = [15, 16, 17, 18, 19, 20, 21, 22]
        result = analyze_temperature(temperatures)
        assert result is None
    def test_negative_temperatures(self):
        """Тест с отрицательными температурами"""
        temperatures = [-5, -10, 0, 5, 15, 20, 25]
        result = analyze_temperature(temperatures)
        assert result is not None
        assert result["min"] == -10
        assert result["cold_days"] == 5
    def test_boundary_values(self):
        """Тест с граничными значениями (точно 10 и 25 градусов)"""
        temperatures = [10, 10, 25, 25, 15, 15, 20]
        result = analyze_temperature(temperatures)
        assert result["hot_days"] == 0
        assert result["cold_days"] == 0
    def test_extreme_temperatures(self):
        """Тест с экстремальными температурами"""
        temperatures = [-30, -20, 40, 50, 0, 10, 25]
        result = analyze_temperature(temperatures)
        assert result["max"] == 50
        assert result["min"] == -30
        assert result["hot_days"] == 2
        assert result["cold_days"] == 2
    def test_all_same_temperature(self):
        """Тест когда все дни одинаковая температура"""
        temperatures = [20, 20, 20, 20, 20, 20, 20]
        result = analyze_temperature(temperatures)
        assert result["average"] == 20.0
        assert result["max"] == 20
        assert result["min"] == 20
        assert result["hot_days"] == 0
        assert result["cold_days"] == 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
