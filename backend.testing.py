import requests
import db_connector

user_id = 9
res = requests.post(url=f"http://localhost:5000/users/{int(user_id)}", json={"user_name": "eliran"})
if res.ok:
    print(f"Test succeeded! user {user_id} was added")
else:
    print(f"ID: {user_id} already exists!")

res2 = requests.get(url=f"http://localhost:5000/users/{user_id}")
print(res2)
print(res2.json()["user_name"])

check_db = db_connector.get_username(user_id)
print(f"user id: {user_id} is bound in DB to {check_db}")
