from main import app
from flask import request, render_template, redirect, url_for, session
from models.cliente_model import *
from models.conexao import *
from models.pet_model import *
from models.produtos_model import *


@app.route("/servicos", methods=['GET'])
def listar_servicos():
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    servicos = db.query(Servicos).all()  # Busca todos os servicos no banco
    db.close()
    return render_template("/servicos/lista_servicos.html", servicos=servicos)

@app.route("/servicos/inserir", methods=['GET'])
def servicos():
    return render_template("/servicos/create_servicos.html")

@app.route("/servicos/inserir", methods=['GET'])
def servicos():
    servicos_id = session.get("servicos_id")
    if not servicos_id:
        return "Erro: Servico não encontrado!", 400
    return render_template("/servicos/create_servicos.html", servicos_id=servicos_id)

@app.route("/servicos/inserir", methods=['POST'])
def create_servicos():   
    if request.method == 'POST':    
        # Captura os dados do formulário      
        nome = request.form['nome']
        price = request.form['price']
        description = request.form['description']   

        # Cria um novo servico    
        new_servicos = Servicos(name=nome, price=price, description=description)
        
        # Cria a sessão com o banco de dados
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        db = SessionLocal()
        db.add(new_servicos)
        db.commit()
        db.refresh(new_servicos)

        # Salva o ID do servico na sessão
        session["servicos_id"] = new_servicos.servicos_id

        db.close()
        

        # Redireciona para o cadastro do servico
        return redirect(url_for('servicos'))