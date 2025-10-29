import pytest

@pytest.mark.parametrize('number', [1, 2, 3, 4, 5])
def test_is_positive(number):
    assert number > 0

@pytest.mark.parametrize('a, b, expected', [
    (1, 2, 3),
    (2, 3, 5),
    (0, 0, 0),
])
def test_add(a, b, expected):
    assert a + b == expected