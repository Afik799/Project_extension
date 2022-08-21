import requests
# import db_connector

user_id = 789
user_name = "TomandJerry"
user_json = {"user_name": f"{user_name}"}
res = requests.post(url=f"http://0.0.0.0:5000/users/{int(user_id)}", json=user_json)
if res.ok:
    print(f"Test succeeded! user {user_id} was added")
# else:
#     print(f"ID: {user_id} already exists!")

res2 = requests.get(url=f"http://0.0.0.0:5000/users/{int(user_id)}")
print(res2)
print(res2.json()["user_name"])

# check_db = db_connector.get_username(user_id)
# print(f"user id: {user_id} is bound in DB to {check_db}")
