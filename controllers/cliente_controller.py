from main import app
from flask import request, render_template, redirect, url_for, session
from models.cliente_model import *
from models.conexao import *

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@app.route("/cliente/inserir")
def cliente():
    return render_template("/cliente/create_cliente.html")

@app.route("/cliente/inserir", methods=['POST'])
def create_client():   
    if request.method == 'POST':      
        # Captura os dados enviados pelo formulário        
        nome = request.form['nome']
        cpf = request.form['cpf']
        email = request.form['email']   
        endereco = request.form['endereco']   
        telefone = request.form['telefone']

        # Cria um novo cliente      
        new_client = Cliente(name=nome, cpf=cpf, email=email, phone=telefone, address=endereco)      
        
        # Cria a sessão
        db = SessionLocal()
        
        # Adiciona o novo usuário ao banco de dados
        db.add(new_client)
        db.commit()
        
        # Retorna para página de login
        return redirect(url_for('cliente'))