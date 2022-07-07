import pymysql

conn = pymysql.connect(host="remotemysql.com", port=3306, user='P0PvfGbwKl', passwd='BvZW0m8DXo')
conn.autocommit(True)

cursor = conn.cursor()


def post_user_data(data):
    return cursor.execute(f"INSERT into P0PvfGbwKl.users (user_id, user_name, creation_date) VALUES {data}")


def get_username(user_id):
    cursor.execute(f"SELECT * FROM P0PvfGbwKl.users;")

    for row in cursor:
        if user_id == row[0]:
            return row[1]


def edit_user(new_data, user_id):
    cursor.execute(f"SELECT * FROM P0PvfGbwKl.users;")

    for row in cursor:
        if user_id == row[0]:
            return cursor.execute(f"UPDATE P0PvfGbwKl.users SET user_name = '{new_data}' WHERE user_id = {user_id}")


def delete_user(user_id):
    cursor.execute(f"DELETE FROM P0PvfGbwKl.users WHERE user_id = {user_id}")
    return cursor.rowcount

# cursor.execute(f"SELECT * FROM P0PvfGbwKl.users;")
#
# for row in cursor:
#     print(row)