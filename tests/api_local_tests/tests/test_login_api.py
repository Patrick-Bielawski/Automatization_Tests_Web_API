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


# Test pro špatné vstupy

@pytest.mark.parametrize("user, passwd, expected_exception", [
    ("unknown_user", "wrong_password", LookupError),  
    ("admin", "wrong_password", NameError),          
    ("joe", "12345", NameError),                      
    ("", "", LookupError),                            
],
)
def test_login_incorrect(user, passwd, expected_exception):
    with pytest.raises(expected_exception):
        login_api.login(user, passwd)



# -----------------------------------------------------------------------------
# -------------------- TEST GET SECRET ---------------------------------
# -----------------------------------------------------------------------------


@pytest.mark.parametrize("user, passwd, expected_secret",
                         [
                             ("admin", "admin", "tajemství"),
                             ("joe", "heslo", "tajemství_joa"),
                             ("fred", "password", "tajemství_freda"),
                             ("bob", "1234", "tajemství_boba"),
                         ],
                         )

def test_get_secret_correct(user, passwd, expected_secret):
    token = login_api.login(user, passwd)
    assert login_api.get_secret(token) == expected_secret
    login_api.logout(token)

def test_get_secret_wrong_auth():
    with pytest.raises(ValueError):
        login_api.get_secret("random")


# -------------------------------------------------------------------------
# ---------------- TEST LOGOUT --------------------------------------
# -------------------------------------------------------------------------

@pytest.mark.parametrize("user, passwd",
                         [
                             ("admin", "admin"),
                             ("joe", "heslo"),
                             ("bob", "1234"),
                             ("fred", "password"),
                         ],
                         )

def test_logout(user, passwd):
    token = login_api.login(user, passwd)
    login_api.logout(token)
    with pytest.raises(ValueError):
        login_api.get_secret(token)