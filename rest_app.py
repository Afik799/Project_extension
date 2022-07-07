import pymysql.err
from flask import Flask, request
import db_connector
from datetime import datetime

app = Flask(__name__)


@app.route("/users/<user_id>", methods=['POST', 'GET', 'PUT', 'DELETE'])
def get_user_name(user_id):
    if request.method == 'POST':
        try:
            user_data = request.json
            user_name = user_data.get("user_name")
            tup_db = (int(user_id), user_name, str(datetime.now()))
            db_connector.post_user_data(tup_db)
            return {"status": "ok", "user_added": user_name}, 200
        except pymysql.err.IntegrityError:
            return {"status": "error", "reason": "id already exists"}, 500

    elif request.method == 'GET':
        try:
            if db_connector.get_username(
                    int(user_id)) is not None:  # user_id is assigned with string type, while db will accept int
                return {"status": "ok", "user_name": db_connector.get_username(int(user_id))}, 200
            else:
                return {"status": "error", "reason": "no such id"}, 500
        except ValueError:
            return {"status": "error", "reason": "no such id"}, 500

    elif request.method == 'PUT':
        user_data = request.json
        user_name = user_data.get("user_name")
        db_connector.edit_user(user_name, int(user_id))
        if db_connector.edit_user(user_name, int(user_id)) is not None:
            return {"status": "ok", "user_updated": user_name}, 200
        else:
            return {"status": "error", "reason": "no such id"}, 500

    elif request.method == 'DELETE':
        if db_connector.delete_user(int(user_id)) != 0:
            return {"status": "ok", "user_deleted": user_id}, 200
        else:
            return {"status": "error", "reason": "no such id"}, 500


app.run(host='localhost', debug=True, port=5000)
