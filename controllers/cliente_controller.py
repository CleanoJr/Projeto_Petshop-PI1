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
        # Captura os dados do formulário        
        nome = request.form['nome']
        cpf = request.form['cpf']
        email = request.form['email']   
        endereco = request.form['endereco']   
        telefone = request.form['telefone']

        # Cria um novo cliente      
        new_client = Cliente(name=nome, cpf=cpf, email=email, phone=telefone, address=endereco)      
        
        # Cria a sessão com o banco de dados
        db = SessionLocal()
        db.add(new_client)
        db.commit()
        db.refresh(new_client)

        # Salva o ID do cliente na sessão
        session["client_id"] = new_client.client_id
        
        print(f"Cliente ID armazenado na sessão: {session['client_id']}")

        # Redireciona para o cadastro do pet
        return redirect(url_for('pet'))
