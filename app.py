from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt


app = Flask(__name__)
bcrypt = Bcrypt(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usuarios.db' #Conecta o arquivo 'app.py' ao banco de dados 'usuarios.db'
app.config['SECRET_KEY'] = 'chavesecreta'

db = SQLAlchemy(app)
app.app_context().push()

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.view = "home"

@login_manager.user_loader
def load_user(user_id):
   return User.query.get(int(user_id))


# Instanciar a tabela de Usuarios
# Digite no Terminal:
#  python
#  from app import app
#  from app import db
#  db.create_all()

class User(db.Model, UserMixin):
   id = db.Column(db.Integer, primary_key=True)
   username = db.Column(db.String(20), nullable=False, unique=True)
   password = db.Column(db.String(80), nullable=False)


# Criação do formulario de cadastro de usuario
class FormCadastro(FlaskForm):
   username = StringField(validators=[InputRequired(), Length(
      min=4, max=20)], render_kw={"placeholder": "Usuario"})
   
   password = PasswordField(validators=[InputRequired(), Length(
      min=4, max=20)], render_kw={"placeholder": "Senha"})
   
   submit = SubmitField("Cadastrar")

   def validar_username(self, username):
      existing_user_username = User.query.filter_by(
         username=username.data).first()
      
      if existing_user_username:
         raise ValidationError("Este usuário já existe. Por favor digite um usuário diferente")


# Criação do formulario de login
class FormLogin(FlaskForm):
   username = StringField(validators=[InputRequired(), Length(
      min=4, max=20)], render_kw={"placeholder": "Usuário"})
   
   password = PasswordField(validators=[InputRequired(), Length(
      min=4, max=20)], render_kw={"placeholder": "Senha"})
   
   submit = SubmitField("Entrar")


# Criação das rotas do sistema

@app.route('/', methods=['GET', 'POST'])
def home():
   form = FormLogin()
   if form.validate_on_submit():
      user = User.query.filter_by(username=form.username.data).first()
      if user:
         if bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('dashboard'))

   return render_template('login.html', form=form)


@app.route('/cadastrar_usuario', methods=['GET', 'POST'])
def cadastrar_usuario():
   form = FormCadastro()

   if form.validate_on_submit():
      hashed_password = bcrypt.generate_password_hash(form.password.data)
      new_user = User(username=form.username.data, password=hashed_password)
      db.session.add(new_user)
      db.session.commit()
      return redirect(url_for('home'))

   return render_template('cad_usuario.html', form=form)


@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
   return render_template('dashboard.html')


@app.route('/logout')
@login_required
def logout():
   logout_user()
   return redirect(url_for('home'))


if __name__ == '__main__':
   app.run(debug=True)