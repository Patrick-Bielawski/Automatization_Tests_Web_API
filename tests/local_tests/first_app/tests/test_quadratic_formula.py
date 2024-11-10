import pytest 
from src import calculator


# funkce, která testuje, jestli pro korektní vstupy jsou správně spočítané kořeny rovnice
@pytest.mark.parametrize(
    "a, b, c, expected",
    [
        (1, 2, 0, (0.0, -2.0)),
        (1, 3, -10, (2, -5)),
        (3, -21, 30, (5, 2)),
        (2, 9, -5, (0.5, -5)),
    ],
)


def test_quaratic_calculator_correct(a, b, c, expected):
    assert calculator.solve_quadratic_formula(a, b, c) == expected


# funkce, která testuje, jestli pro nekorektní vstup je vyhozena korektní výjimka

@pytest.mark.parametrize(
    "a, b, c, expected_exeption, expected_msg",
    [
        ("a", 1, 2, TypeError, "All coefficients must be of type float or int!"),
        (1, "b", 2, TypeError, "All coefficients must be of type float or int!"),
        (1, 2, "c", TypeError, "All coefficients must be of type float or int!"),
        (0, 1, 2, SyntaxError, "Cannot solve quadratic formula with a = 0!"),
        (1, 5, 2, NameError, "I don't like when b = 5!"),
        (1, -1, 1, ValueError, "Cannot solve quadratic formula with negative discriminant!"),
    ],
)

def test_quadratic_calculator_incorrect(a, b, c, expected_exeption, expected_msg):
    with pytest.raises(expected_exeption) as exc:
        calculator.solve_quadratic_formula(a, b, c)
        assert str(exc.value) == expected_msg