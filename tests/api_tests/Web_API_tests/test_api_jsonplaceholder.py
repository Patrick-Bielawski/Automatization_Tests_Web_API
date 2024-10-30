import requests # JEN TESTOVACÍ API NIC SE NEUKLÁDÁ DO DB
#__GET__
# response = requests.get("https://jsonplaceholder.typicode.com/users/")

# code = response.status_code
# msg = response.text
# body = response.json()

# print(code)
# print(msg)
# print(body)

# # posílám požadavek na daný endpoint
# response = requests.get("https://jsonplaceholder.typicode.com/posts")
# # tělo odpovědi si převedu na list uživatelů
# posts = response.json()
# # vytisknu si počet článků
# print("Počet článků je:", len(posts))

#__POST__

# body = {
#     "username": "Patrick_Test",
#     "password": "1234",
#     "name": "Patrick",
#     "surname": "Bie",
#     "email": "patrick.bie@gmail.com",
#     "age": 30,
# }
# response = requests.post("https://jsonplaceholder.typicode.com/users", json=body)
# code = response.status_code
# print(code)
# print(response.json())

#__PUT__

# body = {
#     "body": "tento článek teď vypadá úplně jinak než předtím",
# }
# post_id = 1
# response = requests.put(
#     f"https://jsonplaceholder.typicode.com/users/{post_id}", json=body
# )
# code = response.status_code
# print(code)
# print(response.json())

#__DELETE__

response = requests.delete("https://jsonplaceholder.typicode.com/photos/50")
print(response.status_code)
print(response.json())