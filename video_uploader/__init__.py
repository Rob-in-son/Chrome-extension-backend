from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

#Initialize app
app = Flask(__name__)
#Initialize CORS
CORS(app)


#The absolute path of the current folder 
basedir = os.path.abspath(os.path.dirname(__file__))

#Configure sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

#Initialize sqlalchemy
db = SQLAlchemy(app)

#Run server
if __name__ == "__main__":
    app.run(debug=True)