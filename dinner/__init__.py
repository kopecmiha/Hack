from flask import Flask
from config import Config

dinner = Flask(__name__)
dinner.config.from_object(Config)


from dinner import routes
