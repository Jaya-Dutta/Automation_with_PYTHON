import pytest

# Basic test case
def test_addition():
    result = 10 + 5
    assert result == 15

# Assertion examples
def test_string():
    name = "Selenium"
    assert name == "Selenium"
    assert "Python" not in name
def test_comparison():
    number = 10

    assert number > 5
    assert number >= 10
    assert number != 0

# Multiple test cases
def test_subtraction():
    assert 10 - 5 == 5
def test_multiplication():
    assert 10 * 5 == 50

# Parameterization: run the same test with multiple data sets
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),
        (10, 5, 15),
        (20, 10, 30),
    ],
)
def test_addition_multiple_data(a, b, expected):
    assert a + b == expected

def test_fixture_data(calculator_data):
    """Use data provided by the conftest.py fixture."""
    a = calculator_data["a"]
    b = calculator_data["b"]

    assert a + b == 15