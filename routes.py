
from flask import request, jsonify, Blueprint
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime
from estados.message_handler import Message_handler
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

        query = "INSERT INTO messages (content, role, datetime) values (%s, %s, %s)"
        cursor.execute(query, (content, role, datetime.now()))
        connection.commit()

        cursor.close()
        connection.close()
        return jsonify({"message": "Dados salvos com sucesso!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@routes.route('/process_data', methods=['POST'])
def process_data():
    data = request.json  # Assume que o dado é enviado como JSON no corpo da solicitação POST

    message_history = data['message_history']

    openai_response =  Message_handler().send_message(message_history=message_history)
    # Aqui você pode processar o dado como desejar
    return jsonify(openai_response)