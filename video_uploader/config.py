#Configure database
import os

#The absolute path of the current folder 
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:

    #Configure sqlite database
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False