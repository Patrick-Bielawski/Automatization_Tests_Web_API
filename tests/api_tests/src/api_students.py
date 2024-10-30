import requests

URL = "http://108.143.193.45:8080/api/v1/students/"

def create_student(firstName, lastName, email, age):
    body = {
        "firstName": firstName,
        "lastName": lastName,
        "email": email,
        "age": age,
    }

    response = requests.post(URL, json=body)
    return response.json()

def is_student_in_database(id):
    response = requests.get(f"{URL}{id}")
    if response.status_code == 200:
        return True
    else:
        return False
    
def delete_student(id):
    response = requests.delete(f"{URL}{id}")
    return response.text
        
