from main import app
from flask import request, render_template, redirect, url_for
from models.usuario_model import *
# Criando a sessão para interagir com o banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# rotas
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
        return redirect(url_for('login'))

@app.route("/")
def login():
    return render_template("login.html")