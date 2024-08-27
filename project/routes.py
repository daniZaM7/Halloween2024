#criar as rotas do nosso site (os links)
from flask import render_template, url_for, redirect
from project import app, database, bcrypt
from project.models import Usuario
from flask_login import login_required, login_user, logout_user, current_user
from project.forms import FormLogin, FormCriarConta

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    form_login = FormLogin()
    if form_login.validate_on_submit():
        usuario = Usuario.query.filter_by(email=form_login.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, form_login.senha.data):
            login_user(usuario)
            return redirect(url_for("perfil", id_usuario=usuario.id))
    return render_template("login.html", form=form_login)

@app.route("/criarconta", methods=['GET', 'POST'])
def criarconta():
    form_criarconta = FormCriarConta()
    if form_criarconta.validate_on_submit():
        senha = bcrypt.generate_password_hash(form_criarconta.senha.data)
        usuario = Usuario(username=form_criarconta.username.data,
                          senha=senha,
                          email=form_criarconta.email.data)
        database.session.add(usuario)
        database.session.commit()
        login_user(usuario, remember=True)
        return redirect(url_for("perfil", id_usuario=usuario.id))
    return render_template("criarconta.html", form=form_criarconta)

@app.route("/perfil/<id_usuario>")
@login_required
def perfil(id_usuario):
    if int(id_usuario) == int(current_user.id):
        return render_template("perfil.html", usuario=current_user)
    else:
        usuario = Usuario.query.get(int(id_usuario))
        return render_template("perfil.html", usuario=usuario)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("homepage"))