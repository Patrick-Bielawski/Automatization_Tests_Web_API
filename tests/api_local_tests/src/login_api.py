class User:
    def __init__(self, username, password, secret, authToken):
        self.username = username
        self.password = password
        self.secret = secret
        self.active = False
        self.auth = authToken

    def login(self):
        self.active = True
        return self.auth

users = [
    User("admin", "admin", "tajemství", "authTokenAdmina"),
    User("joe", "heslo", "tajemství_joa", "authTokenJoa"),
    User("fred", "password", "tajemství_freda", "authTokenFreda"),
    User("bob", "1234", "tajemství_boba", "authTokenBoba"),
]

joe_should_been_logged_out = False

def login(username: str, password: str) -> str:
    for user in users:
        if user.username == username:
            if user.password == password:
                return user.login()
            else:
                raise NameError("Neplatné heslo")
    raise LookupError("Neplatné jméno nebo heslo")

def get_secret(auth: str) -> str:
    for user in users:
        if user.auth == auth and user.active == True:
            # if user.username == "bob":
            #     raise Exception(
            #         "Super, objevil jsi chybu ;) - API vrací neznámou chybu"
            #     )
            return user.secret
        elif (
            user.auth == auth and user.username == "joe" and joe_should_been_logged_out
        ):
            return "Super, objevil jsi chybu - dostal jsi tajemství Joa, ačkoliv se odhlásil"
    raise ValueError("Neplatný token")

# def logout(auth: str) -> None:
#     for user in users:
#         if user.auth == auth and user.active == True:
#             if user.username == "joe":
#                 global joe_should_been_logged_out
#                 joe_should_been_logged_out = True
#             else:
#                 user.active = False

def logout(auth: str) -> None:
    for user in users:
        if user.auth == auth:
            if not user.active:
                raise ValueError("Uživatel je již odhlášen")
            user.active = False
            return
    raise ValueError("Neplatný token")



# Přihlašování typicky funguje tak, že se přihlásíme (login) pomocí hesla a přihlašovacího jména a server nám vrátí nějaký náhodný řetězec (tzv. token nebo authToken). Když se pak chceme dostat k nějaké informaci, kterou máme na serveru uloženou, tak už pošleme jen požadavek s daným authTokenem. Pokud odpovídá našemu účtu, tak dostaneme naši informaci. Když se odhlásíme, tak se přihlášení zneplatní (tedy pokud někdo přijde s daným authTokenem, tak nic nedostane).

# Pro zjednodušení je v tomto případě authToken pro každého uživatele dopředu znám (ale pokud se uživatel předtím nepřihlásil, tak není platný) a tajná informace uživatele je jen krátký string.

