import pytest
from src import calculator

# Při testování pozitivných TCs je to OK.
# def test_add():
#     assert calculator.add(1, 2) == 3
#     assert calculator.add(0, 5) == 5
#     assert calculator.add(-2, 9) == 7
#     assert calculator.add(5, -8) == -3


# Zde když je první assert failed další asserty neotestuje.
# def test_add():

#     assert calculator.add_wrong(1, 2) == 3
#     assert calculator.add_wrong(0, 5) == 5
#     assert calculator.add_wrong(-2, 9) == 7
#     assert calculator.add_wrong(0, 0) == 0


# ___Sčítání__
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 3),
        (0, 5, 5),
        (-2, 9, 7),
        (5, -8, -3),
    ],
)

def test_add_parametrized(a, b, expected):
    assert calculator.add(a, b) == expected


# __Špatné sčítání__
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 3),
        (0, 5, 5),
        (-2, 9, 7),
        (0, 0, 0),
    ],
)

def test_add_wrong_parametrized(a, b, expected):
    assert calculator.add_wrong(a, b) == expected


# __Odčítání__
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (55, -15, 70),
        (0, -15, 15),
        (1, 15, -14),
        (55, 15, 40),
    ]
)

def test_substract_parametrized(a, b, expected):
    assert calculator.substract(a, b) == expected


# __Dělení__
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (5, 5, 1),
        (5, 0, 0),
        (5, -1, -5.0),
        (0, 5, 0),
    ]
)

def test_divide(a, b, expected):
    assert calculator.divide(a, b) == expected