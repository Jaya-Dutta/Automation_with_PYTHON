import pytest


@pytest.fixture
def calculator_data():
    """
    Fixture provides common test data.
    PyTest automatically injects this fixture
    into any test that requests calculator_data.
    """
    return {
        "a": 10,
        "b": 5
    }