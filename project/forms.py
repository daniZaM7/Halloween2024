#criar os formularios do nosso site
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

#from project import Usuario
from project.models import Usuario

class FormLogin(FlaskForm):
    email = StringField("E-mail", validators = [DataRequired(),Email()])
    senha = PasswordField("Senha", validators = [DataRequired()])
    botao_confirmacao = SubmitField("Fazer login")

class FormCriarConta(FlaskForm):
    email= StringField("E-mail", validators = [DataRequired(),Email()])
    username= StringField("Nome de usuário", validators = [DataRequired()])
    senha= PasswordField("Senha", validators = [DataRequired(), Length(6,20)])
    confirmacao_senha=  PasswordField("Confirmação de Senha", validators=[DataRequired(), EqualTo("senha")])
    botao_confirmacao= SubmitField("Criar Conta")

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            return ValidationError("E-mail já cadastrado.")