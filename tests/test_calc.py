import pytest
from app.calc import *

# Parametrization 
@pytest.mark.parametrize("num1, num2, expected",
    [
        (3, 2, 5),
        (2, 7, 9),
        (1, 1, 2)
    ])
def test_add(num1, num2, expected):
    assert add(num1, num2) == expected
