from flask import Flask, request
import db_connector

app = Flask(__name__)


@app.route("/users/get_user_data/<user_id>", methods=['GET'])
def get_username(user_id):
    if request.method == 'GET':
        user_name = db_connector.get_username(int(user_id))
        if user_name is not None:
            return "<H1 id='user'>" + str(user_name) + "</H1>", 200
        else:
            return "<H1 id='error'>" "no such user id: " + user_id + "</H1>", 500


app.run(host='localhost', debug=True, port=5001)
