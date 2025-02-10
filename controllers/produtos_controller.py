from main import app
from flask import request, render_template, redirect, url_for, session
from models.cliente_model import *
from models.conexao import *
from models.pet_model import *
from models.servicos_model import *


@app.route("/produtos", methods=['GET'])
def listar_produtos():
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    produtos = db.query(Cliente).all()  # Busca todos os produtos no banco
    db.close()
    return render_template("/produtos/lista_produtos.html", produtos=produtos)

@app.route("/produtos/inserir", methods=['GET'])
def produtos():
    return render_template("/produtos/create_produtos.html")

@app.route("/pet/inserir", methods=['GET'])
def produtos():
    produtos_id = session.get("produtos_id")
    if not produtos_id:
        return "Erro: Produto não encontrado!", 400
    return render_template("/produtos/create_produtos.html", produtos_id=produtos_id)

@app.route("/produtos/inserir", methods=['POST'])
def create_produtos():   
    if request.method == 'POST':    
        # Captura os dados do formulário      
        nome = request.form['nome']
        description = request.form['description']
        price = request.form['price']   
        quantity = request.form['quantity']   

        # Cria um novo produtos     
        new_client = Cliente(name=nome, description=description, price=price, quantity=quantity)
        
        # Cria a sessão com o banco de dados
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        db = SessionLocal()
        db.add(new_produtos)
        db.commit()
        db.refresh(new_produtos)

        # Salva o ID do produto na sessão
        session["produtos_id"] = new_produtos.produtos_id

        db.close()
        

        # Redireciona para o cadastro do produtos
        return redirect(url_for('produtos'))