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



import pytest
from src_api.api_students import create_student, is_student_in_database, delete_student

@pytest.mark.parametrize("firstname, lastname, email, age", [
    ("Pepa", "NOVÁK", "pepa.novak@gmail.com", 25),
    ("Jana", "NOVÁKOVÁ", "jana.novak@gmail.com", 30),
])
def test_get_correct_input(firstname, lastname, email, age):
    # Vytvoření nového studenta
    student = create_student(firstname, lastname, email, age)
    
    # Ověření, zda byl student vytvořen a je v databázi
    assert is_student_in_database(student["id"]) is True
    
    # Ověření, zda jsou data studenta správná
    assert student["firstName"] == firstname
    assert student["lastName"] == lastname
    assert student["email"] == email
    assert student["age"] == age
    
    # Smazání testovacího záznamu
    delete_student(student["id"])
    
    # Ověření, že student byl smazán
    assert is_student_in_database(student["id"]) is False
