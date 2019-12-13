from flask import Flask
from config import Config
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

dinner = Flask(__name__)
dinner.config.from_object(Config)
dinner.config['SQLALCHEMY_DATABASE_URI'] = 'mysql + pymsql://cp36696_admireso:social.admire@localhost/cp36696_admireso'
db = SQLAlchemy(dinner)

login = LoginManager(dinner)


from dinner import routes, models