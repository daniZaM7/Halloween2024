#criar a estrutura do banco de dados

from project import database, login_manager
#from datetime import datetime
from flask_login import UserMixin

class Usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String(150), nullable=False, unique=True)
    email = database.Column(database.String(150), nullable=False, unique=True)
    senha = database.Column(database.String(60), nullable=False)

@login_manager.user_loader
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))

