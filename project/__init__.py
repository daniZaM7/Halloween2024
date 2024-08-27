from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///comunidade.db"
app.config["SECRET_KEY"] = "880d2aaf49c4b16827a3f3ab501992bb"

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"

"""class Usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String(150), nullable=False, unique=True)
    email = database.Column(database.String(150), nullable=False, unique=True)
    senha = database.Column(database.String(60), nullable=False)

@login_manager.user_loader
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))"""

from project import routes