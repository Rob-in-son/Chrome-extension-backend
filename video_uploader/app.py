from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import config
import os

#Initialize app
app = Flask(__name__)
#Initialize CORS
CORS(app)

#Load db config from config.py file
app.config.from_object(config.Config)

#Initialize sqlalchemy
db = SQLAlchemy(app)

#Run server
if __name__ == "__main__":
    app.run(debug=True)