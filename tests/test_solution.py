from mytest.solution import analyze_temperature

def test_analyze_temperature():
    assert analyze_temperature(-5) == "freezing"
    assert analyze_temperature(10) == "cold"
    assert analyze_temperature(25) == "warm"
