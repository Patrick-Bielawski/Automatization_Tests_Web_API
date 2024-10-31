# import pytest
# from src_api import api_students

# @pytest.mark.parametrize("firstname, lastname, email, age",
#      [
#         ("Pepa", "NOVÁK", "pepa.novak@gmail.com", 25),
#         ("Jana", "NOVÁKOVÁ", "jana.novak@gmail.com", 30),
#      ],
#      )

# def test_get_correct_input(firstname, lastname, emial, age):
#     student = create_student(firstname, lastname, emial, age)
#     response = request.get(f"{URL}{student['id']}")
#     delete_student(
#         student["id"]
#     )

# assert response.status_code == 200
# assert student["firstName"] == firstname
# assert student["lastName"] == lastname
# assert student["email"] == email
# assert student["age"] == age


#__Korektní vstup__
import pytest
import requests
from src_api.api_students import create_student, is_student_in_database, delete_student, URL

# @pytest.mark.parametrize("firstname, lastname, email, age", [
#     ("Pepa", "NOVÁK", "pepa.novak@gmail.com", 25),
#     ("Jana", "NOVÁKOVÁ", "jana.novak@gmail.com", 30),
# ])
# def test_get_correct_input(firstname, lastname, email, age):
#     # Vytvoření nového studenta
#     student = create_student(firstname, lastname, email, age)
    
#     # Ověření, zda byl student vytvořen a je v databázi
#     assert is_student_in_database(student["id"]) is True
    
#     # Ověření, zda jsou data studenta správná
#     assert student["firstName"] == firstname
#     assert student["lastName"] == lastname
#     assert student["email"] == email
#     assert student["age"] == age
    
#     # Smazání testovacího záznamu
#     delete_student(student["id"])
    
#     # Ověření, že student byl smazán
#     assert is_student_in_database(student["id"]) is False


# #__Nekorektní vstup__
# from src_api.api_students import is_student_in_database, URL

# @pytest.mark.parametrize(
#     "id",
#     [-1, 1000000, 988001],
# )
# def test_get_incorrect_input(id):
#     # Použití requests přímo, pokud chcete otestovat chybný požadavek, nebo is_student_in_database pro ověření existence
#     response = requests.get(f"{URL}{id}")
    
#     # Očekávaný stavový kód je 404 pro neexistujícího studenta
#     assert response.status_code == 404
#     assert response.json().get("message") == "Student not found"  # kontrola zprávy API


# #__Samostatný smazání studenta__

# @pytest.mark.parametrize(
#     "name, lastname, email, age",
#     [
#         ("Pepa", "NOVÁK", "pepa.novak@seznam.cz", 25),
#         ("Jana", "KOVÁŘOVÁ", "jana.kovarova@seznam.cz", 30),
#     ],
# )
# def test_delete_correct_input(name, lastname, email, age):
#     student = create_student(name, lastname, email, age)
#     response = requests.delete(f"{URL}{student['id']}")
#     assert response.status_code == 200
#     assert is_student_in_database(student["id"]) == False


#__POST Testování__
@pytest.mark.parametrize(
    "firstname, lastname, email, age, expected_code",
    [
        ("Pepa", "Novák", "pepa.novak@seznam.cz", 25, 200),
        ("Pepa", "Novák", "pepa.novak.cz", 25, 200),
        ("pepa", "Novák", "pepa.novak@seznam.cz", "25", 200),
        ("zdena", "Novák", "pepa.novak@seznam.cz", -5, 500),
        ("pepa", "Nov?ák", "pepa.novak@seznam.cz", "25", 200),
    ],
)




def test_post(firstname, lastname, email, age, expected_code):
    response = requests.post(
        URL, json={"firstName": firstname, "lastName": lastname, "email": email, "age": age}
    )

    code = response.status_code
    body = response.text
    db_student = {}

    if code // 100 == 2:
        body = response.json()
        db_student = requests.get(f"{URL}{body['id']}").json()
        delete_student(body["id"])

    assert code == expected_code

    if expected_code // 100 == 2:
        assert body["firstName"] == firstname
        assert body["lastName"] == lastname.upper()
        assert body["email"] == email
        assert body["age"] == age


# Najdi si nějakou otevřenou API (např. https://pokeapi.co/docs/v2, https://newsapi.org/, https://jokeapi.dev/, https://openweathermap.org/api a mnohé další).