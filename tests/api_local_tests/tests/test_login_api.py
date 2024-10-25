import pytest
from src import login_api

users = {
    "admin": ["admin", "tajemství", "authTokenAdmina"],
    "joe": ["heslo", "tajemství_joa", "authTokenJoa"],
    "fred": ["password", "tajemství_freda", "authTokenFreda"],
    "bob": ["1234", "tajemství_boba", "authTokenBoba"],
}

# --------------------------------------------------------------------
# --------- TEST LOGIN API --------------------------------------
# --------------------------------------------------------------------


@pytest.mark.parametrize("user, passwd, expected_token", [
    ("admin", "admin", "authTokenAdmina"),
    ("joe", "heslo", "authTokenJoa"),
    ("fred", "password", "authTokenFreda"),
    ("bob", "1234", "authTokenBoba"),

],
)

def test_login_correct(user, passwd, expected_token):
    # tato funkce testuje dobré vstupy
    assert login_api.login(user, passwd) == expected_token
    login_api.logout(expected_token)

