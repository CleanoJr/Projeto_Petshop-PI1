from main import app
from flask import request, render_template, redirect, url_for, session, flash
from models.usuario_model import *
from models.conexao import *

# Criando a sessão para interagir com o banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Rotas

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")


@app.route('/logar', methods=['GET', 'POST'])
def logar():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
               
        db = SessionLocal()
        usuario = db.query(Usuario).filter(Usuario.login == username, Usuario.senha == password).first()
    
        if usuario:
            session['usuario_id'] = usuario.id
            return redirect(url_for('dashboard'))
        else:
            flash('Usuário ou senha inválidos!', 'danger')
        
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop('usuario_id', None)
    return redirect(url_for('login'))

@app.route("/usuario/inserir")
def inserir():
    return render_template("usuario/create.html")

@app.route("/usuario/inserir", methods=['POST'])
def create():   
    if request.method == 'POST':      
        # Captura os dados enviados pelo formulário        
        nome = request.form['nome']      
        login = request.form['login']
        senha = request.form['senha']      
        email = request.form['email']
        telefone = request.form['telefone']

        # Cria um novo usuário      
        new_user = Usuario(nome=nome, login=login, senha=senha, email=email, telefone=telefone)      
        
        # Cria a sessão
        db = SessionLocal()
        
        # Adiciona o novo usuário ao banco de dados
        db.add(new_user)
        db.commit()
        
        # Retorna para página de login
        flash('Cadastrado com sucesso!', 'success')
        return redirect(url_for('login'))

@app.route("/dashboard")
def dashboard():
    if 'usuario_id' not in session:
        return redirect(url_for('login'))

    db = SessionLocal()
    usuario = db.query(Usuario).filter(Usuario.id == session['usuario_id']).first()
    nome_usuario = usuario.nome if usuario else 'Usuário'

    return render_template("/agendamento/agendamento.html", nome_usuario=nome_usuario)

@app.route("/agendamento/novo_agendamento")
def cad_agendamento():
    return render_template("/agendamento/create_agendamento.html")
