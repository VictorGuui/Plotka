
from flask import request, jsonify, Blueprint
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime
from db import connect_db
from estados import message_handler

routes = Blueprint('routes', __name__)

@routes.route("/send-message", methods=["POST"])
def sendMessage():
    try:
        body = request.get_json()
        content = body.get("content")
        role = body.get("role")

        print(body)

        connection = connect_db()
        cursor = connection.cursor()


        query = "INSERT INTO messages (content, role, datetime) values (%s, %s, %s)"
        cursor.execute(query, (content, role, datetime.now()))
        connection.commit()

        cursor.close()
        connection.close()

        result = message_handler(body)
        
        return jsonify({"message": "Dados salvos com sucesso!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
