from flask import Flask, request
from flask_restful import Resource, Api
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap

application = app = Flask(__name__)
api = Api(app)
app.config.from_object(Config)

login = LoginManager(app)
login.login_view = 'login'
db = SQLAlchemy(app)
migrate = Migrate(app,db)
bootstrap = Bootstrap(app)

from app import routes, models, errors

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080,debug=True)