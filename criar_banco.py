from project import database, app
from project.models import Usuario

with app.app_context():
    database.create_all()