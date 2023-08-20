from flask import Flask
from routes import routes
from flask_cors import CORS, cross_origin
import os

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:6NefcKuYfH3wTFm0Rgw1@containers-us-west-131.railway.app:6146/railway"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

app.register_blueprint(routes)

if __name__ == "__main__":
    app.run(debug=True)