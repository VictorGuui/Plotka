
from flask import request, jsonify, Blueprint
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime
from db import connect_db

routes = Blueprint('routes', __name__)

@routes.route("/send-message", methods=["POST"])
def sendMessage():
    try:
        body = request.get_json()
        content = body.get("content")
        role = "PEDROCA"

        connection = connect_db()
        cursor = connection.cursor()

        query = "INSERT INTO messages values (%s, %s)"
        cursor.execute(query, (content, role))
        connection.commit()

        cursor.close()
        connection.close()
        return jsonify({"message": "Dados salvos com sucesso!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
