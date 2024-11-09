# Testování výjímek

import pytest
from src import calculator

# __Vyhodnotí výjimku jako __FAILURE
# def test_divide_naive():
#     assert calculator.divide(5, 0) == ValueError

# __Vyhodnotí výjimku jako PASS__
# def test_divide():
#     with pytest.raises(ValueError):
#         calculator.divide(5, 0)

# __Testování zpráv u výjimek__

def test_divide():
    with pytest.raises(ValueError) as exc:
        calculator.divide(5, 0)
    assert str(exc.value) == "Cannot divide by zero!"


# __Testování výjimek s parametrize__

@pytest.mark.parametrize(
    "a, b, expected_exception, expected_msg",
    [
        (0, 5, ValueError, "Cannot take log of non_positive number!"),
        (-2, 5, ValueError, "Cannot take log of non_positive number!"),
        (9, -2, ZeroDivisionError, "Cannot take log with non-positive base!"),
        (5, 1, NameError, "Cannot take log with base 1!"),
    ],
)
def test_log(a, b, expected_exception, expected_msg):
    with pytest.raises(expected_exception) as exc_info:
         calculator.log(a, b)
    assert str(exc_info.value) == expected_msg